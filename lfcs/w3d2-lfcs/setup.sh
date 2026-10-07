#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d2-lfcs (Systemd Targets & Runlevel Management)..."
sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload
echo "[✓] Environment ready. Review tasks with: ./lab show w3d2-lfcs"
