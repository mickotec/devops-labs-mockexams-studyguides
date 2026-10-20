#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D1: Services & NodePort in ckad-w6d1..."

BACKEND_TYPE=$(ssh controlplane 'kubectl get svc backend-svc -n ckad-w6d1 -o jsonpath="{.spec.type}" 2>/dev/null || echo ""')
FRONTEND_TYPE=$(ssh controlplane 'kubectl get svc frontend-svc -n ckad-w6d1 -o jsonpath="{.spec.type}" 2>/dev/null || echo ""')
FRONTEND_NP=$(ssh controlplane 'kubectl get svc frontend-svc -n ckad-w6d1 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo 0')

if [ "$BACKEND_TYPE" == "ClusterIP" ] && [ "$FRONTEND_TYPE" == "NodePort" ] && [ "$FRONTEND_NP" -eq 30080 ]; then
  echo -e "[0;32m[PASS] backend-svc (ClusterIP) and frontend-svc (NodePort: 30080) created successfully.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] backend type: '$BACKEND_TYPE' | frontend type: '$FRONTEND_TYPE' | nodePort: $FRONTEND_NP[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi