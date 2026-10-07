#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d4-lfcs..."
sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store
echo "[✓] Reset complete."
