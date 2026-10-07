#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d2-lfcs (Timed Mock Exam 1 (Strict Exam Conditions))..."
sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w8d2-lfcs"
