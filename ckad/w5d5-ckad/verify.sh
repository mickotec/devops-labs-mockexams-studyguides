#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D5: Canary Deployment in ckad-w5d5..."

CANARY_READY=$(ssh controlplane 'kubectl get deploy catalog-canary -n ckad-w5d5 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints catalog-svc -n ckad-w5d5 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null | wc -w || echo 0')

if [ "$CANARY_READY" -eq 1 ] && [ "$EP_COUNT" -eq 5 ]; then
  echo -e "[0;32m[PASS] catalog-canary deployed (1 replica) and catalog-svc has 5 endpoints (20% canary split).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Canary ready: $CANARY_READY/1 | Total endpoints: $EP_COUNT (expected 5).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi