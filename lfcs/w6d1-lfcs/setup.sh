#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d1-lfcs (Storage Partitions (MBR vs GPT) & Swap)..."
sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab
echo "[✓] Environment ready. Review tasks with: ./lab show w6d1-lfcs"
