#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d2-lfcs (Filesystems & Boot Mounting (/etc/fstab))..."
sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store
sudo mkdir -p /mnt/data_store && sudo chmod 777 /mnt/data_store
dd if=/dev/zero of=/var/tmp/data_store.img bs=1M count=150 >/dev/null 2>&1
sudo losetup /dev/loop90 /var/tmp/data_store.img
echo "[✓] Environment ready. Review tasks with: ./lab show w6d2-lfcs"
