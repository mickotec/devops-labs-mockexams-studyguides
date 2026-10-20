#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D4: Data Persistence in ckad-w7d4..."

READER_PHASE=$(ssh controlplane 'kubectl get pod state-reader -n ckad-w7d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
CONTENT=$(ssh controlplane 'kubectl exec state-reader -n ckad-w7d4 -- cat /var/storage/state.txt 2>/dev/null || echo ""')

if [ "$READER_PHASE" == "Running" ] && [[ "$CONTENT" =~ "PERSISTED_STATE_OK" ]]; then
  echo -e "[0;32m[PASS] Data persisted across pod deletion and read by state-reader.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] state-reader phase: $READER_PHASE | Content: '$CONTENT'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi