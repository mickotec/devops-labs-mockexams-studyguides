#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD killer.sh Mock Exam 1 (Timed Simulation) in namespace ckad-w8d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d5.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi