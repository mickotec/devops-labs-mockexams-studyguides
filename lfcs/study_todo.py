#!/usr/bin/env python3
"""
LFCS Daily Study Todo — Interactive TUI (Linux Foundation Track)
Provides an interactive terminal checklist dedicated exclusively to the LFCS curriculum.
Progress persists in ~/.local/share/study_todo/lfcs_progress.json

Keys:
  j/Down    Move cursor down          k/Up     Move cursor up
  h/Left    Previous day              l/Right  Next day
  Space     Toggle task done           a        Mark all done
  u         Undo all on current day    t        Jump to today
  g         Jump to first day          G        Jump to last day
  q/Esc     Quit
"""

import csv
import curses
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

DIR = Path(__file__).resolve().parent
REPO_DIR = DIR.parent
TOOLS_DIR = REPO_DIR / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

DATA_DIR = Path.home() / ".local" / "share" / "study_todo"
PROGRESS_FILE = DATA_DIR / "lfcs_progress.json"

SCHEDULE_CSV = DIR / "schedule.csv"
if not SCHEDULE_CSV.exists():
    SCHEDULE_CSV = DIR / "schedule.template.csv"
CURRICULUM_DIR = TOOLS_DIR / "curriculum"

C_HEADER   = 1
C_CKA      = 2
C_LFCS     = 3
C_RECOVERY = 4
C_REST     = 5
C_DONE     = 6
C_PROGRESS = 7
C_SELECTED = 8
C_DIM      = 9
C_TITLE    = 10
C_WARN     = 11
C_CHECK    = 12

def init_colours():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(C_HEADER,   curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_CKA,      curses.COLOR_BLUE,    -1)
    curses.init_pair(C_LFCS,     curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_RECOVERY, curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_REST,     curses.COLOR_GREEN,   -1)
    curses.init_pair(C_DONE,     curses.COLOR_GREEN,   -1)
    curses.init_pair(C_PROGRESS, curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_SELECTED, curses.COLOR_BLACK,   curses.COLOR_YELLOW)
    curses.init_pair(C_DIM,      8, -1)
    curses.init_pair(C_TITLE,    curses.COLOR_BLACK,   curses.COLOR_YELLOW)
    curses.init_pair(C_WARN,     curses.COLOR_RED,     -1)
    curses.init_pair(C_CHECK,    curses.COLOR_GREEN,   -1)

def parse_schedule_csv():
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
                continue
            if "[LFCS]" in subject:
                btype = "LFCS"
            elif "[RECOVERY]" in subject:
                btype = "RECOVERY"
            elif "[REST]" in subject:
                btype = "REST"
            else:
                btype = "OTHER"
            title = subject
            for tag in ["[LFCS]", "[RECOVERY]", "[REST]", "[PAUSE]"]:
                title = title.replace(tag, "").strip()
            tasks = []
            if desc:
                for line in desc.split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    if any(line.startswith(p) for p in ("LFCS STUDY BLOCK", "COGNITIVE RECOVERY")):
                        continue
                    m = re.match(r"(\d{2}:\d{2}\s*[AP]M)\s*-\s*(\d{2}:\d{2}\s*[AP]M):\s*(.*)", line)
                    if m:
                        tasks.append(f"{m.group(1)}-{m.group(2)}: {m.group(3)}")
                    else:
                        tasks.append(line)
            block = {"type": btype, "title": title, "time": f"{start_time} - {end_time}", "tasks": tasks}
            days.setdefault(date_str, []).append(block)
    return days

def load_curriculum_checklists():
    checklists = {}
    try:
        from curriculum import WEEKS
        for wi in range(1, 9):
            wmod = WEEKS.get(wi)
            if not wmod:
                continue
            for d in range(1, 7):
                fn = f"get_day_{d}"
                if hasattr(wmod, fn):
                    result = getattr(wmod, fn)()
                    items = [
                        {"track": c[0], "task": c[1], "hint": c[2] if len(c) > 2 else ""}
                        for c in result.get("checklist", []) if c[0] == "LFCS"
                    ]
                    checklists[(wi, d)] = items
    except Exception:
        pass
    return checklists

def build_study_days(schedule_days):
    checklists = load_curriculum_checklists()
    week_topics = {}
    try:
        from curriculum import WEEKS
        for wi in range(1, 9):
            wmod = WEEKS.get(wi)
            if wmod and wmod.__doc__:
                for line in wmod.__doc__.strip().split("\n"):
                    m = re.match(r"Day\s+(\d+):\s*(.*)", line.strip())
                    if m:
                        dn = int(m.group(1))
                        parts = m.group(2).split("|")
                        lfcs_topic = parts[1].strip() if len(parts) > 1 else parts[0].strip()
                        week_topics[(wi, dn)] = lfcs_topic
    except Exception:
        pass

    calendar_days = []
    seen = set()
    start_dt = datetime(2026, 9, 14)
    cal_day = 0
    while len(calendar_days) < 56:
        dt = start_dt + timedelta(days=cal_day)
        cal_day += 1
        d_str = dt.strftime("%m/%d/%Y")
        if d_str in seen:
            continue
        seen.add(d_str)
        wk = ((cal_day - 1) // 7) + 1
        dow = dt.weekday()
        day_of_study = dow + 1 if dow < 6 else 0
        calendar_days.append({
            "date_str": d_str,
            "dt": dt,
            "week": wk,
            "day_of_study": day_of_study,
            "is_sunday": dow == 6,
            "blocks": schedule_days.get(d_str, []),
            "checklist": checklists.get((wk, day_of_study), []) if day_of_study > 0 else [],
            "topic": week_topics.get((wk, day_of_study), "") if day_of_study > 0 else ""
        })
    return calendar_days

def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except Exception:
            pass
    return {}

def save_progress(progress):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))

