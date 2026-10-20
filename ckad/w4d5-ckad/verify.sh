#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D5: kubectl top in kube-system..."

SAVED_POD=$(ssh controlplane 'cat /tmp/top-cpu-pod.txt 2>/dev/null | tr -d "[:space:]"')
TOP_POD=$(ssh controlplane 'kubectl top pod -n kube-system --sort-by=cpu --no-headers 2>/dev/null | head -n 1 | awk "{print \$1}" | tr -d "[:space:]"')

if [ -n "$SAVED_POD" ] && [ "$SAVED_POD" == "$TOP_POD" ]; then
  echo -e "[0;32m[PASS] Top CPU pod identified accurately: $SAVED_POD[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Saved pod: '$SAVED_POD' vs Actual top pod: '$TOP_POD'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi