#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d4-cka..."
ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true'
echo "[✓] Reset complete."
