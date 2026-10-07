#!/usr/bin/env python3
"""
Generate complete, production-grade lab packages for Weeks 3 to 8 (both CKA and LFCS).
Replaces generic placeholder stubs with rich, curriculum-aligned scenarios, setups,
verifications, solutions, and resets.
"""

import os
import stat

from curriculum.labs_week3 import WEEK_3_LABS
from curriculum.labs_week4 import WEEK_4_LABS
from curriculum.labs_week5 import WEEK_5_LABS
from curriculum.labs_week6 import WEEK_6_LABS
from curriculum.labs_week7 import WEEK_7_LABS
from curriculum.labs_week8 import WEEK_8_LABS

from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO_DIR = TOOLS_DIR.parent if TOOLS_DIR.name == "tools" else TOOLS_DIR
BASE_DIR = str(REPO_DIR)

ALL_WEEKS = [
    (3, WEEK_3_LABS),
    (4, WEEK_4_LABS),
    (5, WEEK_5_LABS),
    (6, WEEK_6_LABS),
    (7, WEEK_7_LABS),
    (8, WEEK_8_LABS),
]

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

def write_lab(lab_id, track, date_str, title, diff, time_limit, tasks, setup_code, verify_code, solution_code, reset_code):
    lab_dir = os.path.join(BASE_DIR, lab_id)
    os.makedirs(lab_dir, exist_ok=True)

    # 1. meta.env
    with open(os.path.join(lab_dir, "meta.env"), "w", encoding="utf-8") as f:
        f.write(f"""TRACK="{track}"
DATE="{date_str}"
TITLE="{title}"
DIFFICULTY="{diff}"
TIME_LIMIT="{time_limit}"
""")

    # 2. scenario.md
    with open(os.path.join(lab_dir, "scenario.md"), "w", encoding="utf-8") as f:
        target_str = "VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)" if track == "CKA" else "VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal"
        f.write(f"""# [{track} {lab_id.upper()}] {title}

**Date:** {date_str}  
**Time Limit:** {time_limit}  
**Difficulty:** {diff}  
**Target:** {target_str}  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

{tasks}

---

## 🔍 Validation
Run the automated grader:
```bash
lab check {lab_id}
```
""")

    # 3. setup.sh
    setup_path = os.path.join(lab_dir, "setup.sh")
    with open(setup_path, "w", encoding="utf-8") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up {lab_id} ({title})..."
{setup_code}
echo "[✓] Environment ready. Review tasks with: lab show {lab_id}"
""")
    make_executable(setup_path)

    # 4. verify.sh
    verify_path = os.path.join(lab_dir, "verify.sh")
    with open(verify_path, "w", encoding="utf-8") as f:
        f.write(f"""#!/usr/bin/env bash
set -uo pipefail

RED='\\033[0;31m'
GREEN='\\033[0;32m'
BOLD='\\033[1m'
NC='\\033[0m'

echo -e "${{BOLD}}Evaluating {lab_id}: {title}...${{NC}}"
{verify_code}

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${{BOLD}}${{SCORE}}/${{TOTAL}}${{NC}}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${{GREEN}}${{BOLD}}CONGRATULATIONS! Lab {lab_id} completed successfully!${{NC}}"
  exit 0
else
  echo -e "${{RED}}Checks incomplete. Review scenario tasks or run: lab solve {lab_id}${{NC}}"
  exit 1
fi
""")
    make_executable(verify_path)

    # 5. solution.md
    with open(os.path.join(lab_dir, "solution.md"), "w", encoding="utf-8") as f:
        f.write(f"""# [{track} {lab_id.upper()}] Solution & Technical Walkthrough

### Tasks & Official Solution
{solution_code}
""")

    # 6. reset.sh
    reset_path = os.path.join(lab_dir, "reset.sh")
    with open(reset_path, "w", encoding="utf-8") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up {lab_id}..."
{reset_code}
echo "[✓] Reset complete."
""")
    make_executable(reset_path)

def main():
    total_generated = 0
    for week_num, days_data in ALL_WEEKS:
        print(f"--> Processing Week {week_num} ({len(days_data)} days)...")
        for item in days_data:
            d = item["day"]
            date_str = item["date"]

            # Generate CKA lab
            cka_id = f"w{week_num}d{d}-cka"
            write_lab(
                cka_id,
                "CKA",
                date_str,
                item["cka_title"],
                item["cka_diff"],
                item["cka_time"],
                item["cka_tasks"],
                item["cka_setup"],
                item["cka_verify"],
                item["cka_solution"],
                item["cka_reset"]
            )
            total_generated += 1

            # Generate LFCS lab
            lfcs_id = f"w{week_num}d{d}-lfcs"
            write_lab(
                lfcs_id,
                "LFCS",
                date_str,
                item["lfcs_title"],
                item["lfcs_diff"],
                item["lfcs_time"],
                item["lfcs_tasks"],
                item["lfcs_setup"],
                item["lfcs_verify"],
                item["lfcs_solution"],
                item["lfcs_reset"]
            )
            total_generated += 1

    print(f"\n[SUCCESS] Successfully generated {total_generated} production-grade labs for Weeks 3 through 8!")

if __name__ == "__main__":
    main()
