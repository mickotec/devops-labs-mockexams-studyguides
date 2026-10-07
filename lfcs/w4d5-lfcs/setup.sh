#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d5-lfcs (Bash Automation & Maintenance Scripting)..."
sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log
echo "[✓] Environment ready. Review tasks with: ./lab show w4d5-lfcs"
