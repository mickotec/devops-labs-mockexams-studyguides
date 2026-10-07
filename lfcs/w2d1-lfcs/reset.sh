#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d1-lfcs..."
sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt
echo "[✓] Reset complete."
