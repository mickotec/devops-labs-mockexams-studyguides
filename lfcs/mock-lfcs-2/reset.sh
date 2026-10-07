#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-lfcs-2..."
sudo systemctl stop mock-cleanup.timer 2>/dev/null || true
sudo systemctl disable mock-cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/mock-cleanup.*
sudo systemctl daemon-reload
sudo ip route del 192.168.100.0/24 dev dummy0 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo swapoff /var/tmp/mock-lfcs-2/swapfile2 2>/dev/null || true
sudo lvremove -f /dev/mock-vg2/data-snap 2>/dev/null || true
sudo lvremove -f /dev/mock-vg2/data-lv 2>/dev/null || true
sudo vgremove -f mock-vg2 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-2" | cut -d: -f1); do
  sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r newhire 2>/dev/null || true
sudo rm -f /etc/skel/.custom_profile
sudo sed -i '/mnt-point/d' /etc/fstab
sudo rm -rf /var/tmp/mock-lfcs-2 /etc/rsyslog.d/40-custom.conf /etc/apt/preferences.d/pin-package
echo "[✓] Reset complete."
