#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d2-lfcs..."
sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt
echo "[✓] Reset complete."
