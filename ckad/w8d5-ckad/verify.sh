#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D5: Helm Release in ckad-w8d5..."

HELM_STATUS=$(ssh controlplane 'helm list -n ckad-w8d5 -q 2>/dev/null | grep "^frontend-app$" || echo ""')
REPLICAS=$(ssh controlplane 'kubectl get deploy frontend-app -n ckad-w8d5 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')

if [ -n "$HELM_STATUS" ] && [ "$REPLICAS" -eq 3 ]; then
  echo -e "\033[0;32m[PASS] Helm release frontend-app deployed with replicaCount=3 (3/3 Ready).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Helm status: '''$HELM_STATUS''' | Ready replicas: $REPLICAS (expected 3).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi