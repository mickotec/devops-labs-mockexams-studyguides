#!/usr/bin/env python3
"""
CKA Master Daily Study Guide Generator
Dedicated generator for the Certified Kubernetes Administrator (CKA) track.
Outputs: cka/guides/CKA_Daily_Study_Guide_W{w}D{d}.html
"""

import os
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
REPO_DIR = DIR.parent
TOOLS_DIR = REPO_DIR / "tools"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

from tools.generate_daily_guide import (
    parse_ics_schedule,
    generate_single_day,
    generate_day_worker,
    START_DATE
)
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
import re

ICS_PATH = DIR / "schedule.ics"
if not ICS_PATH.exists():
    ICS_PATH = REPO_DIR / "cka_lfcs_schedule.ics"

def main():
    schedule = parse_ics_schedule(ICS_PATH)
    args = sys.argv[1:]

    if not args:
        print("[*] Generating default Day 1 (W1D1) CKA Study Guide...")
        generate_single_day(1, 1, schedule, track="cka")
        return

    first_arg = args[0].lower().strip("-")

    if first_arg in ["all"]:
        print("[*] Batch generating all 48 CKA Daily Study Guides...")
        tasks = []
        for w in range(1, 9):
            for d in range(1, 7):
                tasks.append((w, d, schedule, "cka"))

        start_t = datetime.now()
        completed = 0
        with ProcessPoolExecutor(max_workers=4) as executor:
            future_to_day = {executor.submit(generate_day_worker, t): (t[0], t[1]) for t in tasks}
            for future in as_completed(future_to_day):
                w, d = future_to_day[future]
                try:
                    res = future.result()
                    completed += 1
                    names = ", ".join(f.name for f in res)
                    print(f"[{completed:02d}/48] [✓] Week {w} Day {d} -> {names}")
                except Exception as e:
                    print(f"[-] Error on Week {w} Day {d}: {e}", file=sys.stderr)

        elapsed = (datetime.now() - start_t).total_seconds()
        print(f"\n[★] Batch generation complete in {elapsed:.1f}s!")
        print(f"    CKA Guides saved to: {DIR / 'guides'}")
        return

    if first_arg in ["week", "w"] and len(args) > 1:
        wk = int(args[1])
        print(f"[*] Generating Week {wk} CKA Study Guides...")
        for d in range(1, 7):
            generate_single_day(wk, d, schedule, track="cka")
        return

    m = re.match(r"^w([1-8])d([1-6])$", first_arg)
    if m:
        wk = int(m.group(1))
        dy = int(m.group(2))
        generate_single_day(wk, dy, schedule, track="cka")
        return

    print(f"[-] Unrecognized option: {' '.join(args)}")
    print("Usage:")
    print("  python3 generate_guides.py w1d1        # Generate W1D1 CKA guide")
    print("  python3 generate_guides.py --week 1    # Generate Week 1 CKA guides")
    print("  python3 generate_guides.py --all       # Generate all 48 CKA guides")

if __name__ == "__main__":
    main()
