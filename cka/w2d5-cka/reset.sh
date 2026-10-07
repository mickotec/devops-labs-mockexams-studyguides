#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d5-cka..."
ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'
echo "[✓] Reset complete."
