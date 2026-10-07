#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d6-cka..."
ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
