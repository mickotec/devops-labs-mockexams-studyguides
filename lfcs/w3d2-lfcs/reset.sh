#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d2-lfcs..."
sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload
echo "[✓] Reset complete."
