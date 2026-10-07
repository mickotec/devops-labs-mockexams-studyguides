#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d3-lfcs..."
sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data
echo "[✓] Reset complete."
