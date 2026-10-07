#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d3-lfcs..."
sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true
echo "[✓] Reset complete."
