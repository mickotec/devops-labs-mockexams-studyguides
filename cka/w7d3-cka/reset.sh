#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d3-cka..."
ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
