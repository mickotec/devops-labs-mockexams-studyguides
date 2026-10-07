#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d1-cka..."
ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s/replicaset-broken.yaml
'
echo "[✓] Reset complete."
