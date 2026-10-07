#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d3-lfcs (Logical Volume Management (LVM) Architecture)..."
sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data
sudo mkdir -p /mnt/orders_data && sudo chmod 777 /mnt/orders_data
dd if=/dev/zero of=/var/tmp/lvm_backing.img bs=1M count=250 >/dev/null 2>&1
sudo losetup /dev/loop91 /var/tmp/lvm_backing.img
echo "[✓] Environment ready. Review tasks with: ./lab show w6d3-lfcs"
