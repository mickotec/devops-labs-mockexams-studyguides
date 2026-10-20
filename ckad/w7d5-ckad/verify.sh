#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D5: StorageClasses in ckad-w7d5..."

MODE=$(ssh controlplane 'kubectl get sc delayed-storage -o jsonpath="{.volumeBindingMode}" 2>/dev/null || echo ""')
PVC_STATUS=$(ssh controlplane 'kubectl get pvc delayed-pvc -n ckad-w7d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')

if [ "$MODE" == "WaitForFirstConsumer" ] && [ "$PVC_STATUS" == "Pending" ]; then
  echo -e "[0;32m[PASS] StorageClass configured with WaitForFirstConsumer and PVC pending consumer scheduling.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] volumeBindingMode: '$MODE' (expected WaitForFirstConsumer) | PVC status: '$PVC_STATUS' (expected Pending).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi