#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d1-lfcs..."
if [ -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub.bak /etc/default/grub
  sudo update-grub
fi
sudo rm -f /var/tmp/boot_diagnostic.txt
echo "[✓] Reset complete."
