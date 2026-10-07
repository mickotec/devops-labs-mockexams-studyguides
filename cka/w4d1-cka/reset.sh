#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d1-cka..."
ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
