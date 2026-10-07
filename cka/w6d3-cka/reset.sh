#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d3-cka..."
ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
