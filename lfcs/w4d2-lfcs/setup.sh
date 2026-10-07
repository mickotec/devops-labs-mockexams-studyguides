#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d2-lfcs (Task Scheduling with Cron and At)..."
sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w4d2-lfcs"
