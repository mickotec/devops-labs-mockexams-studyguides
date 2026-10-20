#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D2: ConfigMaps & Environment Variables in ckad-w2d2..."

PHASE=$(ssh controlplane 'kubectl get pod app-server -n ckad-w2d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
ENV_DB_HOST=$(ssh controlplane 'kubectl exec app-server -n ckad-w2d2 -- printenv DB_HOST 2>/dev/null || echo ""')
ENV_APP_ENV=$(ssh controlplane 'kubectl exec app-server -n ckad-w2d2 -- printenv APP_ENV 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$ENV_DB_HOST" == "postgres.internal" ] && [ "$ENV_APP_ENV" == "production" ]; then
  echo -e "[0;32m[PASS] Pod app-server successfully injected with envFrom ConfigMap and literal env.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE | DB_HOST: '$ENV_DB_HOST' | APP_ENV: '$ENV_APP_ENV'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi