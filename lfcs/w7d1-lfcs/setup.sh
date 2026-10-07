#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d1-lfcs (Linux Networking Configuration (IP & Routing))..."
sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log
echo "[✓] Environment ready. Review tasks with: ./lab show w7d1-lfcs"
