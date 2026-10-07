#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d5-cka..."
ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-cache.yaml
'
echo "[✓] Reset complete."