def build_task_list(day_data):
    tasks = []
    d_str = day_data["date_str"]
    for bi, block in enumerate(day_data["blocks"]):
        for ti, task_text in enumerate(block["tasks"]):
            tid = f"{d_str}_b{bi}_t{ti}"
            tasks.append({
                "id": tid, "type": "schedule", "track": block["type"],
                "section": f"{block['type']} ({block['time']}): {block['title']}",
                "text": task_text, "hint": ""
            })
    for ci, chk in enumerate(day_data["checklist"]):
        tid = f"{d_str}_chk_{ci}"
        tasks.append({
            "id": tid, "type": "checklist", "track": chk["track"],
            "section": "LFCS Self-Assessment Checklist",
            "text": chk["task"], "hint": chk.get("hint", "")
        })
    return tasks

def render_screen(stdscr, days, day_idx, cursor, scroll_offset, progress):
    stdscr.erase()
    max_y, max_x = stdscr.getmaxyx()
    if max_y < 12 or max_x < 50:
        stdscr.addstr(0, 0, "Terminal too small.", curses.A_BOLD)
        stdscr.refresh()
        return scroll_offset

    curr = days[day_idx]
    all_tasks = build_task_list(curr)
    done_count = sum(1, bool(progress.get(t["id"]))) if all_tasks else 0
    pct = int(done_count * 100 / len(all_tasks)) if all_tasks else 0

    title_str = " 🐧 LFCS MASTER STUDY TODO — LINUX FOUNDATION TRACK "
    stdscr.attron(curses.color_pair(C_TITLE) | curses.A_BOLD)
    stdscr.addstr(0, 0, title_str.center(max_x)[:max_x - 1])
    stdscr.attroff(curses.color_pair(C_TITLE) | curses.A_BOLD)

    header_line = f" Week {curr['week']} Day {curr['day_of_study']} | {curr['dt'].strftime('%A, %b %d, %Y')} | [{done_count}/{len(all_tasks)} Done - {pct}%] "
    stdscr.attron(curses.color_pair(C_HEADER) | curses.A_BOLD)
    stdscr.addstr(1, 0, header_line[:max_x - 1])
    stdscr.attroff(curses.color_pair(C_HEADER) | curses.A_BOLD)

    if curr.get("topic"):
        stdscr.addstr(2, 2, f"Topic: {curr['topic']}"[:max_x - 4], curses.color_pair(C_LFCS))

    list_start_y = 4
    list_h = max_y - list_start_y - 3
    if cursor < scroll_offset:
        scroll_offset = cursor
    if cursor >= scroll_offset + list_h:
        scroll_offset = cursor - list_h + 1

    row = list_start_y
    for idx in range(scroll_offset, min(len(all_tasks), scroll_offset + list_h)):
        t = all_tasks[idx]
        is_done = progress.get(t["id"], False)
        is_sel = (idx == cursor)
        mark = "[✓]" if is_done else "[ ]"
        line = f" {mark} {t['text']}"
        if t["hint"]:
            line += f" -> {t['hint']}"
        line = line[:max_x - 2]

        attr = curses.color_pair(C_SELECTED) | curses.A_BOLD if is_sel else (curses.color_pair(C_DONE) if is_done else curses.color_pair(C_LFCS))
        stdscr.addstr(row, 0, line, attr)
        row += 1

    footer = " [j/k] Navigate  [Space] Toggle  [h/l] Day  [t] Today  [a] Mark All  [u] Undo  [q] Quit"
    stdscr.attron(curses.color_pair(C_DIM))
    stdscr.addstr(max_y - 1, 0, footer[:max_x - 1])
    stdscr.attroff(curses.color_pair(C_DIM))
    stdscr.refresh()
    return scroll_offset

def main(stdscr):
    init_colours()
    curses.curs_set(0)
    stdscr.keypad(True)

    sched = parse_schedule_csv()
    days = build_study_days(sched)
    progress = load_progress()

    day_idx = 0
    today_str = datetime.now().strftime("%m/%d/%Y")
    for i, d in enumerate(days):
        if d["date_str"] == today_str:
            day_idx = i
            break

    cursor = 0
    scroll_offset = 0

    while True:
        scroll_offset = render_screen(stdscr, days, day_idx, cursor, scroll_offset, progress)
        ch = stdscr.getch()

        if ch in (ord("q"), 27):
            break
        elif ch in (curses.KEY_UP, ord("k")):
            if cursor > 0: cursor -= 1
        elif ch in (curses.KEY_DOWN, ord("j")):
            tasks = build_task_list(days[day_idx])
            if cursor < len(tasks) - 1: cursor += 1
        elif ch in (curses.KEY_LEFT, ord("h")):
            if day_idx > 0:
                day_idx -= 1
                cursor = 0
                scroll_offset = 0
        elif ch in (curses.KEY_RIGHT, ord("l")):
            if day_idx < len(days) - 1:
                day_idx += 1
                cursor = 0
                scroll_offset = 0
        elif ch == ord(" "):
            tasks = build_task_list(days[day_idx])
            if tasks and cursor < len(tasks):
                tid = tasks[cursor]["id"]
                progress[tid] = not progress.get(tid, False)
                save_progress(progress)
        elif ch == ord("a"):
            tasks = build_task_list(days[day_idx])
            for t in tasks:
                progress[t["id"]] = True
            save_progress(progress)
        elif ch == ord("u"):
            tasks = build_task_list(days[day_idx])
            for t in tasks:
                progress[t["id"]] = False
            save_progress(progress)
        elif ch == ord("t"):
            for i, d in enumerate(days):
                if d["date_str"] == today_str:
                    day_idx = i
                    cursor = 0
                    scroll_offset = 0
                    break

if __name__ == "__main__":
    curses.wrapper(main)
