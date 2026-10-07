#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d6-cka..."
ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-export.yaml
'
echo "[✓] Reset complete."
