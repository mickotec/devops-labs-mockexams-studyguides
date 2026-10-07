#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d5-lfcs..."
sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log
echo "[✓] Reset complete."
