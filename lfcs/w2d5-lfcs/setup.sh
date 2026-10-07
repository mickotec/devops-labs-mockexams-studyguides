#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d5-lfcs (Archiving, Compression & Remote Backups)..."
sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w2d5-lfcs"
