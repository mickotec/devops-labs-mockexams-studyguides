#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d3-cka..."
ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
