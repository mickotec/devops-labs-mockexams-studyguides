#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d1-cka..."
ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
