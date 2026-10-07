#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d5-lfcs (Remote Filesystems: NFS & Storage Monitoring)..."
sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log
echo "[✓] Environment ready. Review tasks with: ./lab show w6d5-lfcs"
