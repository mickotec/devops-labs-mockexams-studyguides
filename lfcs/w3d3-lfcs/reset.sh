#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d3-lfcs..."
sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload
echo "[✓] Reset complete."
