#!/usr/bin/env python3
"""
CKA Dedicated Study Calendar Generator
Customizes the CKA preparation calendar based on:
 1. When the learner starts studying (Start Date)
 2. Study duration / pacing (8-Week Standard, 4-Week Sprint, or Custom)
 3. Optional pause / recovery weeks

Outputs: cka/schedule.ics and cka/schedule.csv
"""

import sys
import argparse
from pathlib import Path

DIR = Path(__file__).resolve().parent
REPO_ROOT = DIR.parent
TOOLS_DIR = REPO_ROOT / "tools"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.generate_calendar import (
    prompt_user_inputs,
    resolve_start_date,
    resolve_duration,
    resolve_pause_weeks,
    parse_time_window,
    run_generator
)

def main():
    parser = argparse.ArgumentParser(description="CKA Dedicated Study Calendar Generator")
    parser.add_argument("-s", "--start", "--start-date", dest="start_date", help="Start date (YYYY-MM-DD, 'today', 'tomorrow', 'next monday')")
    parser.add_argument("-w", "--weeks", "--duration", dest="duration_weeks", type=str, help="Duration in weeks (8 or 4)")
    parser.add_argument("-p", "--pause", dest="pauses", default="", help="Scheduled pause weeks, comma-separated (e.g. '2')")
    parser.add_argument("-t", "--time", "--study-time", "--cka-time", dest="time_window", default="", help="Preferred daily study hours (e.g. '4am to 12pm')")
    parser.add_argument("-i", "--interactive", action="store_true", help="Force interactive prompt")
    parser.add_argument("-y", "--yes", "--non-interactive", dest="non_interactive", action="store_true", help="Non-interactive batch mode")

    args = parser.parse_args()

    is_interactive = (sys.stdin.isatty() and not args.non_interactive and not (args.start_date and args.duration_weeks)) or args.interactive

    if is_interactive:
        start_date, duration_weeks, _, pauses, cka_time, _ = prompt_user_inputs(default_track="cka")
    else:
        start_date = resolve_start_date(args.start_date or "")
        duration_weeks = resolve_duration(args.duration_weeks or "8")
        pauses = resolve_pause_weeks(args.pauses or "")
        cka_time = parse_time_window(args.time_window or "", "08:00 AM", "12:00 PM")

    run_generator(start_date, duration_weeks, track="cka", pauses=pauses, output_dir=REPO_ROOT, cka_time=cka_time)

if __name__ == "__main__":
    main()
