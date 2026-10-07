#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d3-cka..."
ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s-manifests
'
echo "[✓] Reset complete."
