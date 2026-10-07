#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d6-lfcs (Certification Gate Review & Readiness Audit)..."
sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh
echo "[✓] Environment ready. Review tasks with: ./lab show w8d6-lfcs"
