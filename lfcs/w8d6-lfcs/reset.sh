#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d6-lfcs..."
sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh
echo "[✓] Reset complete."
