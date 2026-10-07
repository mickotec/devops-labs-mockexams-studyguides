#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d6-cka..."
ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
'
echo "[✓] Reset complete."
