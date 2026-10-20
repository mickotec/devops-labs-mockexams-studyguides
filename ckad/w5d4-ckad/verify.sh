#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D4: Blue-Green Cutover in ckad-w5d4..."

GREEN_READY=$(ssh controlplane 'kubectl get deploy portal-green -n ckad-w5d4 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
SVC_VERSION=$(ssh controlplane 'kubectl get svc web-portal -n ckad-w5d4 -o jsonpath="{.spec.selector.version}" 2>/dev/null || echo "v1"')

if [ "$GREEN_READY" -eq 3 ] && [ "$SVC_VERSION" == "v2" ]; then
  echo -e "[0;32m[PASS] Green release ready (3/3) and web-portal service switched to version=v2.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] portal-green ready: $GREEN_READY/3 | web-portal selector version: '$SVC_VERSION' (expected v2).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi