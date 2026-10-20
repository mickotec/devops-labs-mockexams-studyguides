#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D1: Multi-Container Pod in namespace ckad-w1d1..."

POD_STATUS=$(ssh controlplane 'kubectl get pod webapp-core -n ckad-w1d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY_COUNT=$(ssh controlplane 'kubectl get pod webapp-core -n ckad-w1d1 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')

if [ "$POD_STATUS" != "Running" ] || [ "$READY_COUNT" -ne 2 ]; then
  echo -e "\033[0;31m[FAIL] Pod webapp-core status is '$POD_STATUS' with $READY_COUNT/2 containers ready (expected 2/2 Running).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

LOG_CHECK=$(ssh controlplane 'kubectl exec webapp-core -c web-app -n ckad-w1d1 -- cat /var/log/app/heartbeat.log 2>/dev/null | head -n 1 || echo "Empty"')
if [ "$LOG_CHECK" == "Empty" ] || [ -z "$LOG_CHECK" ]; then
  echo -e "\033[0;31m[FAIL] /var/log/app/heartbeat.log not found or empty inside container web-app.\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

echo -e "\033[0;32m[PASS] Multi-container pod webapp-core running with shared volume and 2/2 containers ready.\033[0m"
echo "Final Score: 1/1 (100%)"
exit 0