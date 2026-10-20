#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D3: Ambassador Pattern in ckad-w3d3-apps..."

PHASE=$(ssh controlplane 'kubectl get pod client-ambassador -n ckad-w3d3-apps -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
LOG=$(ssh controlplane 'kubectl exec client-ambassador -c client -n ckad-w3d3-apps -- cat /tmp/proxy.log 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [[ "$LOG" =~ "AMBASSADOR_CONNECTED" ]]; then
  echo -e "[0;32m[PASS] Client successfully accessed remote database through localhost ambassador proxy.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE | Proxy log: '$LOG'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi