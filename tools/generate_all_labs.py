#!/usr/bin/env python3
"""
Master Lab Generator for all 100 CKA and LFCS Labs.
Covers:
  - Weeks 1 to 8 (96 daily labs: 48 CKA + 48 LFCS)
  - 4 Comprehensive Mock Exams (mock-cka-1, mock-cka-2, mock-lfcs-1, mock-lfcs-2)
Generates complete, production-grade lab packages:
  - meta.env
  - scenario.md
  - setup.sh
  - verify.sh
  - solution.md
  - reset.sh
"""

import os
import stat

from curriculum.cka.labs_week1 import WEEK_1_LABS as CKA_W1
from curriculum.cka.labs_week2 import WEEK_2_LABS as CKA_W2
from curriculum.cka.labs_week3 import WEEK_3_LABS as CKA_W3
from curriculum.cka.labs_week4 import WEEK_4_LABS as CKA_W4
from curriculum.cka.labs_week5 import WEEK_5_LABS as CKA_W5
from curriculum.cka.labs_week6 import WEEK_6_LABS as CKA_W6
from curriculum.cka.labs_week7 import WEEK_7_LABS as CKA_W7
from curriculum.cka.labs_week8 import WEEK_8_LABS as CKA_W8
from curriculum.cka.labs_mocks import MOCK_LABS as CKA_MOCKS

from curriculum.lfcs.labs_week1 import WEEK_1_LABS as LFCS_W1
from curriculum.lfcs.labs_week2 import WEEK_2_LABS as LFCS_W2
from curriculum.lfcs.labs_week3 import WEEK_3_LABS as LFCS_W3
from curriculum.lfcs.labs_week4 import WEEK_4_LABS as LFCS_W4
from curriculum.lfcs.labs_week5 import WEEK_5_LABS as LFCS_W5
from curriculum.lfcs.labs_week6 import WEEK_6_LABS as LFCS_W6
from curriculum.lfcs.labs_week7 import WEEK_7_LABS as LFCS_W7
from curriculum.lfcs.labs_week8 import WEEK_8_LABS as LFCS_W8
from curriculum.lfcs.labs_mocks import MOCK_LABS as LFCS_MOCKS

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(TOOLS_DIR) if os.path.basename(TOOLS_DIR) == "tools" else TOOLS_DIR
CKA_DIR = os.path.join(REPO_DIR, "cka")
LFCS_DIR = os.path.join(REPO_DIR, "lfcs")

CKA_WEEKS = [
    (1, CKA_W1), (2, CKA_W2), (3, CKA_W3), (4, CKA_W4),
    (5, CKA_W5), (6, CKA_W6), (7, CKA_W7), (8, CKA_W8),
]
LFCS_WEEKS = [
    (1, LFCS_W1), (2, LFCS_W2), (3, LFCS_W3), (4, LFCS_W4),
    (5, LFCS_W5), (6, LFCS_W6), (7, LFCS_W7), (8, LFCS_W8),
]

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

def write_lab(lab_id, track, date_str, title, diff, time_limit, tasks, setup_code, verify_code, solution_code, reset_code):
    parent_dir = CKA_DIR if track.upper() == "CKA" else LFCS_DIR
    lab_dir = os.path.join(parent_dir, lab_id)
    os.makedirs(lab_dir, exist_ok=True)

    # 1. meta.env
    pass_score = "66%" if (lab_id.startswith("mock-") and track == "CKA") else ("67%" if lab_id.startswith("mock-") else "100%")
    with open(os.path.join(lab_dir, "meta.env"), "w", encoding="utf-8") as f:
        f.write(f"""TRACK="{track}"
DATE="{date_str}"
TITLE="{title}"
DIFFICULTY="{diff}"
TIME_LIMIT="{time_limit}"
PASSING_SCORE="{pass_score}"
""")

    # 2. scenario.md
    with open(os.path.join(lab_dir, "scenario.md"), "w", encoding="utf-8") as f:
        target_str = "VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)" if track == "CKA" else "VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal"
        pass_line = f"\n**Passing Score:** {pass_score}  " if lab_id.startswith("mock-") else ""
        f.write(f"""# [{track} {lab_id.upper()}] {title}

**Date:** {date_str}  
**Time Limit:** {time_limit}  {pass_line}
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
./lab check {lab_id}
```
""")

    # 3. setup.sh
    setup_path = os.path.join(lab_dir, "setup.sh")
    with open(setup_path, "w", encoding="utf-8") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up {lab_id} ({title})..."
{setup_code}
echo "[✓] Environment ready. Review tasks with: ./lab show {lab_id}"
""")
    make_executable(setup_path)

    # 4. verify.sh
    verify_path = os.path.join(lab_dir, "verify.sh")
    with open(verify_path, "w", encoding="utf-8") as f:
        if lab_id.startswith("mock-") and track == "CKA":
            score_block = f"""
PCT_STOR=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_STOR * 10.0 / $TOTAL_STOR}}")
PCT_TROUBLE=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_TROUBLE * 30.0 / $TOTAL_TROUBLE}}")
PCT_WORKLOAD=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_WORKLOAD * 15.0 / $TOTAL_WORKLOAD}}")
PCT_CLUSTER=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_CLUSTER * 25.0 / $TOTAL_CLUSTER}}")
PCT_SVC=$(awk "BEGIN {{printf \\"%.1f\\", $SCORE_SVC * 20.0 / $TOTAL_SVC}}")

TOTAL_PCT=$(awk "BEGIN {{printf \\"%.1f\\", ($SCORE_STOR * 10.0 / $TOTAL_STOR) + ($SCORE_TROUBLE * 30.0 / $TOTAL_TROUBLE) + ($SCORE_WORKLOAD * 15.0 / $TOTAL_WORKLOAD) + ($SCORE_CLUSTER * 25.0 / $TOTAL_CLUSTER) + ($SCORE_SVC * 20.0 / $TOTAL_SVC)}}")

echo ""
echo "────────────────────────────────────────────────────────────"
echo -e "${{BOLD}}Linux Foundation Domain Weight Breakdown (CKA):${{NC}}"
echo -e "  • Storage (10%):                                     ${{SCORE_STOR}}/${{TOTAL_STOR}} passed   (${{PCT_STOR}}% / 10.0%)"
echo -e "  • Troubleshooting (30%):                             ${{SCORE_TROUBLE}}/${{TOTAL_TROUBLE}} passed   (${{PCT_TROUBLE}}% / 30.0%)"
echo -e "  • Workloads & Scheduling (15%):                      ${{SCORE_WORKLOAD}}/${{TOTAL_WORKLOAD}} passed   (${{PCT_WORKLOAD}}% / 15.0%)"
echo -e "  • Cluster Architecture, Install & Config (25%):      ${{SCORE_CLUSTER}}/${{TOTAL_CLUSTER}} passed   (${{PCT_CLUSTER}}% / 25.0%)"
echo -e "  • Services & Networking (20%):                       ${{SCORE_SVC}}/${{TOTAL_SVC}} passed   (${{PCT_SVC}}% / 20.0%)"
echo "────────────────────────────────────────────────────────────"
echo -e "Questions Passed:     ${{BOLD}}${{TOTAL_PASSED}} / ${{TOTAL_QUESTIONS}}${{NC}}"
echo -e "Final Weighted Score: ${{BOLD}}${{TOTAL_PCT}}%${{NC}}"
echo -e "Passing Threshold:    66.0%"
echo "────────────────────────────────────────────────────────────"

IS_PASS=$(awk "BEGIN {{if ($TOTAL_PCT >= 66.0) print 1; else print 0}}")
if [ "$IS_PASS" -eq 1 ]; then
  echo -e "${{GREEN}}${{BOLD}}CONGRATULATIONS! Mock Exam {lab_id} completed successfully! (${{TOTAL_PCT}}% >= 66.0%)${{NC}}"
  exit 0
else
  echo -e "${{RED}}Score below passing threshold (66.0%). Current: ${{TOTAL_PCT}}%. Review domain competencies or run: ./lab solve {lab_id}${{NC}}"
  exit 1
fi"""
        elif lab_id.startswith("mock-") and track == "LFCS":
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

        f.write(f"""#!/usr/bin/env bash
set -uo pipefail

RED='\\033[0;31m'
GREEN='\\033[0;32m'
BOLD='\\033[1m'
NC='\\033[0m'

echo -e "${{BOLD}}Evaluating {lab_id}: {title}...${{NC}}"
{verify_code}

{score_block}
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

    # Generate CKA Weeks 1 to 8
    for week_num, days_data in CKA_WEEKS:
        print(f"--> Processing CKA Week {week_num} ({len(days_data)} days)...")
        for item in days_data:
            d = item["day"]
            date_str = item["date"]
            cka_id = f"w{week_num}d{d}-cka"
            write_lab(
                cka_id,
                "CKA",
                date_str,
                item["title"],
                item["diff"],
                item["time"],
                item["tasks"],
                item["setup"],
                item["verify"],
                item["solution"],
                item["reset"]
            )
            total_generated += 1

    # Generate LFCS Weeks 1 to 8
    for week_num, days_data in LFCS_WEEKS:
        print(f"--> Processing LFCS Week {week_num} ({len(days_data)} days)...")
        for item in days_data:
            d = item["day"]
            date_str = item["date"]
            lfcs_id = f"w{week_num}d{d}-lfcs"
            write_lab(
                lfcs_id,
                "LFCS",
                date_str,
                item["title"],
                item["diff"],
                item["time"],
                item["tasks"],
                item["setup"],
                item["verify"],
                item["solution"],
                item["reset"]
            )
            total_generated += 1

    # Generate CKA Mock Exams
    print(f"--> Processing CKA Mock Exams ({len(CKA_MOCKS)} mock exams)...")
    for mock in CKA_MOCKS:
        write_lab(
            mock["lab_id"],
            "CKA",
            mock["date"],
            mock["title"],
            mock["diff"],
            mock["time"],
            mock["tasks"],
            mock["setup"],
            mock["verify"],
            mock["solution"],
            mock["reset"]
        )
        total_generated += 1

    # Generate LFCS Mock Exams
    print(f"--> Processing LFCS Mock Exams ({len(LFCS_MOCKS)} mock exams)...")
    for mock in LFCS_MOCKS:
        write_lab(
            mock["lab_id"],
            "LFCS",
            mock["date"],
            mock["title"],
            mock["diff"],
            mock["time"],
            mock["tasks"],
            mock["setup"],
            mock["verify"],
            mock["solution"],
            mock["reset"]
        )
        total_generated += 1

    print(f"\n[SUCCESS] Successfully generated all {total_generated} production-grade labs across Weeks 1-8 and Mock Exams!")

if __name__ == "__main__":
    main()
