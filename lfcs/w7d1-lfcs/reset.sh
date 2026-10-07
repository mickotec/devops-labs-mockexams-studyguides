#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d1-lfcs..."
sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log
echo "[✓] Reset complete."
