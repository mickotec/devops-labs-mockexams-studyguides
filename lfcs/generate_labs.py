#!/usr/bin/env python3
"""
LFCS Master Lab & Mock Exam Generator
Generates all 48 hands-on LFCS daily practice labs and 4 full-scale mock exams
directly into the lfcs/ directory.
"""

import os
import sys
import stat
from pathlib import Path

DIR = Path(__file__).resolve().parent
REPO_DIR = DIR.parent
TOOLS_DIR = REPO_DIR / "tools"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

from curriculum.labs_week1 import WEEK_1_LABS
from curriculum.labs_week2 import WEEK_2_LABS
from curriculum.labs_week3 import WEEK_3_LABS
from curriculum.labs_week4 import WEEK_4_LABS
from curriculum.labs_week5 import WEEK_5_LABS
from curriculum.labs_week6 import WEEK_6_LABS
from curriculum.labs_week7 import WEEK_7_LABS
from curriculum.labs_week8 import WEEK_8_LABS
from curriculum.labs_mocks import MOCK_LABS

ALL_WEEKS = [
    (1, WEEK_1_LABS),
    (2, WEEK_2_LABS),
    (3, WEEK_3_LABS),
    (4, WEEK_4_LABS),
    (5, WEEK_5_LABS),
    (6, WEEK_6_LABS),
    (7, WEEK_7_LABS),
    (8, WEEK_8_LABS),
]
LFCS_MOCKS = [m for m in MOCK_LABS if m.get("track", "").upper() == "LFCS"]

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

def write_lab(lab_id, date_str, title, diff, time_limit, tasks, setup_code, verify_code, solution_code, reset_code):
    lab_dir = DIR / lab_id
    lab_dir.mkdir(parents=True, exist_ok=True)

    pass_score = "67%" if lab_id.startswith("mock-") else "100%"
    target_str = "VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal"

    (lab_dir / "meta.env").write_text(f"""TRACK="LFCS"
DATE="{date_str}"
TITLE="{title}"
DIFFICULTY="{diff}"
TIME_LIMIT="{time_limit}"
PASSING_SCORE="{pass_score}"
""", encoding="utf-8")

    pass_line = f"\n**Passing Score:** {pass_score}  " if lab_id.startswith("mock-") else ""
    (lab_dir / "scenario.md").write_text(f"""# [LFCS {lab_id.upper()}] {title}

**Date:** {date_str}  
**Time Limit:** {time_limit}  {pass_line}
**Difficulty:** {diff}  
**Target:** {target_str}  

---

## 📋 Scenario Overview
Practice scenario aligned with your official LFCS preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

{tasks}

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check {lab_id}
```
""", encoding="utf-8")

    (lab_dir / "solution.md").write_text(f"""# [LFCS {lab_id.upper()}] Solution Walkthrough: {title}

{solution_code}
""", encoding="utf-8")

    setup_file = lab_dir / "setup.sh"
    setup_file.write_text(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up {lab_id} ({title})..."
{setup_code}
echo "[✓] Environment ready. Review tasks with: ./lab show {lab_id}"
""", encoding="utf-8")
    make_executable(setup_file)

    verify_file = lab_dir / "verify.sh"
    if lab_id.startswith("mock-"):
        score_block = f"""
PCT_OPS=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_OPS * 25.0 / $TOTAL_OPS}}")
PCT_NET=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_NET * 25.0 / $TOTAL_NET}}")
PCT_STOR=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_STOR * 20.0 / $TOTAL_STOR}}")
PCT_CMD=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_CMD * 20.0 / $TOTAL_CMD}}")
PCT_USER=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_USER * 10.0 / $TOTAL_USER}}")

TOTAL_PCT=$(awk "BEGIN {{printf \\"%.1f\\", ($SCORE_OPS * 25.0 / $TOTAL_OPS) + ($SCORE_NET * 25.0 / $TOTAL_NET) + ($SCORE_STOR * 20.0 / $TOTAL_STOR) + ($SCORE_CMD * 20.0 / $TOTAL_CMD) + ($SCORE_USER * 10.0 / $TOTAL_USER)}}")

echo ""
echo "────────────────────────────────────────────────────────────"
echo -e "${{BOLD}}Linux Foundation Domain Weight Breakdown (LFCS):${{NC}}"
echo -e "  • Operations Deployment (25%):                       ${{SCORE_OPS}}/${{TOTAL_OPS}} passed   (${{PCT_OPS}}% / 25.0%)"
echo -e "  • Networking (25%):                                  ${{SCORE_NET}}/${{TOTAL_NET}} passed   (${{PCT_NET}}% / 25.0%)"
echo -e "  • Storage (20%):                                     ${{SCORE_STOR}}/${{TOTAL_STOR}} passed   (${{PCT_STOR}}% / 20.0%)"
echo -e "  • Essential Commands (20%):                          ${{SCORE_CMD}}/${{TOTAL_CMD}} passed   (${{PCT_CMD}}% / 20.0%)"
echo -e "  • Users and Groups (10%):                            ${{SCORE_USER}}/${{TOTAL_USER}} passed   (${{PCT_USER}}% / 10.0%)"
echo "────────────────────────────────────────────────────────────"
echo -e "Questions Passed:     ${{BOLD}}${{TOTAL_PASSED}} / ${{TOTAL_QUESTIONS}}${{NC}}"
echo -e "Final Weighted Score: ${{BOLD}}${{TOTAL_PCT}}%${{NC}}"
echo -e "Passing Threshold:    67.0%"
echo "────────────────────────────────────────────────────────────"

