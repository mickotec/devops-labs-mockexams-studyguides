#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d4-lfcs (Dynamic LVM Volume Expansion)..."
sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store
sudo mkdir -p /mnt/expand_store && sudo chmod 777 /mnt/expand_store
dd if=/dev/zero of=/var/tmp/expand_backing.img bs=1M count=350 >/dev/null 2>&1
sudo losetup /dev/loop92 /var/tmp/expand_backing.img
sudo pvcreate /dev/loop92 >/dev/null 2>&1
sudo vgcreate vg_expand /dev/loop92 >/dev/null 2>&1
sudo lvcreate -L 100M -n lv_store vg_expand >/dev/null 2>&1
sudo mkfs.ext4 /dev/vg_expand/lv_store >/dev/null 2>&1
sudo mount /dev/vg_expand/lv_store /mnt/expand_store
echo "[✓] Environment ready. Review tasks with: ./lab show w6d4-lfcs"
