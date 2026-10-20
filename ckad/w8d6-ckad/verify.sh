#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D6: Kustomize Overlays in ckad-w8d6..."

REPLICAS=$(ssh controlplane 'kubectl get deploy prod-web-app -n ckad-w8d6 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
LABEL_ENV=$(ssh controlplane 'kubectl get deploy prod-web-app -n ckad-w8d6 -o jsonpath="{.metadata.labels.env}" 2>/dev/null || echo ""')

if [ "$REPLICAS" -eq 3 ] && [ "$LABEL_ENV" == "production" ]; then
  echo -e "[0;32m[PASS] Kustomize overlay applied successfully (prod-web-app, 3/3 Ready, env=production).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Ready replicas: $REPLICAS (expected 3) | Label env: '$LABEL_ENV' (expected production).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi