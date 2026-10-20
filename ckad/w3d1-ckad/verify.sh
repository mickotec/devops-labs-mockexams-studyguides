#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D1: Sidecar Logging in ckad-w3d1..."

PHASE=$(ssh controlplane 'kubectl get pod app-logger -n ckad-w3d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY_COUNT=$(ssh controlplane 'kubectl get pod app-logger -n ckad-w3d1 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
LOG_OUT=$(ssh controlplane 'kubectl logs app-logger -c sidecar -n ckad-w3d1 2>/dev/null | head -n 1 || echo ""')

if [ "$PHASE" == "Running" ] && [ "$READY_COUNT" -eq 2 ] && [[ "$LOG_OUT" =~ "TRANSACTION_ID" ]]; then
  echo -e "[0;32m[PASS] Pod app-logger running 2/2 with sidecar successfully streaming transaction logs.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Ready: $READY_COUNT/2, Log: '$LOG_OUT'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi