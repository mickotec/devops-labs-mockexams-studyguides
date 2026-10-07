#!/usr/bin/env python3
"""
CKA & LFCS Daily Study Todo — Flask Web App
Serves the 8-week study schedule as an interactive web dashboard.
Progress persists in ~/.local/share/study_todo/progress.json
"""

import codecs
import csv
import fcntl
import json
import os
import pty
import re
import select
import signal
import struct
import subprocess
import sys
import termios
import threading
import time
from datetime import datetime, timedelta
DIR = Path(__file__).resolve().parent
LFCS_DIR = DIR.parent
REPO_DIR = LFCS_DIR.parent
TOOLS_DIR = REPO_DIR / "tools"

if str(DIR) not in sys.path:
    sys.path.insert(0, str(DIR))
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

from flask import Flask, jsonify, render_template, request
from flask_sock import Sock
try:
    from exam_service import (
        get_all_mock_exams,
        get_exam_metadata,
        get_exam_result,
        parse_grade_output,
        run_exam_action,
        submit_and_grade_exam,
    )
except ImportError:
    from lfcs.webapp.exam_service import (
        get_all_mock_exams,
        get_exam_metadata,
        get_exam_result,
        parse_grade_output,
        run_exam_action,
        submit_and_grade_exam,
    )

DATA_DIR = Path.home() / ".local" / "share" / "study_todo"
PROGRESS_FILE = DATA_DIR / "lfcs_progress.json"
SCHEDULE_CSV = LFCS_DIR / "schedule.csv"
if not SCHEDULE_CSV.exists():
    SCHEDULE_CSV = LFCS_DIR / "schedule.template.csv"

BASE_DIR = REPO_DIR

app = Flask(__name__,
            template_folder=str(DIR / "templates"),
            static_folder=str(DIR / "static"))
sock = Sock(app)

START_DATE = datetime(2026, 9, 14)


# ── Progress persistence ─────────────────────────────────────
SETTINGS_FILE = DATA_DIR / "settings.json"


def load_settings():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    defaults = {"notification_minutes_before": 5, "desktop_notifications": True}
    if SETTINGS_FILE.exists():
        try:
            data = json.loads(SETTINGS_FILE.read_text())
            defaults.update(data)
            return defaults
        except (json.JSONDecodeError, OSError):
            return defaults
    return defaults


def save_settings(settings):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2))


def load_progress():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_progress(progress):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))


# ── Curriculum loader ─────────────────────────────────────────
def load_curriculum():
    sys.path.insert(0, str(BASE_DIR))
    checklists = {}
    week_topics = {}
    try:
        from curriculum import WEEKS
        for wi in range(1, 9):
            wmod = WEEKS.get(wi)
            if not wmod:
                continue
            if wmod.__doc__:
                for line in wmod.__doc__.strip().split("\n"):
                    line = line.strip()
                    m = re.match(r"Day\s+(\d+):\s*(.*)", line)
                    if m:
                        dn = int(m.group(1))
                        parts = m.group(2).split("|")
                        cka = parts[0].strip()
                        lfcs = parts[1].strip() if len(parts) > 1 else "LFCS Study"
                        week_topics[(wi, dn)] = (cka, lfcs)
            for d in range(1, 7):
                fn = f"get_day_{d}"
                if hasattr(wmod, fn):
                    result = getattr(wmod, fn)()
                    items = []
                    for item in result.get("checklist", []):
                        if isinstance(item, (list, tuple)) and len(item) >= 2:
                            hint = item[2] if len(item) > 2 else ""
                            items.append({"track": item[0],
                                          "task": item[1], "hint": hint})
                    checklists[(wi, d)] = items
    except Exception:
        pass
    return checklists, week_topics


CHECKLISTS, WEEK_TOPICS = load_curriculum()


