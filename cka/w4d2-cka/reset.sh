#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d2-cka..."
ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/settings.json
'
echo "[✓] Reset complete."
