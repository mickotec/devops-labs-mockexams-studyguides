#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d2-lfcs..."
sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true
echo "[✓] Reset complete."
