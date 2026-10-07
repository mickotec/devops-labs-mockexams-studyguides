#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d6-lfcs..."
sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true
echo "[✓] Reset complete."
