#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d4-cka..."
ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
