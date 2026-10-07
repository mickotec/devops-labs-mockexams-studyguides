#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d3-cka..."
ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true'
echo "[✓] Reset complete."
