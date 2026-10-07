#!/usr/bin/env python3
"""
Comprehensive Lifecycle & Pre-Check Reject Validator across all 100 labs.
Ensures:
1. `./lab start <lab_id>` succeeds and initializes the real environment.
2. `./lab check <lab_id>` rejects the uncompleted lab (MUST FAIL - NO AUTO-PASS).
3. `./lab reset <lab_id>` cleanly tears down and restores cluster/node state.
"""

import sys
import subprocess
import time

def run(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout, res.stderr

def main():
    target_labs = sys.argv[1:]
    if not target_labs:
        print("Usage: python3 test_all_100_lifecycle.py <lab_id1> [lab_id2...]")
        sys.exit(1)

    print("=" * 75)
    print(f"LIFECYCLE & PRE-CHECK VALIDATION ({len(target_labs)} LABS)")
    print("=" * 75)

    records = []
    failures = []

    for idx, lab_id in enumerate(target_labs, 1):
        print(f"\n[{idx}/{len(target_labs)}] Testing {lab_id}...")

        # 1. Start
        t0 = time.time()
        rc_start, out_start, err_start = run(f"./lab start {lab_id}")
        start_time = round(time.time() - t0, 1)
        start_ok = (rc_start == 0)
        print(f"  Start:     {'PASS' if start_ok else 'FAIL'} ({start_time}s)")
        if not start_ok:
            print(f"    Error: {err_start or out_start}")

        # 2. Check (MUST FAIL before solution)
        rc_pre, out_pre, err_pre = run(f"./lab check {lab_id}")
        pre_ok = (rc_pre != 0)
        print(f"  Pre-Check: {'REJECTED (Correct)' if pre_ok else 'AUTO-PASS BUG!'}")
        if not pre_ok:
            print(f"    Check Output:\n{out_pre}")

        # 3. Reset
        rc_reset, out_reset, err_reset = run(f"./lab reset {lab_id}")
        reset_ok = (rc_reset == 0)
        print(f"  Reset:     {'CLEAN' if reset_ok else 'FAIL'}")
        if not reset_ok:
            print(f"    Error: {err_reset or out_reset}")

        verdict = start_ok and pre_ok and reset_ok
        records.append({
            "lab": lab_id,
            "start": "PASS" if start_ok else "FAIL",
            "pre": "PASS" if pre_ok else "FAIL",
            "reset": "PASS" if reset_ok else "FAIL",
            "verdict": "PASS" if verdict else "FAIL"
        })

        if not verdict:
            failures.append(lab_id)

    print("\n" + "=" * 75)
    print("VALIDATION SUMMARY MATRIX")
    print("=" * 75)
    print(f"{'Lab ID':<14} | {'Start':<6} | {'Pre-Check':<10} | {'Reset':<6} | {'Verdict':<7}")
    print("-" * 75)
    for r in records:
        print(f"{r['lab']:<14} | {r['start']:<6} | {r['pre']:<10} | {r['reset']:<6} | {r['verdict']:<7}")
    print("=" * 75)
    passed_count = sum(1 for r in records if r['verdict'] == "PASS")
    print(f"TOTAL: {passed_count}/{len(target_labs)} LABS PASSED")
    if failures:
        print(f"FAILED: {', '.join(failures)}")
        sys.exit(1)
    else:
        print("ALL TESTED LABS PASSED LIFECYCLE & PRE-CHECK VALIDATION!")
        sys.exit(0)

if __name__ == "__main__":
    main()
