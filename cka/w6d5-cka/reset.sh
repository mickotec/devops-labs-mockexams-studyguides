#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d5-cka..."
ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  rm -rf /opt/k8s/kustomize
'
echo "[✓] Reset complete."
