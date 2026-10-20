#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D3: Rollback in ckad-w5d3..."

IMG=$(ssh controlplane 'kubectl get deploy checkout-api -n ckad-w5d3 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
READY=$(ssh controlplane 'kubectl get deploy checkout-api -n ckad-w5d3 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')

if [[ "$IMG" =~ "nginx:1.24-alpine" ]] && [ "$READY" -eq 3 ]; then
  echo -e "[0;32m[PASS] checkout-api successfully rolled back to revision 1 (nginx:1.24-alpine, 3/3 Ready).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Image: $IMG (expected nginx:1.24-alpine), Ready: $READY (expected 3).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi