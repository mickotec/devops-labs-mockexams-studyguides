#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D4: Pod Ingress Rules in ckad-w6d4..."

TARGET=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.podSelector.matchLabels.tier}" 2>/dev/null || echo ""')
ALLOW_TIER=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.ingress[*].from[*].podSelector.matchLabels.tier}" 2>/dev/null || echo ""')
PORT=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.ingress[*].ports[*].port}" 2>/dev/null || echo 0')

if [ "$TARGET" == "backend" ] && [ "$ALLOW_TIER" == "frontend" ] && [ "$PORT" -eq 8080 ]; then
  echo -e "[0;32m[PASS] NetworkPolicy allow-frontend-only correctly permits tier=frontend on TCP 8080.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Target tier: '$TARGET' | Allow tier: '$ALLOW_TIER' | Port: $PORT[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi