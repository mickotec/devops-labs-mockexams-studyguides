#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-lfcs-4 (LFCS Full-Scale Timed Mock Exam 4 (Benchmark))..."
sudo rm -rf /var/tmp/mock-lfcs-4 /etc/systemd/system/batch.slice /etc/systemd/system/batch-worker.service /etc/sysctl.d/99-security.conf /usr/local/bin/system_backup.sh /etc/ld.so.conf.d/customlib.conf /opt/customlib /etc/auto.master.d/shares.autofs /etc/auto.shares /etc/sssd/sssd.conf
sudo mkdir -p /var/tmp/mock-lfcs-4/archive_vault /var/tmp/mock-lfcs-4/code-repo /var/tmp/mock-lfcs-4/data /var/tmp/mock-lfcs-4/cdata /var/tmp/mock-lfcs-4/storage_export /var/tmp/mock-lfcs-4/quota_mount /opt/customlib
sudo chown -R student:student /var/tmp/mock-lfcs-4

# Q1 sales.csv
cat << 'EOF' > /var/tmp/mock-lfcs-4/sales.csv
ID,Product,Department,Price,Quantity
101,Monitor,Electronics,150,2
102,Desk,Furniture,300,1
103,Keyboard,Electronics,50,4
104,Chair,Furniture,120,3
105,Mouse,Electronics,25,4
EOF

# Q2 archive vault files
touch -d "10 days ago" /var/tmp/mock-lfcs-4/archive_vault/old_backup.bak
touch -d "12 days ago" /var/tmp/mock-lfcs-4/archive_vault/legacy_data.old
touch -d "2 days ago" /var/tmp/mock-lfcs-4/archive_vault/recent.bak
touch -d "15 days ago" /var/tmp/mock-lfcs-4/archive_vault/notes.txt
chmod 644 /var/tmp/mock-lfcs-4/archive_vault/*

# Q3 production.crt
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/prod.key -out /var/tmp/mock-lfcs-4/production.crt -subj "/CN=prod.internal/O=EnterpriseCorp/OU=IT" 2>/dev/null || true
rm -f /tmp/prod.key

# Q4 code-repo with hotfix branch
git -C /var/tmp/mock-lfcs-4/code-repo init -b main 2>/dev/null || (git -C /var/tmp/mock-lfcs-4/code-repo init && git -C /var/tmp/mock-lfcs-4/code-repo checkout -b main)
echo "base codebase" > /var/tmp/mock-lfcs-4/code-repo/main.py
git -C /var/tmp/mock-lfcs-4/code-repo add main.py
git -C /var/tmp/mock-lfcs-4/code-repo -c user.name="LFCS Admin" -c user.email="admin@lfcs.local" commit -m "Initial commit" 2>/dev/null || true
git -C /var/tmp/mock-lfcs-4/code-repo checkout -b hotfix 2>/dev/null || true
echo "security patch applied" >> /var/tmp/mock-lfcs-4/code-repo/main.py
git -C /var/tmp/mock-lfcs-4/code-repo add main.py
git -C /var/tmp/mock-lfcs-4/code-repo -c user.name="Security Team" -c user.email="sec@lfcs.local" commit -m "HOTFIX: fix buffer overflow" 2>/dev/null || true
git -C /var/tmp/mock-lfcs-4/code-repo checkout main 2>/dev/null || true

# Q5 batch-worker service
sudo tee /etc/systemd/system/batch-worker.service << 'EOF'
[Unit]
Description=Batch Worker Service
[Service]
Type=simple
ExecStart=/usr/bin/sleep infinity
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now batch-worker.service 2>/dev/null || true

# Q7 backup data
echo "data file 1" > /var/tmp/mock-lfcs-4/data/file1.txt
echo "data file 2" > /var/tmp/mock-lfcs-4/data/file2.txt

# Q8 dynamic shared library
sudo cp /usr/lib/x86_64-linux-gnu/libc.so.6 /opt/customlib/libcustom.so 2>/dev/null || sudo touch /opt/customlib/libcustom.so

# Q10 HAProxy backends on 9001 and 9002
(python3 -m http.server 9001 &>/dev/null) &
(python3 -m http.server 9002 &>/dev/null) &

# Q11 bonding slave interfaces
sudo modprobe bonding 2>/dev/null || true
sudo ip link del bond0 2>/dev/null || true
sudo ip link del veth-bond1 2>/dev/null || true
sudo ip link del veth-bond2 2>/dev/null || true
sudo ip link add veth-bond1 type dummy 2>/dev/null || true
sudo ip link add veth-bond2 type dummy 2>/dev/null || true

# Q14 dummy0 interface for VLAN
sudo modprobe 8021q 2>/dev/null || true
sudo modprobe dummy 2>/dev/null || true
sudo ip link del dummy0.50 2>/dev/null || true
sudo ip link add dummy0 type dummy 2>/dev/null || true
sudo ip link set dummy0 up 2>/dev/null || true

# Q15 background disk activity
(while true; do dd if=/dev/zero of=/var/tmp/mock-lfcs-4/io_burn bs=1M count=10 oflag=direct 2>/dev/null; sleep 0.2; done) &
echo $! > /var/tmp/mock-lfcs-4/io.pid

# Q16 storage export
echo "policy content" > /var/tmp/mock-lfcs-4/storage_export/policy.pdf

# Q17 LVM striped VG
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/pv1.img bs=1M count=40 2>/dev/null || true
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/pv2.img bs=1M count=40 2>/dev/null || true
L1=$(sudo losetup -f --show /var/tmp/mock-lfcs-4/pv1.img 2>/dev/null || true)
L2=$(sudo losetup -f --show /var/tmp/mock-lfcs-4/pv2.img 2>/dev/null || true)
if [ -n "$L1" ] && [ -n "$L2" ]; then
    sudo pvcreate "$L1" "$L2" 2>/dev/null || true
    sudo vgcreate mock-vg4 "$L1" "$L2" 2>/dev/null || true
fi

# Q18 user tester-quota & quota image
sudo userdel -r tester-quota 2>/dev/null || true
sudo useradd -m tester-quota 2>/dev/null || true
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/quota.img bs=1M count=100 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-4/quota.img 2>/dev/null || true
sudo mount -o loop,usrquota /var/tmp/mock-lfcs-4/quota.img /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo quotacheck -cum /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo quotaon -u /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true

# Q20 user temp-auditor clean
sudo userdel -r temp-auditor 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show mock-lfcs-4"
