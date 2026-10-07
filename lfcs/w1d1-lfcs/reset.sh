#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d1-lfcs..."
sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman
echo "[✓] Reset complete."
