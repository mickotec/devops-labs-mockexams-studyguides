#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d5-cka..."
ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
