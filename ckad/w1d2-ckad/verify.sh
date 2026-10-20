#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D2: Editing Pod Command & Args in ckad-w1d2..."

PHASE=$(ssh controlplane 'kubectl get pod data-worker -n ckad-w1d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
if [ "$PHASE" != "Running" ]; then
  echo -e "\033[0;31m[FAIL] Pod data-worker is '$PHASE' (expected Running).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

ARGS=$(ssh controlplane 'kubectl get pod data-worker -n ckad-w1d2 -o jsonpath="{.spec.containers[0].args}" 2>/dev/null || echo ""')
LOG_CHECK=$(ssh controlplane 'kubectl exec data-worker -n ckad-w1d2 -- cat /tmp/processed.log 2>/dev/null | head -n 1 || echo "Empty"')

if [[ "$ARGS" =~ "processed.log" ]] && [ "$LOG_CHECK" != "Empty" ]; then
  echo -e "\033[0;32m[PASS] Pod data-worker successfully updated with command/args loop.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Pod command/args not updated or /tmp/processed.log not generated.\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi