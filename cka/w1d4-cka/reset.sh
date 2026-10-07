#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d4-cka..."
ssh controlplane 'kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true'
echo "[✓] Reset complete."
