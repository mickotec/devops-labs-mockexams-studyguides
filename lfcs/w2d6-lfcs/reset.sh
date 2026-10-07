#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d6-lfcs..."
sudo rm -rf /srv/repo /var/backups/repo.tar.gz
echo "[✓] Reset complete."
