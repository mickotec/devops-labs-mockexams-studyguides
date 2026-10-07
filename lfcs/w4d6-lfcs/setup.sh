#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d6-lfcs (Week 4 System Automation & Maintenance Triathlon)..."
sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w4d6-lfcs"
