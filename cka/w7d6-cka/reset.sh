#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d6-cka..."
ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  rm -f /tmp/tls.key /tmp/tls.crt
'
echo "[✓] Reset complete."
