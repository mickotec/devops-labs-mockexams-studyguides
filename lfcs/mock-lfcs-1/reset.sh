#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-lfcs-1..."
sudo systemctl stop mock-monitor.service 2>/dev/null || true
sudo systemctl disable mock-monitor.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/mock-monitor.service /usr/local/bin/mock_monitor.sh
sudo systemctl daemon-reload
sudo swapoff /var/tmp/mock-lfcs-1/swapfile 2>/dev/null || true
sudo umount /var/tmp/mock-lfcs-1/lvm-mount 2>/dev/null || true
sudo lvremove -f /dev/mock-vg/mock-lv 2>/dev/null || true
sudo vgremove -f mock-vg 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-1" | cut -d: -f1); do
  sudo losetup -d "$l" 2>/dev/null || true
done
docker rm -f mock-web 2>/dev/null || podman rm -f mock-web 2>/dev/null || true
sudo userdel -r devops 2>/dev/null || true
sudo userdel -r tester 2>/dev/null || true
sudo groupdel infrateam 2>/dev/null || true
crontab -u student -r 2>/dev/null || true
sudo sed -i '/exam.local/d' /etc/hosts
sudo sed -i '/student.*nofile/d' /etc/security/limits.conf
sudo rm -rf /var/tmp/mock-lfcs-1 /etc/sysctl.d/99-swappiness.conf /etc/ssh/sshd_config.d/99-hardening.conf
echo "[✓] Reset complete."
