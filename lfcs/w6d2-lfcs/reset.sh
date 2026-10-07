#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d2-lfcs..."
sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store
echo "[✓] Reset complete."
