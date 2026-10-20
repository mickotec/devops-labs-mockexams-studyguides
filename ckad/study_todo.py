#!/usr/bin/env python3
"""
CKAD Daily Study Todo — Interactive TUI (Kubernetes Developer Track)
Provides an interactive terminal checklist dedicated exclusively to the CKAD curriculum.
Progress persists in ~/.local/share/study_todo/ckad_progress.json

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
if str(DIR) not in sys.path:
    sys.path.insert(0, str(DIR))
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

DATA_DIR = Path.home() / ".local" / "share" / "study_todo"
PROGRESS_FILE = DATA_DIR / "ckad_progress.json"

SCHEDULE_CSV = DIR / "schedule.csv"
if not SCHEDULE_CSV.exists():
    SCHEDULE_CSV = DIR / "schedule.template.csv"

C_HEADER   = 1
C_CKAD     = 2
C_RECOVERY = 3
C_REST     = 4
C_DONE     = 5
C_PROGRESS = 6
C_SELECTED = 7
C_DIM      = 8
C_TITLE    = 9
C_WARN     = 10
C_CHECK    = 11

def init_colours():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(C_HEADER,   curses.COLOR_GREEN,   -1)
    curses.init_pair(C_CKAD,     curses.COLOR_CYAN,    -1)
    curses.init_pair(C_RECOVERY, curses.COLOR_MAGENTA, -1)
    curses.init_pair(C_REST,     curses.COLOR_WHITE,   -1)
    curses.init_pair(C_DONE,     curses.COLOR_GREEN,   -1)
    curses.init_pair(C_PROGRESS, curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_SELECTED, curses.COLOR_BLACK,   curses.COLOR_GREEN)
    curses.init_pair(C_DIM,      curses.COLOR_BLACK,   -1)
    curses.init_pair(C_TITLE,    curses.COLOR_WHITE,   -1)
    curses.init_pair(C_WARN,     curses.COLOR_RED,     -1)
    curses.init_pair(C_CHECK,    curses.COLOR_GREEN,   -1)

def load_progress():
    if not PROGRESS_FILE.exists():
        return {}
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_progress(progress):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

def load_schedule_days():
    if not SCHEDULE_CSV.exists():
        return []
    days = []
    with open(SCHEDULE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            days.append({
                "date": row.get("Start Date", ""),
                "subject": row.get("Subject", ""),
                "desc": row.get("Description", "")
            })
    return days

def main(stdscr):
    curses.curs_set(0)
    init_colours()
    days = load_schedule_days()
    if not days:
        stdscr.addstr(0, 0, "No schedule found in schedule.csv or schedule.template.csv.")
        stdscr.refresh()
        stdscr.getch()
        return

    progress = load_progress()
    day_idx = 0
    task_idx = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        cur_day = days[day_idx]
        d_str = cur_day["date"]
        subj = cur_day["subject"]
        desc = cur_day["desc"]

        tasks = [line.strip() for line in desc.split("\n") if line.strip() and not line.startswith("CKAD STUDY BLOCK")]
        
        # Header
        header = f" CKAD STUDY PLANNER — DAY {day_idx + 1}/{len(days)} ({d_str}) "
        stdscr.attron(curses.color_pair(C_HEADER) | curses.A_BOLD)
        stdscr.addstr(0, max(0, (w - len(header)) // 2), header[:w])
        stdscr.attroff(curses.color_pair(C_HEADER) | curses.A_BOLD)

        # Subject
        stdscr.attron(curses.color_pair(C_CKAD) | curses.A_BOLD)
        stdscr.addstr(2, 2, f"Topic: {subj[:w-10]}")
        stdscr.attroff(curses.color_pair(C_CKAD) | curses.A_BOLD)

        # Tasks list
        stdscr.addstr(4, 2, "Daily Schedule & Tasks:", curses.A_UNDERLINE)
        
        day_prog = progress.get(d_str, {})
        for idx, t in enumerate(tasks):
            y = 6 + idx
            if y >= h - 3:
                break
            is_done = day_prog.get(str(idx), False)
            box = "[✓]" if is_done else "[ ]"
            color = curses.color_pair(C_DONE) if is_done else curses.color_pair(C_TITLE)
            
            if idx == task_idx:
                stdscr.attron(curses.color_pair(C_SELECTED) | curses.A_BOLD)
                stdscr.addstr(y, 2, f" {box} {t[:w-10]} ".ljust(w - 4))
                stdscr.attroff(curses.color_pair(C_SELECTED) | curses.A_BOLD)
            else:
                stdscr.attron(color)
                stdscr.addstr(y, 4, f"{box} {t[:w-10]}")
                stdscr.attroff(color)

        # Footer
        footer = " [Space] Toggle | [h/l] Prev/Next Day | [j/k] Select Task | [a] All Done | [q] Quit "
        stdscr.attron(curses.color_pair(C_DIM))
        stdscr.addstr(h - 1, max(0, (w - len(footer)) // 2), footer[:w])
        stdscr.attroff(curses.color_pair(C_DIM))

        stdscr.refresh()
        key = stdscr.getch()

        if key in (ord('q'), 27):
            break
        elif key in (curses.KEY_DOWN, ord('j')):
            if task_idx < len(tasks) - 1:
                task_idx += 1
        elif key in (curses.KEY_UP, ord('k')):
            if task_idx > 0:
                task_idx -= 1
        elif key in (curses.KEY_RIGHT, ord('l')):
            if day_idx < len(days) - 1:
                day_idx += 1
                task_idx = 0
        elif key in (curses.KEY_LEFT, ord('h')):
            if day_idx > 0:
                day_idx -= 1
                task_idx = 0
        elif key == ord(' '):
            if d_str not in progress:
                progress[d_str] = {}
            progress[d_str][str(task_idx)] = not progress[d_str].get(str(task_idx), False)
            save_progress(progress)
        elif key == ord('a'):
            if d_str not in progress:
                progress[d_str] = {}
            for i in range(len(tasks)):
                progress[d_str][str(i)] = True
            save_progress(progress)
        elif key == ord('u'):
            if d_str in progress:
                progress[d_str] = {}
                save_progress(progress)

if __name__ == "__main__":
    curses.wrapper(main)
