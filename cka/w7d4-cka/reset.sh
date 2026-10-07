#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d4-cka..."
ssh controlplane '
  kubectl delete namespace w7d4-gw --grace-period=0 --force 2>/dev/null || true
  kubectl delete gatewayclass cluster-gateway-class 2>/dev/null || true
'
echo "[✓] Reset complete."
