#!/usr/bin/env python3
"""
Comprehensive Live Cluster Test Runner for ALL 48 CKAD Labs and 2 Mock Exams.
Executes on the live VirtualBox K8s cluster (controlplane, node01, node02).

For each lab:
1. ./lab start <lab-id>: Verifies cluster setup executes cleanly (exit code 0).
2. ./lab check <lab-id>: Verifies the grader detects the unsolved state and REJECTS (exit code != 0, no false auto-pass).
3. ./lab reset <lab-id>: Verifies namespace and resource cleanup completes cleanly (exit code 0).
"""

import subprocess
import sys
import time

ALL_CKAD_TARGETS = [
    f"w{w}d{d}-ckad"
    for w in range(1, 9)
    for d in range(1, 7)
] + ["mock-ckad-1", "mock-ckad-2"]

def run(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def test_target(lab_id):
    # 1. Start lab
    t0 = time.time()
    rc_start, out_start, err_start = run(f"./lab start {lab_id}")
    t_start = round(time.time() - t0, 1)
    start_ok = (rc_start == 0)

    # 2. Check pre-solve (MUST fail/reject)
    t0 = time.time()
    rc_check, out_check, err_check = run(f"./lab check {lab_id}")
    t_check = round(time.time() - t0, 1)
    # MUST fail (non-zero) or output 0% score
    check_rejected = (rc_check != 0) or ("Score: 0/" in out_check) or ("[FAIL]" in out_check)

    # 3. Reset lab
    t0 = time.time()
    rc_reset, out_reset, err_reset = run(f"./lab reset {lab_id}")
    t_reset = round(time.time() - t0, 1)
    reset_ok = (rc_reset == 0)

    verdict = start_ok and check_rejected and reset_ok
    return {
        "lab": lab_id,
        "start": "PASS" if start_ok else f"FAIL(rc={rc_start})",
        "pre_check": "REJECT_OK" if check_rejected else "AUTO_PASS_BUG",
        "reset": "PASS" if reset_ok else f"FAIL(rc={rc_reset})",
        "verdict": "PASS" if verdict else "FAIL",
        "time": round(t_start + t_check + t_reset, 1),
        "details": {
            "start_err": err_start if not start_ok else "",
            "check_out": out_check if not check_rejected else "",
            "reset_err": err_reset if not reset_ok else ""
        }
    }

def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else ALL_CKAD_TARGETS
    print("=" * 80)
    print(f"LIVE CLUSTER VALIDATION RUNNER: {len(targets)} CKAD LABS & MOCK EXAMS")
    print("Target Cluster: controlplane (172.16.16.210), node01, node02")
    print("=" * 80)

    results = []
    failures = []

    for i, lab_id in enumerate(targets, 1):
        print(f"[{i:02d}/{len(targets):02d}] Testing {lab_id}...", end="", flush=True)
        res = test_target(lab_id)
        results.append(res)
        status_tag = "✓ PASS" if res["verdict"] == "PASS" else "✗ FAIL"
        print(f" {status_tag} ({res['time']}s) [Start: {res['start']} | PreCheck: {res['pre_check']} | Reset: {res['reset']}]")
        if res["verdict"] != "PASS":
            failures.append(res)
            print(f"      Details: {res['details']}")

    print("\n" + "=" * 80)
    print("FINAL SUMMARY REPORT")
    print("=" * 80)
    passed_count = sum(1 for r in results if r["verdict"] == "PASS")
    print(f"Total Targets Evaluated: {len(targets)}")
    print(f"Passed: {passed_count}/{len(targets)} ({round(passed_count/len(targets)*100, 1)}%)")
    print(f"Failed: {len(failures)}/{len(targets)}")

    if failures:
        print("\nFailed Scenarios:")
        for f in failures:
            print(f" - {f['lab']}: Start={f['start']}, PreCheck={f['pre_check']}, Reset={f['reset']}")
        sys.exit(1)
    else:
        print("\n[SUCCESS] ALL 48 CKAD LABS AND 2 MOCK EXAMS PASSED COMPLETE CLUSTER LIFECYCLE!")
        sys.exit(0)

if __name__ == "__main__":
    main()
