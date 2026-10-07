#!/usr/bin/env python3
"""
CKA & LFCS Daily Study Todo — Interactive TUI
Combines the 8-week schedule CSV with curriculum checklist items.
Progress persists in ~/.local/share/study_todo/progress.json

Keys:
  j/Down    Move cursor down          k/Up     Move cursor up
  h/Left    Previous day              l/Right  Next day
  Space     Toggle task done           a        Mark all done
  u         Undo all on current day    t        Jump to today
  g         Jump to first day          G        Jump to last day
  /         Filter CKA only            ?        Filter LFCS only
  0         Show all (clear filter)    q/Esc    Quit
"""

import csv
import curses
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path.home() / ".local" / "share" / "study_todo"
PROGRESS_FILE = DATA_DIR / "progress.json"
TOOLS_DIR = Path(__file__).resolve().parent
BASE_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

SCHEDULE_CSV = BASE_DIR / "cka_lfcs_schedule.csv"
if not SCHEDULE_CSV.exists():
    SCHEDULE_CSV = TOOLS_DIR / "cka_lfcs_schedule.csv"
CURRICULUM_DIR = TOOLS_DIR / "curriculum"

# ── Colour pairs ──────────────────────────────────────────────
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
    curses.init_pair(C_HEADER,   curses.COLOR_CYAN,    -1)
    curses.init_pair(C_CKA,      curses.COLOR_BLUE,    -1)
    curses.init_pair(C_LFCS,     curses.COLOR_MAGENTA, -1)
    curses.init_pair(C_RECOVERY, curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_REST,     curses.COLOR_GREEN,   -1)
    curses.init_pair(C_DONE,     curses.COLOR_GREEN,   -1)
    curses.init_pair(C_PROGRESS, curses.COLOR_CYAN,    -1)
    curses.init_pair(C_SELECTED, curses.COLOR_BLACK,   curses.COLOR_CYAN)
    curses.init_pair(C_DIM,      8, -1)
    curses.init_pair(C_TITLE,    curses.COLOR_WHITE,   curses.COLOR_BLUE)
    curses.init_pair(C_WARN,     curses.COLOR_RED,     -1)
    curses.init_pair(C_CHECK,    curses.COLOR_GREEN,   -1)


# ── Schedule CSV parser ───────────────────────────────────────
def parse_schedule_csv():
    """Return {date_str: [block, ...]} from the CSV."""
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
                    skip_prefixes = ("CKA STUDY BLOCK", "LFCS STUDY BLOCK",
                                     "COGNITIVE RECOVERY")
                    if any(line.startswith(p) for p in skip_prefixes):
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


# ── Curriculum checklist loader ───────────────────────────────
def load_curriculum_checklists():
    """Return {(week, day): [{'track': ..., 'task': ..., 'hint': ...}, ...]}."""
    sys.path.insert(0, str(Path(__file__).parent))
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
                    items = []
                    for item in result.get("checklist", []):
                        if isinstance(item, (list, tuple)) and len(item) >= 2:
                            hint = item[2] if len(item) > 2 else ""
                            items.append({"track": item[0],
                                          "task": item[1], "hint": hint})
                    checklists[(wi, d)] = items
    except Exception as e:
        pass  # Graceful degradation — CSV-only mode
    return checklists


# ── Build complete schedule ───────────────────────────────────
# The CSV only has week 1. We generate the remaining 7 weeks by
# computing dates (Mon-Sat per week, Sun rest) and using curriculum
# checklist data for study content.

START_DATE = datetime(2026, 9, 14)  # Monday Sep 14 2026


