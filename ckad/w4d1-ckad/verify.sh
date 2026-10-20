#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D1: Readiness Probes in ckad-w4d1..."

PHASE=$(ssh controlplane 'kubectl get pod order-processor -n ckad-w4d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod order-processor -n ckad-w4d1 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
EP=$(ssh controlplane 'kubectl get endpoints order-service -n ckad-w4d1 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ] && [ -n "$EP" ]; then
  echo -e "[0;32m[PASS] Pod order-processor ready and registered in order-service endpoints.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Ready: $READY, Endpoints: '$EP'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi