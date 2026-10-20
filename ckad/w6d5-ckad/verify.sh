#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D5: Ingress Routing in ckad-w6d5..."

HOST=$(ssh controlplane 'kubectl get ingress ecommerce-ingress -n ckad-w6d5 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
PATHS=$(ssh controlplane 'kubectl get ingress ecommerce-ingress -n ckad-w6d5 -o jsonpath="{.spec.rules[0].http.paths[*].path}" 2>/dev/null || echo ""')

if [ "$HOST" == "store.internal" ] && [[ "$PATHS" =~ "/orders" ]] && [[ "$PATHS" =~ "/catalog" ]]; then
  echo -e "[0;32m[PASS] Ingress ecommerce-ingress successfully routes host store.internal on /orders and /catalog.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Host: '$HOST' | Paths: '$PATHS'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi