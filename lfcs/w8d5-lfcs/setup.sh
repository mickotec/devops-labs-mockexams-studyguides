#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d5-lfcs (Timed Mock Exam 4 & Final Speed Marathon)..."
sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w8d5-lfcs"
