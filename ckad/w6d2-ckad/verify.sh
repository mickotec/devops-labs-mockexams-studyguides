#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D2: Headless Service in ckad-w6d2..."

CIP=$(ssh controlplane 'kubectl get svc db-headless -n ckad-w6d2 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "not-found"')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints db-headless -n ckad-w6d2 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null | wc -w || echo 0')

if [ "$CIP" == "None" ] && [ "$EP_COUNT" -eq 2 ]; then
  echo -e "[0;32m[PASS] Headless service db-headless (clusterIP: None) successfully tracking 2 pod endpoints.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] clusterIP: '$CIP' (expected None) | Endpoint count: $EP_COUNT (expected 2).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi