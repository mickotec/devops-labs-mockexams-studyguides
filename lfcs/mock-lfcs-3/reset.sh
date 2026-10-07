#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-lfcs-3..."
sudo systemctl stop mock-worker.service 2>/dev/null || true
sudo systemctl disable mock-worker.service 2>/dev/null || true
sudo rm -rf /etc/systemd/system/mock-worker.service* /etc/modprobe.d/blacklist-cramfs.conf /usr/local/bin/reload_mock_app.sh /etc/nginx/conf.d/proxy-balance.conf /etc/auto.master.d/direct.autofs /etc/auto.direct /etc/sudoers.d/90-developer
sudo systemctl daemon-reload
podman stop mock-web-c3 2>/dev/null || true
podman rm -f mock-web-c3 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8443 -j REDIRECT --to-ports 443 2>/dev/null || true
sudo ip route del 10.150.0.0/16 dev dummy0 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
sudo ip link del veth-br1 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo umount /mnt/secure-data 2>/dev/null || true
sudo sed -i '/secure-data/d' /etc/fstab
sudo rm -rf /mnt/secure-data
sudo systemctl stop autofs 2>/dev/null || true
sudo umount -l /mnt/auto-data 2>/dev/null || true
sudo systemctl start autofs 2>/dev/null || true
sudo lvremove -f /dev/mock-vg3/mock-thin 2>/dev/null || true
sudo lvremove -f /dev/mock-vg3/mock-pool 2>/dev/null || true
sudo vgremove -f mock-vg3 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-3" | cut -d: -f1); do
    sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r developer 2>/dev/null || true
sudo groupdel devteam 2>/dev/null || true
sudo rm -rf /var/tmp/mock-lfcs-3 /var/run/mock-app.pid
echo "[✓] Reset complete."