def build_full_schedule():
    """Build 48-day + 8-rest-day schedule. Returns (days_dict, sorted_dates)."""
    csv_days = parse_schedule_csv()
    checklists = load_curriculum_checklists()

    # Week topic titles from the curriculum module docstrings
    week_topics = {}
    try:
        from curriculum import WEEKS
        for wi in range(1, 9):
            wmod = WEEKS.get(wi)
            if wmod and wmod.__doc__:
                lines = [l.strip() for l in wmod.__doc__.strip().split("\n")
                         if l.strip() and "Curriculum" not in l]
                for i, line in enumerate(lines):
                    m = re.match(r"Day\s+(\d+):\s*(.*)", line)
                    if m:
                        day_num = int(m.group(1))
                        parts = m.group(2).split("|")
                        cka_topic = parts[0].strip() if parts else "CKA Study"
                        lfcs_topic = parts[1].strip() if len(parts) > 1 else "LFCS Study"
                        week_topics[(wi, day_num)] = (cka_topic, lfcs_topic)
    except Exception:
        pass

    days = {}
    all_dates = []

    # --- Week 1 (Sep 14 - Sep 20, 2026) ---
    week_start = START_DATE
    for day_in_week in range(6):
        dt = week_start + timedelta(days=day_in_week)
        date_str = dt.strftime("%m/%d/%Y")
        all_dates.append(date_str)
        day_num = day_in_week + 1

        if date_str in csv_days:
            days[date_str] = csv_days[date_str]
            cl = checklists.get((1, day_num), [])
            if cl:
                _append_checklist_block(days[date_str], cl, 1, day_num)
        else:
            cka_topic, lfcs_topic = week_topics.get(
                (1, day_num), ("CKA Study", "LFCS Study"))
            days[date_str] = _generate_day_blocks(
                1, day_num, cka_topic, lfcs_topic,
                checklists.get((1, day_num), []))

    rest_dt = week_start + timedelta(days=6)
    rest_str = rest_dt.strftime("%m/%d/%Y")
    all_dates.append(rest_str)
    days[rest_str] = [{
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
        date_str = dt.strftime("%m/%d/%Y")
        all_dates.append(date_str)
        if date_str in csv_days:
            days[date_str] = csv_days[date_str]
        else:
            days[date_str] = [{
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
        for day_in_week in range(6):  # Mon-Sat = 0-5
            dt = week_start + timedelta(days=day_in_week)
            date_str = dt.strftime("%m/%d/%Y")
            all_dates.append(date_str)
            day_num = day_in_week + 1  # 1-6

            if date_str in csv_days:
                days[date_str] = csv_days[date_str]
                cl = checklists.get((week, day_num), [])
                if cl:
                    _append_checklist_block(days[date_str], cl, week, day_num)
            else:
                cka_topic, lfcs_topic = week_topics.get(
                    (week, day_num), ("CKA Study", "LFCS Study"))
                days[date_str] = _generate_day_blocks(
                    week, day_num, cka_topic, lfcs_topic,
                    checklists.get((week, day_num), []))

        # Sunday rest day
        rest_dt = week_start + timedelta(days=6)
        rest_str = rest_dt.strftime("%m/%d/%Y")
        all_dates.append(rest_str)
        days[rest_str] = [{
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


def _generate_day_blocks(week, day, cka_topic, lfcs_topic, checklist):
    """Generate study blocks for a day without CSV data."""
    blocks = []

    # CKA Block
    cka_tasks = [
        "08:00 AM-08:20 AM: Warm-up retrieval practice",
        f"08:20 AM-09:30 AM: Theory: {cka_topic}",
        "09:30 AM-09:45 AM: Physical reset & hydration",
        "09:45 AM-11:15 AM: Hands-on labs & practice",
        "11:15 AM-11:30 AM: Eye rest & micro-break",
        "11:30 AM-12:00 PM: Exploratory practice & notes",
    ]
    blocks.append({
        "type": "CKA",
        "title": f"8am-12pm: {cka_topic}",
        "time": "08:00 AM - 12:00 PM",
        "tasks": cka_tasks,
    })

    # Recovery
    blocks.append({
        "type": "RECOVERY",
        "title": "12pm-3pm: Cognitive Reset & Physical Regeneration",
        "time": "12:00 PM - 03:00 PM",
        "tasks": [
            "12:00 PM-01:00 PM: Nutritious lunch & screen detachment",
            "01:00 PM-02:00 PM: Aerobic exercise / walk (BDNF boost)",
            "02:00 PM-02:45 PM: Power nap or NSDR",
            "02:45 PM-03:00 PM: Terminal & desk prep for LFCS",
        ],
    })

    # LFCS Block
    lfcs_tasks = [
        "03:00 PM-03:20 PM: Warm-up drills",
        f"03:20 PM-04:20 PM: Theory: {lfcs_topic}",
        "04:20 PM-04:35 PM: Movement break",
        "04:35 PM-05:35 PM: Hands-on labs & practice",
        "05:35 PM-06:00 PM: Synthesis & cheat sheet update",
    ]
    blocks.append({
        "type": "LFCS",
        "title": f"3pm-6pm: {lfcs_topic}",
        "time": "03:00 PM - 06:00 PM",
        "tasks": lfcs_tasks,
    })

    # Checklist block
    if checklist:
        _append_checklist_block(blocks, checklist, week, day)

    return blocks


def _append_checklist_block(blocks, checklist, week, day):
    """Append a self-check block with curriculum checklist items."""
    tasks = []
    for item in checklist:
        prefix = f"[{item['track']}]"
        tasks.append(f"{prefix} {item['task']}")
    blocks.append({
        "type": "CKA",  # mixed, but we'll colour per-item
        "title": f"Self-Check: W{week}D{day} Mastery Verification",
        "time": "End of Day",
        "tasks": tasks,
        "is_checklist": True,
    })


# ── Progress persistence ──────────────────────────────────────
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


def task_key(date_str, block_idx, task_idx):
    return f"{date_str}|{block_idx}|{task_idx}"


# ── Day items builder ─────────────────────────────────────────
def build_day_items(date_str, blocks, progress):
    items = []
    for bi, block in enumerate(blocks):
        items.append({
            "kind": "block_header",
            "text": f"  {block['title']}  ({block['time']})",
            "btype": block["type"],
            "done": False,
            "key": None,
            "is_checklist": block.get("is_checklist", False),
        })
        for ti, task in enumerate(block["tasks"]):
            key = task_key(date_str, bi, ti)
            done = progress.get(key, False)
            # Detect track from checklist items
            btype = block["type"]
            if block.get("is_checklist"):
                if task.startswith("[CKA]"):
                    btype = "CKA"
                elif task.startswith("[LFCS]"):
                    btype = "LFCS"
            items.append({
                "kind": "task",
                "text": f"    {task}",
                "btype": btype,
                "done": done,
                "key": key,
            })
    return items


def day_progress(items):
    tasks = [i for i in items if i["kind"] == "task"]
    if not tasks:
        return 0, 0
    return sum(1 for t in tasks if t["done"]), len(tasks)


def overall_progress(days, dates, progress):
    total = done = 0
    for d in dates:
        if d not in days:
            continue
        for bi, block in enumerate(days[d]):
            for ti in range(len(block["tasks"])):
                total += 1
                if progress.get(task_key(d, bi, ti), False):
                    done += 1
    return done, total


# ── Date helpers ──────────────────────────────────────────────
def date_label(date_str, dates):
    try:
        dt = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        return date_str
    idx = dates.index(date_str)
    week = idx // 7 + 1
    day_in_week = idx % 7 + 1
    day_name = dt.strftime("%a")
    formatted = dt.strftime("%b %d, %Y")
    if day_in_week == 7:
        return f"Week {week} REST — {day_name} {formatted}"
    return f"Week {week} Day {day_in_week} — {day_name} {formatted}"


def today_str():
    return datetime.now().strftime("%m/%d/%Y")


def find_today_index(dates):
    t = today_str()
    for i, d in enumerate(dates):
        if d == t:
            return i
    now = datetime.now()
    for i, d in enumerate(dates):
        try:
            dt = datetime.strptime(d, "%m/%d/%Y")
            if dt.date() >= now.date():
                return i
        except ValueError:
            pass
    return 0


# ── Colour helpers ────────────────────────────────────────────
def colour_for_btype(btype):
    return {
        "CKA": C_CKA, "LFCS": C_LFCS, "RECOVERY": C_RECOVERY, "REST": C_REST,
    }.get(btype, C_HEADER)


def draw_bar(win, y, x, width, done, total, pair=C_PROGRESS):
    if total == 0:
        return
    pct = done / total
    filled = int(pct * width)
    bar = "█" * filled + "░" * (width - filled)
    label = f" {done}/{total} ({pct:.0%})"
    colour = C_DONE if pct >= 1.0 else pair
    try:
        win.addstr(y, x, bar, curses.color_pair(pair))
        win.addstr(y, x + width + 1, label, curses.color_pair(colour))
    except curses.error:
        pass


def safe_addstr(win, y, x, text, attr):
    h, w = win.getmaxyx()
    if y < 0 or y >= h or x >= w:
        return
    try:
        win.addstr(y, x, text[:w - x - 1], attr)
    except curses.error:
        pass


# ── Main TUI ──────────────────────────────────────────────────
def main(stdscr):
    curses.curs_set(0)
    init_colours()
    stdscr.timeout(100)

    days, dates = build_full_schedule()
    if not days:
        stdscr.addstr(0, 0, "Error: no schedule data found.")
        stdscr.getch()
        return

    progress = load_progress()
    day_idx = find_today_index(dates)
    cursor = 0
    scroll_offset = 0
    dirty = False
    track_filter = None  # None = all, "CKA", "LFCS"

    while True:
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        if h < 10 or w < 40:
            stdscr.addstr(0, 0, "Terminal too small")
            stdscr.refresh()
            stdscr.getch()
            continue

        date_str = dates[day_idx]
        blocks = days.get(date_str, [])
        all_items = build_day_items(date_str, blocks, progress)

        # Apply filter
        if track_filter:
            items = []
            skip_header = True
            for item in all_items:
                if item["kind"] == "block_header":
                    # Include header if its type matches or it's a checklist header
                    if item["btype"] == track_filter or item.get("is_checklist"):
                        items.append(item)
                        skip_header = False
                    else:
                        skip_header = True
                else:
                    if not skip_header and (item["btype"] == track_filter
                                            or item["btype"] == "RECOVERY"
                                            or item["btype"] == "REST"):
                        items.append(item)
                    elif item["btype"] == track_filter:
                        items.append(item)
        else:
            items = all_items

        done_count, total_count = day_progress(all_items)
        o_done, o_total = overall_progress(days, dates, progress)

        # ── Title bar
        filter_label = f" [{track_filter}]" if track_filter else ""
        title = f" CKA & LFCS Study Todo{filter_label} "
        safe_addstr(stdscr, 0, 0, " " * w,
                    curses.color_pair(C_TITLE))
        safe_addstr(stdscr, 0, max(0, (w - len(title)) // 2), title,
                    curses.color_pair(C_TITLE) | curses.A_BOLD)

        # ── Day header
        label = date_label(date_str, dates)
        is_today = (date_str == today_str())
        day_marker = " (TODAY)" if is_today else ""
        nav = f"  [{day_idx + 1}/{len(dates)}]"
        safe_addstr(stdscr, 2, 2, label + day_marker + nav,
                    curses.color_pair(C_HEADER) | curses.A_BOLD)

        # ── Progress bars
        bar_w = min(30, w - 20)
        draw_bar(stdscr, 3, 2, bar_w, done_count, total_count)

        overall_label = f"Overall: {o_done}/{o_total}"
        if o_total:
            overall_label += f" ({o_done/o_total:.0%})"
        safe_addstr(stdscr, 3, max(2, w - len(overall_label) - 2),
                    overall_label, curses.color_pair(C_DIM))

        # ── Weeks overview line (compact)
        weeks_line = ""
        for wk in range(1, 9):
            wk_done = wk_total = 0
            for di in range(7):
                idx = (wk - 1) * 7 + di
                if idx < len(dates):
                    d = dates[idx]
                    if d in days:
                        for bi, block in enumerate(days[d]):
                            for ti in range(len(block["tasks"])):
                                wk_total += 1
                                if progress.get(task_key(d, bi, ti), False):
                                    wk_done += 1
            if wk_total > 0:
                pct = wk_done / wk_total
                marker = "●" if pct >= 1.0 else ("◐" if pct > 0 else "○")
            else:
                marker = "○"
            weeks_line += f" W{wk}{marker}"
        safe_addstr(stdscr, 4, 2, weeks_line, curses.color_pair(C_DIM))

        # ── Items list
        list_start = 6
        list_height = h - list_start - 3

        selectable = [i for i, it in enumerate(items) if it["kind"] == "task"]
        if not selectable:
            cursor = -1
        else:
            cursor = max(0, min(cursor, len(selectable) - 1))

        sel_item_idx = selectable[cursor] if cursor >= 0 and selectable else -1

        if sel_item_idx >= 0:
            if sel_item_idx - scroll_offset >= list_height:
                scroll_offset = sel_item_idx - list_height + 1
            if sel_item_idx < scroll_offset:
                scroll_offset = sel_item_idx
        scroll_offset = max(0, scroll_offset)

        for vi in range(list_height):
            ii = vi + scroll_offset
            if ii >= len(items):
                break
            item = items[ii]
            y = list_start + vi

            if item["kind"] == "block_header":
                attr = curses.color_pair(colour_for_btype(item["btype"])) | curses.A_BOLD
                safe_addstr(stdscr, y, 0, item["text"], attr)
            else:
                is_sel = (ii == sel_item_idx)
                checkbox = "[x]" if item["done"] else "[ ]"
                if is_sel:
                    attr = curses.color_pair(C_SELECTED) | curses.A_BOLD
                    line = f" > {checkbox} {item['text']}"
                elif item["done"]:
                    attr = curses.color_pair(C_DONE)
                    line = f"   {checkbox} {item['text']}"
                else:
                    attr = curses.color_pair(colour_for_btype(item["btype"]))
                    line = f"   {checkbox} {item['text']}"
                safe_addstr(stdscr, y, 0, line, attr)

        # ── Key bar
        keys = " j/k Up/Down  h/l Prev/Next Day  Space Toggle  a All  u Undo  t Today  / CKA  ? LFCS  0 All  q Quit "
        safe_addstr(stdscr, h - 2, 0, " " * w, curses.color_pair(C_TITLE))
        safe_addstr(stdscr, h - 2, max(0, (w - len(keys)) // 2), keys,
                    curses.color_pair(C_TITLE))

        stdscr.refresh()

        # ── Input
        ch = stdscr.getch()
        if ch == -1:
            continue

        if ch in (ord("q"), ord("Q"), 27):
            if dirty:
                save_progress(progress)
            break

        elif ch in (ord("j"), curses.KEY_DOWN):
            if selectable and cursor < len(selectable) - 1:
                cursor += 1

        elif ch in (ord("k"), curses.KEY_UP):
            if selectable and cursor > 0:
                cursor -= 1

        elif ch in (ord("l"), curses.KEY_RIGHT):
            if day_idx < len(dates) - 1:
                if dirty:
                    save_progress(progress)
                    dirty = False
                day_idx += 1
                cursor = 0
                scroll_offset = 0

        elif ch in (ord("h"), curses.KEY_LEFT):
            if day_idx > 0:
                if dirty:
                    save_progress(progress)
                    dirty = False
                day_idx -= 1
                cursor = 0
                scroll_offset = 0

        elif ch == ord(" ") or ch == 10:
            if selectable and 0 <= cursor < len(selectable):
                idx = selectable[cursor]
                key = items[idx]["key"]
                if key:
                    new_val = not items[idx]["done"]
                    items[idx]["done"] = new_val
                    progress[key] = new_val
                    dirty = True

        elif ch in (ord("a"), ord("A")):
            for item in all_items:
                if item["kind"] == "task" and item["key"]:
                    item["done"] = True
                    progress[item["key"]] = True
            dirty = True

        elif ch in (ord("u"), ord("U")):
            for item in all_items:
                if item["kind"] == "task" and item["key"]:
                    item["done"] = False
                    progress[item["key"]] = False
            dirty = True

        elif ch in (ord("t"), ord("T")):
            if dirty:
                save_progress(progress)
                dirty = False
            day_idx = find_today_index(dates)
            cursor = 0
            scroll_offset = 0

        elif ch == ord("g"):
            if dirty:
                save_progress(progress)
                dirty = False
            day_idx = 0
            cursor = 0
            scroll_offset = 0

        elif ch == ord("G"):
            if dirty:
                save_progress(progress)
                dirty = False
            day_idx = len(dates) - 1
            cursor = 0
            scroll_offset = 0

        elif ch == ord("/"):
            track_filter = "CKA"
            cursor = 0
            scroll_offset = 0

        elif ch == ord("?"):
            track_filter = "LFCS"
            cursor = 0
            scroll_offset = 0

        elif ch == ord("0"):
            track_filter = None
            cursor = 0
            scroll_offset = 0

    save_progress(progress)


if __name__ == "__main__":
    curses.wrapper(main)
