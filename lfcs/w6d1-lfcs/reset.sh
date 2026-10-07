#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d1-lfcs..."
sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab
echo "[✓] Reset complete."
