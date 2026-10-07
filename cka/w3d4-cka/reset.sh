#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d4-cka..."
ssh controlplane '
kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
kubectl delete pod node02-telemetry-node02 --force --grace-period=0 2>/dev/null || true
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
echo "[✓] Reset complete."
