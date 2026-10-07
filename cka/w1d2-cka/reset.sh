#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d2-cka..."
ssh controlplane 'sudo rm -rf /opt/backup'
echo "[✓] Reset complete."
