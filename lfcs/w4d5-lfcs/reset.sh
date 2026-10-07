#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d5-lfcs..."
sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log
echo "[✓] Reset complete."