# ── Schedule CSV parser ───────────────────────────────────────
def parse_csv():
    days = {}
    if not SCHEDULE_CSV.exists():
        return days
    with open(SCHEDULE_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subject = row.get("Subject", "").strip()
            date_str = row.get("Start Date", "").strip()
            start_time = row.get("Start Time", "").strip()
            end_time = row.get("End Time", "").strip()
            desc = row.get("Description", "").strip()
            if not date_str or not subject:
                continue
            if "[CKA]" in subject:
                btype = "CKA"
            elif "[LFCS]" in subject:
                btype = "LFCS"
            elif "[RECOVERY]" in subject:
                btype = "RECOVERY"
            elif "[REST]" in subject:
                btype = "REST"
            else:
                btype = "OTHER"
            title = subject
            for tag in ["[CKA]", "[LFCS]", "[RECOVERY]", "[REST]"]:
                title = title.replace(tag, "").strip()
            tasks = []
            if desc:
                for line in desc.split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    skip = ("CKA STUDY BLOCK", "LFCS STUDY BLOCK",
                            "COGNITIVE RECOVERY")
                    if any(line.startswith(p) for p in skip):
                        continue
                    m = re.match(
                        r"(\d{2}:\d{2}\s*[AP]M)\s*-\s*(\d{2}:\d{2}\s*[AP]M):\s*(.*)",
                        line)
                    if m:
                        tasks.append(f"{m.group(1)}-{m.group(2)}: {m.group(3)}")
                    else:
                        tasks.append(line)
            block = {"type": btype, "title": title,
                     "time": f"{start_time} - {end_time}", "tasks": tasks}
            days.setdefault(date_str, []).append(block)
    return days


CSV_DAYS = parse_csv()


# ── Build full schedule ───────────────────────────────────────
def build_schedule():
    days = {}
    all_dates = []

    # --- Week 1 (Sep 14 - Sep 20, 2026) ---
    week_start = START_DATE
    for dow in range(6):
        dt = week_start + timedelta(days=dow)
        ds = dt.strftime("%m/%d/%Y")
        all_dates.append(ds)
        day_num = dow + 1

        if ds in CSV_DAYS:
            days[ds] = CSV_DAYS[ds]
            cl = CHECKLISTS.get((1, day_num), [])
            if cl:
                _add_checklist(days[ds], cl, 1, day_num)
        else:
            cka_t, lfcs_t = WEEK_TOPICS.get(
                (1, day_num), ("CKA Study", "LFCS Study"))
            days[ds] = _gen_blocks(1, day_num, cka_t, lfcs_t,
                                   CHECKLISTS.get((1, day_num), []))

    rest_dt = week_start + timedelta(days=6)
    rs = rest_dt.strftime("%m/%d/%Y")
    all_dates.append(rs)
    days[rs] = [{
        "type": "REST",
        "title": "Full Recovery & Memory Consolidation (Week 1)",
        "time": "All Day",
        "tasks": [
            "Complete detachment from code and terminal",
            "Physical movement, outdoor activities, social time",
            "Restorative sleep for synaptic consolidation",
        ]
    }]

    # --- 2-Week Pause Period (Sep 21 - Oct 04, 2026) ---
    pause_start = START_DATE + timedelta(weeks=1)
    for day_offset in range(14):
        dt = pause_start + timedelta(days=day_offset)
        ds = dt.strftime("%m/%d/%Y")
        all_dates.append(ds)
        if ds in CSV_DAYS:
            days[ds] = CSV_DAYS[ds]
        else:
            days[ds] = [{
                "type": "REST",
                "title": "Study Paused — Family Matters Break",
                "time": "All Day",
                "tasks": [
                    "Study temporarily paused due to family matters.",
                    "Resumes with Week 2 on Monday, October 5, 2026.",
                ]
            }]

    # --- Weeks 2 to 8 (Pushed to start Monday, Oct 05, 2026) ---
    for week in range(2, 9):
        # Week 2 starts at week offset 3 (START_DATE + 3 weeks = Oct 05, 2026)
        week_start = START_DATE + timedelta(weeks=week + 1)
        for dow in range(6):
            dt = week_start + timedelta(days=dow)
            ds = dt.strftime("%m/%d/%Y")
            all_dates.append(ds)
            day_num = dow + 1

            if ds in CSV_DAYS:
                days[ds] = CSV_DAYS[ds]
                cl = CHECKLISTS.get((week, day_num), [])
                if cl:
                    _add_checklist(days[ds], cl, week, day_num)
            else:
                cka_t, lfcs_t = WEEK_TOPICS.get(
                    (week, day_num), ("CKA Study", "LFCS Study"))
                days[ds] = _gen_blocks(week, day_num, cka_t, lfcs_t,
                                       CHECKLISTS.get((week, day_num), []))

        rest_dt = week_start + timedelta(days=6)
        rs = rest_dt.strftime("%m/%d/%Y")
        all_dates.append(rs)
        days[rs] = [{
            "type": "REST",
            "title": f"Full Recovery & Memory Consolidation (Week {week})",
            "time": "All Day",
            "tasks": [
                "Complete detachment from code and terminal",
                "Physical movement, outdoor activities, social time",
                "Restorative sleep for synaptic consolidation",
            ]
        }]

    return days, all_dates


def _gen_blocks(week, day, cka_t, lfcs_t, cl):
    blocks = [
        {"type": "CKA", "title": f"8am-12pm: {cka_t}",
         "time": "08:00 AM - 12:00 PM", "tasks": [
             "08:00 AM-08:20 AM: Warm-up retrieval practice",
             f"08:20 AM-09:30 AM: Theory: {cka_t}",
             "09:30 AM-09:45 AM: Physical reset & hydration",
             "09:45 AM-11:15 AM: Hands-on labs & practice",
             "11:15 AM-11:30 AM: Eye rest & micro-break",
             "11:30 AM-12:00 PM: Exploratory practice & notes"]},
        {"type": "RECOVERY",
         "title": "12pm-3pm: Cognitive Reset & Physical Regeneration",
         "time": "12:00 PM - 03:00 PM", "tasks": [
             "12:00 PM-01:00 PM: Nutritious lunch & screen detachment",
             "01:00 PM-02:00 PM: Aerobic exercise / walk (BDNF boost)",
             "02:00 PM-02:45 PM: Power nap or NSDR",
             "02:45 PM-03:00 PM: Terminal & desk prep for LFCS"]},
        {"type": "LFCS", "title": f"3pm-6pm: {lfcs_t}",
         "time": "03:00 PM - 06:00 PM", "tasks": [
             "03:00 PM-03:20 PM: Warm-up drills",
             f"03:20 PM-04:20 PM: Theory: {lfcs_t}",
             "04:20 PM-04:35 PM: Movement break",
             "04:35 PM-05:35 PM: Hands-on labs & practice",
             "05:35 PM-06:00 PM: Synthesis & cheat sheet update"]},
    ]
    if cl:
        _add_checklist(blocks, cl, week, day)
    return blocks


def _add_checklist(blocks, cl, week, day):
    tasks = [f"[{it['track']}] {it['task']}" for it in cl]
    blocks.append({
        "type": "CHECK",
        "title": f"Self-Check: W{week}D{day} Mastery Verification",
        "time": "End of Day",
        "tasks": tasks,
        "is_checklist": True,
    })


SCHEDULE, DATES = build_schedule()


# ── API helpers ───────────────────────────────────────────────
def task_key(date_str, block_idx, task_idx):
    return f"{date_str}|{block_idx}|{task_idx}"


def day_meta(date_str, idx, progress):
    try:
        dt = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        dt = datetime.now()
    week = idx // 7 + 1
    day_in_week = idx % 7 + 1
    blocks = SCHEDULE.get(date_str, [])
    total = done = 0
    for bi, block in enumerate(blocks):
        for ti in range(len(block["tasks"])):
            total += 1
            if progress.get(task_key(date_str, bi, ti), False):
                done += 1
    is_rest = day_in_week == 7
    if week in (2, 3):
        day_label = f"Pause {week-1} {'REST' if is_rest else f'Day {day_in_week}'} — {dt.strftime('%a %b %d')}"
    elif week >= 4:
        curr_week = week - 2
        day_label = f"Week {curr_week} {'REST' if is_rest else f'Day {day_in_week}'} — {dt.strftime('%a %b %d')}"
    else:
        day_label = f"Week {week} {'REST' if is_rest else f'Day {day_in_week}'} — {dt.strftime('%a %b %d')}"

    return {
        "date": date_str,
        "iso": dt.strftime("%Y-%m-%d"),
        "weekday": dt.strftime("%a"),
        "formatted": dt.strftime("%b %d, %Y"),
        "week": week,
        "dayInWeek": day_in_week,
        "isRest": is_rest,
        "label": day_label,
        "done": done,
        "total": total,
        "pct": round(done / total * 100) if total else 0,
    }


# ── Desktop Notification Scheduler ────────────────────────────
sent_notifications = set()

def parse_time_str(date_str, t_str):
    try:
        dt_base = datetime.strptime(date_str, "%m/%d/%Y")
        t_clean = t_str.strip().upper()
        # format like 08:00 AM or 8:00 AM
        dt_time = datetime.strptime(t_clean, "%I:%M %p")
        return dt_base.replace(hour=dt_time.hour, minute=dt_time.minute, second=0, microsecond=0)
    except Exception:
        return None

def extract_task_start_time(date_str, task_text, block_time_str):
    m = re.match(r"^(\d{1,2}:\d{2}\s*[AP]M)", task_text)
    if m:
        return parse_time_str(date_str, m.group(1))
    if block_time_str and " - " in block_time_str:
        start_part = block_time_str.split(" - ")[0].strip()
        return parse_time_str(date_str, start_part)
    return None

def send_linux_notification(title, message, urgency="normal"):
    try:
        subprocess.run([
            "notify-send",
            "-a", "Study Todo",
            "-u", urgency,
            "-i", "appointment-soon",
            title,
            message
        ], check=False)
    except Exception:
        pass

def notification_daemon():
    while True:
        try:
            settings = load_settings()
            if settings.get("desktop_notifications", True):
                lead_mins = int(settings.get("notification_minutes_before", 5))
                now = datetime.now()
                today_str = now.strftime("%m/%d/%Y")
                blocks = SCHEDULE.get(today_str, [])
                
                for bi, block in enumerate(blocks):
                    for ti, task_text in enumerate(block["tasks"]):
                        key = task_key(today_str, bi, ti)
                        task_start = extract_task_start_time(today_str, task_text, block.get("time", ""))
                        if task_start:
                            notify_target_time = task_start - timedelta(minutes=lead_mins)
                            # Window of 60s
                            if timedelta(seconds=0) <= (now - notify_target_time) <= timedelta(seconds=70):
                                notif_id = f"{key}_{task_start.strftime('%H%M')}_{lead_mins}"
                                if notif_id not in sent_notifications:
                                    sent_notifications.add(notif_id)
                                    title = f"[{block['type']}] Upcoming Task in {lead_mins}m"
                                    msg = f"Starts at {task_start.strftime('%I:%M %p')}\n{task_text}"
                                    send_linux_notification(title, msg)
        except Exception:
            pass
        time.sleep(30)


# ── Routes ────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/schedule")
def api_schedule():
    progress = load_progress()
    today = datetime.now().strftime("%m/%d/%Y")
    today_idx = 0
    for i, d in enumerate(DATES):
        if d == today:
            today_idx = i
            break
        try:
            dt = datetime.strptime(d, "%m/%d/%Y")
            if dt.date() >= datetime.now().date():
                today_idx = i
                break
        except ValueError:
            pass

    weeks_summary = []
    total_weeks = (len(DATES) + 6) // 7
    for wk in range(1, total_weeks + 1):
        wk_done = wk_total = 0
        for di in range(7):
            idx = (wk - 1) * 7 + di
            if idx < len(DATES):
                d = DATES[idx]
                for bi, block in enumerate(SCHEDULE.get(d, [])):
                    for ti in range(len(block["tasks"])):
                        wk_total += 1
                        if progress.get(task_key(d, bi, ti), False):
                            wk_done += 1

        if wk == 1:
            tab_name = "Week 1"
        elif wk in (2, 3):
            tab_name = f"Pause {wk-1}"
        elif wk < total_weeks:
            tab_name = f"Week {wk-2} (W{wk})"
        else:
            tab_name = "Week 8 (Mocks)"

        weeks_summary.append({
            "week": wk, "name": tab_name, "done": wk_done, "total": wk_total,
            "pct": round(wk_done / wk_total * 100) if wk_total else 0
        })

    all_days = [day_meta(DATES[i], i, progress) for i in range(len(DATES))]
    o_done = sum(d["done"] for d in all_days)
    o_total = sum(d["total"] for d in all_days)

    return jsonify({
        "days": all_days,
        "weeks": weeks_summary,
        "todayIndex": today_idx,
        "overall": {"done": o_done, "total": o_total,
                    "pct": round(o_done / o_total * 100) if o_total else 0},
    })


@app.route("/api/day/<path:date_str>")
def api_day(date_str):
    progress = load_progress()
    blocks = SCHEDULE.get(date_str, [])
    result = []
    for bi, block in enumerate(blocks):
        tasks = []
        for ti, task_text in enumerate(block["tasks"]):
            key = task_key(date_str, bi, ti)
            tasks.append({
                "key": key,
                "text": task_text,
                "done": progress.get(key, False),
                "track": _detect_track(task_text, block),
            })
        result.append({
            "type": block["type"],
            "title": block["title"],
            "time": block["time"],
            "tasks": tasks,
            "isChecklist": block.get("is_checklist", False),
        })
    return jsonify({"blocks": result})


def _detect_track(text, block):
    if text.startswith("[CKA]"):
        return "CKA"
    if text.startswith("[LFCS]"):
        return "LFCS"
    return block["type"]


@app.route("/api/toggle", methods=["POST"])
def api_toggle():
    data = request.get_json()
    key = data.get("key")
    if not key:
        return jsonify({"error": "missing key"}), 400
    progress = load_progress()
    progress[key] = not progress.get(key, False)
    save_progress(progress)
    return jsonify({"key": key, "done": progress[key]})


@app.route("/api/toggle_all", methods=["POST"])
def api_toggle_all():
    data = request.get_json()
    date_str = data.get("date")
    value = data.get("value", True)
    if not date_str:
        return jsonify({"error": "missing date"}), 400
    progress = load_progress()
    blocks = SCHEDULE.get(date_str, [])
    for bi, block in enumerate(blocks):
        for ti in range(len(block["tasks"])):
            progress[task_key(date_str, bi, ti)] = value
    save_progress(progress)
    return jsonify({"ok": True})


@app.route("/api/settings", methods=["GET", "POST"])
def api_settings():
    if request.method == "POST":
        data = request.get_json() or {}
        settings = load_settings()
        if "notification_minutes_before" in data:
            settings["notification_minutes_before"] = int(data["notification_minutes_before"])
        if "desktop_notifications" in data:
            settings["desktop_notifications"] = bool(data["desktop_notifications"])
        save_settings(settings)
        return jsonify({"ok": True, "settings": settings})
    return jsonify(load_settings())


@app.route("/api/test_notification", methods=["POST"])
def api_test_notification():
    send_linux_notification("Study Todo Test", "Notifications are active and working properly!")
    return jsonify({"ok": True})


# ── killer.sh & Linux Foundation Exam Simulator Routes ─────────
@app.route("/exam/<exam_id>")
def exam_simulator_view(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return f"Mock Exam '{exam_id}' not found. Available: mock-cka-1, mock-cka-2, mock-lfcs-1, mock-lfcs-2, mock-lfcs-3, mock-lfcs-4", 404
    return render_template("exam_simulator.html", exam=meta)


@app.route("/exam/<exam_id>/result")
def exam_result_view(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return f"Mock Exam '{exam_id}' not found. Available: mock-cka-1, mock-cka-2, mock-lfcs-1, mock-lfcs-2, mock-lfcs-3, mock-lfcs-4", 404
    result = get_exam_result(exam_id)
    if not result:
        result = submit_and_grade_exam(exam_id, time_spent_seconds=0)
    return render_template("exam_result.html", exam=meta, result=result)


@app.route("/exam/<exam_id>/solutions")
def exam_solutions_view(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return f"Mock Exam '{exam_id}' not found. Available: mock-cka-1, mock-cka-2, mock-lfcs-1, mock-lfcs-2, mock-lfcs-3, mock-lfcs-4", 404
    result = get_exam_result(exam_id)
    return render_template("exam_solutions.html", exam=meta, result=result)


@app.route("/api/exam/list")
def api_exam_list():
    return jsonify(get_all_mock_exams())


@app.route("/api/exam/<exam_id>")
def api_exam_detail(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return jsonify({"error": f"Exam '{exam_id}' not found"}), 404
    return jsonify(meta)


@app.route("/api/exam/<exam_id>/submit", methods=["POST"])
def api_exam_submit(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return jsonify({"error": f"Exam '{exam_id}' not found"}), 404
    data = request.get_json(silent=True) or {}
    time_spent = data.get("time_spent_seconds", 0)
    report = submit_and_grade_exam(exam_id, time_spent_seconds=time_spent)
    return jsonify({
        "ok": True,
        "redirect_url": f"/exam/{exam_id}/result",
        "report": report
    })


@app.route("/api/exam/<exam_id>/restart", methods=["POST"])
def api_exam_restart(exam_id):
    meta = get_exam_metadata(exam_id)
    if not meta:
        return jsonify({"error": f"Exam '{exam_id}' not found"}), 404
    ok, out = run_exam_action(exam_id, "start")
    return jsonify({
        "ok": ok,
        "redirect_url": f"/exam/{exam_id}?restart=1",
        "output": out
    })


@app.route("/api/exam/<exam_id>/<action>", methods=["POST"])
def api_exam_action(exam_id, action):
    if action not in ["start", "grade", "reset"]:
        return jsonify({"error": f"Invalid action '{action}'. Choose from start, grade, reset"}), 400
    ok, out = run_exam_action(exam_id, action)
    if action == "grade":
        report = parse_grade_output(exam_id, out)
        return jsonify(report)
    return jsonify({"ok": ok, "output": out})


@sock.route("/ws/terminal/<target>")
def terminal_socket(ws, target):
    """
    Spawns an interactive PTY session connected to the target host
    (controlplane or lfcs) via SSH, with bidirectional WebSocket streaming.
    """
    if target in ["controlplane", "node01", "node02", "lfcs"]:
        cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "BatchMode=no", "-t", target]
    else:
        cmd = ["/bin/bash"]

    pid, fd = pty.fork()
    if pid == 0:
        # Slave side: Set initial window dimensions (24 rows, 80 cols) before SSH execvp
        # so SSH negotiates RFC 4254 pty-req with valid non-zero rows/columns.
        try:
            fcntl.ioctl(0, termios.TIOCSWINSZ, struct.pack("HHHH", 24, 80, 0, 0))
        except OSError:
            pass
        os.environ["TERM"] = "xterm-256color"
        os.environ["LANG"] = "C.UTF-8"
        os.environ["LC_ALL"] = "C.UTF-8"
        os.execvp(cmd[0], cmd)

    # Parent process: initialize master fd with 24x80 immediately
    try:
        fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 24, 80, 0, 0))
    except OSError:
        pass

    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    stop_event = threading.Event()
    decoder = codecs.getincrementaldecoder("utf-8")("replace")

    def read_pty_loop():
        while not stop_event.is_set():
            try:
                r, _, _ = select.select([fd], [], [], 0.05)
                if r:
                    chunk = os.read(fd, 4096)
                    if not chunk:
                        break
                    text = decoder.decode(chunk)
                    if text:
                        ws.send(text)
            except (OSError, Exception):
                break
        stop_event.set()

    reader_thread = threading.Thread(target=read_pty_loop, daemon=True)
    reader_thread.start()

    try:
        while not stop_event.is_set():
            msg = ws.receive(timeout=1.0)
            if msg is None:
                continue
            try:
                data_obj = json.loads(msg)
                if data_obj.get("type") == "input":
                    os.write(fd, data_obj["data"].encode("utf-8"))
                elif data_obj.get("type") == "resize":
                    cols = max(10, int(data_obj.get("cols") or 80))
                    rows = max(5, int(data_obj.get("rows") or 24))
                    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))
            except (json.JSONDecodeError, KeyError):
                os.write(fd, msg.encode("utf-8"))
    except Exception:
        pass
    finally:
        stop_event.set()
        try:
            os.close(fd)
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass


if __name__ == "__main__":
    t = threading.Thread(target=notification_daemon, daemon=True)
    t.start()
    port = int(os.environ.get("PORT", 5052))
    print(f"[*] Starting LFCS Webapp & Exam Simulator on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
