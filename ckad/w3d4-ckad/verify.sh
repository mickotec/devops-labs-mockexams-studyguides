#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D4: Init Container Unblocking in ckad-w3d4..."

PHASE=$(ssh controlplane 'kubectl get pod webapp-gated -n ckad-w3d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod webapp-gated -n ckad-w3d4 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ]; then
  echo -e "[0;32m[PASS] webapp-gated unblocked and Running 1/1 after service dependency fulfilled.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Ready: $READY (expected 1/1 Running).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi