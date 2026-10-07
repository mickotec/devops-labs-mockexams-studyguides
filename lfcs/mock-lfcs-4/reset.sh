#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-lfcs-4..."
sudo systemctl stop batch-worker.service 2>/dev/null || true
sudo systemctl disable batch-worker.service 2>/dev/null || true
sudo rm -rf /etc/systemd/system/batch.slice /etc/systemd/system/batch-worker.service /etc/sysctl.d/99-security.conf /usr/local/bin/system_backup.sh /etc/ld.so.conf.d/customlib.conf /opt/customlib /etc/auto.master.d/shares.autofs /etc/auto.shares /etc/sssd/sssd.conf /var/log/backup_sync.log
sudo systemctl daemon-reload
podman stop mock-backup-job 2>/dev/null || true
podman rm -f mock-backup-job 2>/dev/null || true
if [ -f /var/tmp/mock-lfcs-4/io.pid ]; then
    kill -9 $(cat /var/tmp/mock-lfcs-4/io.pid) 2>/dev/null || true
fi
sudo iptables -D INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT 2>/dev/null || true
sudo ip link del bond0 2>/dev/null || true
sudo ip link del veth-bond1 2>/dev/null || true
sudo ip link del veth-bond2 2>/dev/null || true
sudo ip link del dummy0.50 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo systemctl stop autofs 2>/dev/null || true
sudo umount -l /shares/docs 2>/dev/null || true
sudo systemctl start autofs 2>/dev/null || true
sudo quotaoff /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo umount /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo lvremove -f /dev/mock-vg4/mock-striped 2>/dev/null || true
sudo vgremove -f mock-vg4 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-4" | cut -d: -f1); do
    sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r tester-quota 2>/dev/null || true
sudo userdel -r temp-auditor 2>/dev/null || true
sudo rm -rf /var/tmp/mock-lfcs-4
echo "[✓] Reset complete."
