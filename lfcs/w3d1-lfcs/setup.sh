#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d1-lfcs (Linux Boot Architecture & GRUB2)..."
sudo rm -f /var/tmp/boot_diagnostic.txt
if [ ! -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub /etc/default/grub.bak
fi
echo "[✓] Environment ready. Review tasks with: ./lab show w3d1-lfcs"
