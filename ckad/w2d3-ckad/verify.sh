#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D3: ConfigMaps as Volumes in ckad-w2d3..."

PHASE=$(ssh controlplane 'kubectl get pod nginx-custom-port -n ckad-w2d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESP=$(ssh controlplane 'kubectl exec nginx-custom-port -n ckad-w2d3 -- wget -qO- 127.0.0.1:8088 2>/dev/null || echo "Failed"')

if [ "$PHASE" == "Running" ] && [[ "$RESP" =~ "CUSTOM-PORT-OK" ]]; then
  echo -e "[0;32m[PASS] Pod nginx-custom-port successfully loaded ConfigMap volume on port 8088.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: '$PHASE' | Curl Response: '$RESP' (expected CUSTOM-PORT-OK).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi