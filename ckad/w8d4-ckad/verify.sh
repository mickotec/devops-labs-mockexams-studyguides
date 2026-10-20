#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D4: API Deprecations in ckad-w8d4..."

API_VER=$(ssh controlplane 'kubectl get ingress legacy-ingress -n ckad-w8d4 -o jsonpath="{.apiVersion}" 2>/dev/null || echo ""')
HOST=$(ssh controlplane 'kubectl get ingress legacy-ingress -n ckad-w8d4 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')

if [ "$API_VER" == "networking.k8s.io/v1" ] && [ "$HOST" == "legacy.example.com" ]; then
  echo -e "[0;32m[PASS] Ingress successfully migrated to networking.k8s.io/v1 and applied.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] apiVersion: '$API_VER' (expected networking.k8s.io/v1) | Host: '$HOST'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi