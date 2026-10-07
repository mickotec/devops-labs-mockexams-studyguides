#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d4-cka (DaemonSets & Static Pods Architecture)..."
ssh controlplane '
  kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d4-ds
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d4-cka"
