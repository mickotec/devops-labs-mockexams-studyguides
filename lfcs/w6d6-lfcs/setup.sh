#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d6-lfcs (Week 6 Storage Mastery & LVM Drill)..."
sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit
sudo mkdir -p /mnt/secure_audit && sudo chmod 777 /mnt/secure_audit
dd if=/dev/zero of=/var/tmp/m6_backing.img bs=1M count=300 >/dev/null 2>&1
sudo losetup /dev/loop93 /var/tmp/m6_backing.img
sudo pvcreate /dev/loop93 >/dev/null 2>&1
echo "[✓] Environment ready. Review tasks with: ./lab show w6d6-lfcs"
