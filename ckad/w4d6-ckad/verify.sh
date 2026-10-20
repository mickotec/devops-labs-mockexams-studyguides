#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D6: Debugging Exit Codes in ckad-w4d6..."

MEM_PHASE=$(ssh controlplane 'kubectl get pod memory-hungry -n ckad-w4d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
MEM_READY=$(ssh controlplane 'kubectl get pod memory-hungry -n ckad-w4d6 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

EXEC_PHASE=$(ssh controlplane 'kubectl get pod broken-exec -n ckad-w4d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
EXEC_READY=$(ssh controlplane 'kubectl get pod broken-exec -n ckad-w4d6 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

if [ "$MEM_PHASE" == "Running" ] && [ "$MEM_READY" == "true" ] && [ "$EXEC_PHASE" == "Running" ] && [ "$EXEC_READY" == "true" ]; then
  echo -e "[0;32m[PASS] Both memory-hungry and broken-exec repaired and Running 1/1.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] memory-hungry: $MEM_PHASE ($MEM_READY) | broken-exec: $EXEC_PHASE ($EXEC_READY)[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi