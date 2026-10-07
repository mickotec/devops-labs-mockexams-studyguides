#!/usr/bin/env python3
"""
Automated validation harness to test lab setup, initial grading (must not auto-pass),
and reset across all weeks.
"""

import subprocess
import sys

# Comprehensive test suite covering Week 1, Week 2, Mock Exams, and Weeks 3-8
LABS_TO_TEST = [
    # Mock Exams
    "mock-cka-1", "mock-cka-2",
    "mock-lfcs-1", "mock-lfcs-2",
    # Week 1 (All 12 labs)
    "w1d1-cka", "w1d1-lfcs",
    "w1d2-cka", "w1d2-lfcs",
    "w1d3-cka", "w1d3-lfcs",
    "w1d4-cka", "w1d4-lfcs",
    "w1d5-cka", "w1d5-lfcs",
    "w1d6-cka", "w1d6-lfcs",
    # Week 2 (All 12 labs)
    "w2d1-cka", "w2d1-lfcs",
    "w2d2-cka", "w2d2-lfcs",
    "w2d3-cka", "w2d3-lfcs",
    "w2d4-cka", "w2d4-lfcs",
    "w2d5-cka", "w2d5-lfcs",
    "w2d6-cka", "w2d6-lfcs",
    # Representative samples from Weeks 3-8
    "w3d1-cka", "w3d1-lfcs",
    "w4d1-cka", "w4d1-lfcs",
    "w5d1-cka", "w5d1-lfcs",
    "w6d1-cka", "w6d1-lfcs",
    "w7d2-cka", "w7d2-lfcs",
    "w8d3-cka", "w8d3-lfcs",
]

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout, res.stderr

print(f"Starting test sweep across {len(LABS_TO_TEST)} representative labs...")

results = []

for lab_id in LABS_TO_TEST:
    print(f"\n[--> Testing {lab_id}]")

    # 1. Start lab (setup.sh)
    rc_start, out_start, err_start = run_cmd(f"./lab start {lab_id}")
    if rc_start != 0:
        print(f"  [ERROR] ./lab start {lab_id} failed (code {rc_start}):\n{err_start or out_start}")
        results.append((lab_id, "START_FAILED"))
        continue
    else:
        print(f"  [OK] setup.sh succeeded")

    # 2. Check lab (verify.sh before solution - MUST FAIL)
    rc_check, out_check, err_check = run_cmd(f"./lab check {lab_id}")
    if rc_check == 0:
        print(f"  [BUG] ./lab check {lab_id} PASSED without candidate doing anything! (Auto-pass bug)")
        results.append((lab_id, "AUTO_PASS_BUG"))
    else:
        print(f"  [OK] verify.sh properly rejected uncompleted state (exit {rc_check})")

    # 3. Reset lab (reset.sh)
    rc_reset, out_reset, err_reset = run_cmd(f"./lab reset {lab_id}")
    if rc_reset != 0:
        print(f"  [ERROR] ./lab reset {lab_id} failed (code {rc_reset}):\n{err_reset or out_reset}")
        results.append((lab_id, "RESET_FAILED"))
    else:
        print(f"  [OK] reset.sh succeeded")
        results.append((lab_id, "PASSED"))

print("\n" + "="*50)
print("TEST SUMMARY:")
passed_count = sum(1 for _, s in results if s == "PASSED")
print(f"Total tested: {len(results)} | Passed Lifecycle: {passed_count}/{len(results)}")
for lab, stat in results:
    if stat != "PASSED":
        print(f"  FAILED: {lab} -> {stat}")
print("="*50)
