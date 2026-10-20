#!/usr/bin/env python3
"""
Comprehensive End-to-End Solve Test Runner for CKAD Daily Labs (Weeks 1 to 8).
Executes on the live VirtualBox Kubernetes cluster (controlplane, node01, node02).

For each daily lab:
1. ./lab start <lab-id>             (Initializes the scenario)
2. Executes solution from solution.md (Applies official candidate steps)
3. Waits for pods/resources to reach Ready
4. ./lab check <lab-id>             (Validates 100% PASS with exit code 0)
5. ./lab reset <lab-id>             (Tears down test resources)
"""

import os
import sys
import time
import subprocess

CWD = "/home/micko/Projects/labs_&_exams"

ALL_DAILY_LABS = [
    f"w{w}d{d}-ckad"
    for w in range(1, 9)
    for d in range(1, 7)
]

def run(cmd):
    res = subprocess.run(cmd, cwd=CWD, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def extract_solution(lab_id):
    path = os.path.join(CWD, "ckad", lab_id, "solution.md")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        content = f.read()
    start = content.find("```bash")
    if start == -1:
        return None
    start = content.find("\n", start) + 1
    end = content.find("```", start)
    if end == -1:
        return None
    return content[start:end].strip()

def test_daily_lab(lab_id):
    sol = extract_solution(lab_id)
    if not sol:
        return {"lab": lab_id, "status": "FAIL", "reason": "Missing solution.md"}

    # 1. Start lab
    t0 = time.time()
    rc_start, out_start, err_start = run(f"./lab start {lab_id}")
    if rc_start != 0:
        return {"lab": lab_id, "status": "FAIL", "reason": f"Start failed: {err_start or out_start}"}

    time.sleep(6)

    # 2. Apply solution
    rc_sol, out_sol, err_sol = run(sol)
    
    # 3. Wait for pod/resource stabilization
    time.sleep(6)

    # 4. Grade solution
    rc_check, out_check, err_check = run(f"./lab check {lab_id}")
    check_pass = (rc_check == 0) and ("100%" in out_check or "[PASS]" in out_check)

    # 5. Reset lab
    rc_reset, out_reset, err_reset = run(f"./lab reset {lab_id}")

    elapsed = round(time.time() - t0, 1)

    if check_pass and rc_reset == 0:
        return {"lab": lab_id, "status": "PASS", "time": elapsed, "output": out_check}
    else:
        return {
            "lab": lab_id,
            "status": "FAIL",
            "time": elapsed,
            "reason": f"Grade failed: {out_check}" if not check_pass else f"Reset failed: {err_reset}"
        }

def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else ALL_DAILY_LABS
    print("=" * 80)
    print(f"LIVE CLUSTER SOLVE RUNNER: {len(targets)} CKAD DAILY LABS")
    print("Target Cluster: controlplane (172.16.16.210), node01, node02")
    print("=" * 80)

    results = []
    failures = []

    for i, lab_id in enumerate(targets, 1):
        print(f"[{i:02d}/{len(targets):02d}] Solving & Grading {lab_id}...", end="", flush=True)
        res = test_daily_lab(lab_id)
        results.append(res)
        tag = "✓ PASS" if res["status"] == "PASS" else "✗ FAIL"
        print(f" {tag} ({res.get('time', 0)}s)")
        if res["status"] != "PASS":
            failures.append(res)
            print(f"      Reason: {res.get('reason')}")

    print("\n" + "=" * 80)
    print("DAILY LABS SOLVE SUMMARY REPORT")
    print("=" * 80)
    passed = sum(1 for r in results if r["status"] == "PASS")
    print(f"Total Daily Labs Evaluated: {len(targets)}")
    print(f"Passed: {passed}/{len(targets)} ({round(passed/len(targets)*100, 1)}%)")
    print(f"Failed: {len(failures)}/{len(targets)}")

    if failures:
        print("\nFailed Daily Labs:")
        for f in failures:
            print(f" - {f['lab']}: {f.get('reason')}")
        sys.exit(1)
    else:
        print("\n[SUCCESS] ALL TESTED DAILY LABS SOLVED AND GRADED 100% ON LIVE CLUSTER!")
        sys.exit(0)

if __name__ == "__main__":
    main()