IS_PASS=$(awk "BEGIN {{if ($TOTAL_PCT >= 67.0) print 1; else print 0}}")
if [ "$IS_PASS" -eq 1 ]; then
  echo -e "${{GREEN}}${{BOLD}}CONGRATULATIONS! Mock Exam {lab_id} completed successfully! (${{TOTAL_PCT}}% >= 67.0%)${{NC}}"
  exit 0
else
  echo -e "${{RED}}Score below passing threshold (67.0%). Current: ${{TOTAL_PCT}}%. Review domain competencies or run: ./lab solve {lab_id}${{NC}}"
  exit 1
fi"""
    else:
        score_block = f"""echo "──────────────────────────────────────────────"
echo -e "Final Score: ${{BOLD}}${{SCORE}}/${{TOTAL}}${{NC}}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${{GREEN}}${{BOLD}}CONGRATULATIONS! Lab {lab_id} completed successfully!${{NC}}"
  exit 0
else
  echo -e "${{RED}}Checks incomplete. Review scenario tasks or run: ./lab solve {lab_id}${{NC}}"
  exit 1
fi"""

    verify_file.write_text(f"""#!/usr/bin/env bash
set -uo pipefail

RED='\\033[0;31m'
GREEN='\\033[0;32m'
BOLD='\\033[1m'
NC='\\033[0m'

echo -e "${{BOLD}}Evaluating {lab_id}: {title}...${{NC}}"
{verify_code}

{score_block}
""", encoding="utf-8")
    make_executable(verify_file)

    reset_file = lab_dir / "reset.sh"
    reset_file.write_text(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up {lab_id}..."
{reset_code}
echo "[✓] Reset complete."
""", encoding="utf-8")
    make_executable(reset_file)

    return lab_id

def main():
    args = sys.argv[1:]
    if not args or args[0] in ["--all", "-all", "all"]:
        print(f"[*] Generating all 48 LFCS daily practice labs and {len(LFCS_MOCKS)} LFCS mock exams...")
        count = 0
        for wk, days in ALL_WEEKS:
            for item in days:
                lid = f"w{wk}d{item['day']}-lfcs"
                write_lab(lid, item["date"], item["lfcs_title"], item["lfcs_diff"], item["lfcs_time"],
                          item["lfcs_tasks"], item["lfcs_setup"], item["lfcs_verify"], item["lfcs_solution"], item["lfcs_reset"])
                count += 1
                print(f"  [✓] {lid}")
        for m in LFCS_MOCKS:
            write_lab(m["lab_id"], m["date"], m["title"], m["diff"], m["time"],
                      m["tasks"], m["setup"], m["verify"], m["solution"], m["reset"])
            count += 1
            print(f"  [✓] {m['lab_id']}")
        print(f"\n[★] All {count} LFCS lab scenarios successfully generated in {DIR}!")
        return

    arg = args[0].lower()
    if arg.startswith("w") and len(arg) == 2 and arg[1].isdigit():
        wk = int(arg[1])
        for wk_num, days in ALL_WEEKS:
            if wk_num == wk:
                print(f"[*] Generating Week {wk} LFCS labs...")
                for item in days:
                    lid = f"w{wk}d{item['day']}-lfcs"
                    write_lab(lid, item["date"], item["lfcs_title"], item["lfcs_diff"], item["lfcs_time"],
                              item["lfcs_tasks"], item["lfcs_setup"], item["lfcs_verify"], item["lfcs_solution"], item["lfcs_reset"])
                    print(f"  [✓] {lid}")
                return

    # Specific lab or mock
    for wk, days in ALL_WEEKS:
        for item in days:
            lid = f"w{wk}d{item['day']}-lfcs"
            if lid == arg:
                write_lab(lid, item["date"], item["lfcs_title"], item["lfcs_diff"], item["lfcs_time"],
                          item["lfcs_tasks"], item["lfcs_setup"], item["lfcs_verify"], item["lfcs_solution"], item["lfcs_reset"])
                print(f"[✓] Generated LFCS lab: {lid}")
                return

    for m in LFCS_MOCKS:
        if m["lab_id"].lower() == arg:
            write_lab(m["lab_id"], m["date"], m["title"], m["diff"], m["time"],
                      m["tasks"], m["setup"], m["verify"], m["solution"], m["reset"])
            print(f"[✓] Generated LFCS mock exam: {m['lab_id']}")
            return

    print(f"[-] LFCS lab '{arg}' not found.")
    print("Usage: python3 generate_labs.py [--all | w1 | w1d1-lfcs | mock-lfcs-1]")

if __name__ == "__main__":
    main()
