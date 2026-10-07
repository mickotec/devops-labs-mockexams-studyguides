#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d3-lfcs (Creating & Managing Systemd Services)..."
sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload
echo "[✓] Environment ready. Review tasks with: ./lab show w3d3-lfcs"
