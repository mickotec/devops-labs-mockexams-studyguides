#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d5-lfcs..."
sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true
echo "[✓] Reset complete."
