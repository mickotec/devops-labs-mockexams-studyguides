#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d2-cka..."
ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true'
echo "[✓] Reset complete."
