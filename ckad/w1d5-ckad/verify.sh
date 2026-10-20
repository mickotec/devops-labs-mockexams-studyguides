#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D5: Cross-Namespace DNS in ckad-w1d5-frontend..."

PHASE=$(ssh controlplane 'kubectl get pod query-client -n ckad-w1d5-frontend -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
LOG=$(ssh controlplane 'kubectl exec query-client -n ckad-w1d5-frontend -- cat /tmp/conn.log 2>/dev/null || echo "Missing"')

if [ "$PHASE" == "Running" ] && [[ "$LOG" =~ "CONNECTION_SUCCESS" ]]; then
  echo -e "\033[0;32m[PASS] query-client successfully reached db-service across namespaces via CoreDNS.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] query-client phase: '$PHASE' | conn.log: '$LOG'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi