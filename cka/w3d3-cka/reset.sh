#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d3-cka..."
ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
