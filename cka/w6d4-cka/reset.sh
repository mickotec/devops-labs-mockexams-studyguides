#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d4-cka..."
ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
'
echo "[✓] Reset complete."
