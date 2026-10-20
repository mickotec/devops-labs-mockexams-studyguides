#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D3: PVC Binding in ckad-w7d3..."

STATUS=$(ssh controlplane 'kubectl get pvc app-storage-pvc -n ckad-w7d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
BOUND_PV=$(ssh controlplane 'kubectl get pvc app-storage-pvc -n ckad-w7d3 -o jsonpath="{.spec.volumeName}" 2>/dev/null || echo ""')

if [ "$STATUS" == "Bound" ] && [ "$BOUND_PV" == "claim-target-pv" ]; then
  echo -e "[0;32m[PASS] PVC app-storage-pvc successfully Bound to claim-target-pv.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Status: '$STATUS' (expected Bound) | Bound PV: '$BOUND_PV'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi