#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d5-lfcs..."
sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt
echo "[✓] Reset complete."
