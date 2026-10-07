#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d6-lfcs..."
sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit
echo "[✓] Reset complete."
