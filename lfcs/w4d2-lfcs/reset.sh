#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d2-lfcs..."
sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true
echo "[✓] Reset complete."
