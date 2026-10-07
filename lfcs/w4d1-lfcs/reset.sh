#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d1-lfcs..."
sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt
echo "[✓] Reset complete."
