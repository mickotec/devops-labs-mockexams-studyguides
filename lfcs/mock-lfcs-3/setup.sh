#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-lfcs-3 (LFCS Full-Scale Timed Mock Exam 3)..."
sudo rm -rf /var/tmp/mock-lfcs-3 /etc/systemd/system/mock-worker.service.d /etc/modprobe.d/blacklist-cramfs.conf /etc/nginx/conf.d/proxy-balance.conf /etc/auto.master.d/direct.autofs /etc/auto.direct /etc/sudoers.d/90-developer /var/run/mock-app.pid
sudo mkdir -p /var/tmp/mock-lfcs-3/source_data /var/tmp/mock-lfcs-3/git-app /mnt/secure-data
sudo chown -R student:student /var/tmp/mock-lfcs-3

# Q1 sample log
cat << 'EOF' > /var/tmp/mock-lfcs-3/web_access.log
192.168.1.10 - - [10/Nov/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 4523
192.168.1.50 - - [10/Nov/2026:10:00:05 +0000] "GET /admin HTTP/1.1" 403 342
10.0.0.12 - - [10/Nov/2026:10:01:10 +0000] "POST /api/v1/login HTTP/1.1" 500 523
172.16.0.5 - - [10/Nov/2026:10:01:25 +0000] "GET /nonexistent HTTP/1.1" 404 289
192.168.1.10 - - [10/Nov/2026:10:02:00 +0000] "GET /style.css HTTP/1.1" 200 1204
10.0.0.12 - - [10/Nov/2026:10:02:15 +0000] "GET /broken HTTP/1.1" 502 189
EOF

# Q3 sample source files
echo "Project source code file 1" > /var/tmp/mock-lfcs-3/source_data/module1.py
echo "Configuration parameters file 2" > /var/tmp/mock-lfcs-3/source_data/config.json

# Q4 sample git repo
git -C /var/tmp/mock-lfcs-3/git-app init -b main 2>/dev/null || (git -C /var/tmp/mock-lfcs-3/git-app init && git -C /var/tmp/mock-lfcs-3/git-app checkout -b main)
echo "print('App v1.0')" > /var/tmp/mock-lfcs-3/git-app/app.py
git -C /var/tmp/mock-lfcs-3/git-app add app.py
git -C /var/tmp/mock-lfcs-3/git-app -c user.name="LFCS Admin" -c user.email="admin@lfcs.local" commit -m "Initial commit v1.0" 2>/dev/null || true

# Q5 worker service
sudo tee /etc/systemd/system/mock-worker.service << 'EOF'
[Unit]
Description=Mock Worker Service
[Service]
Type=simple
ExecStart=/usr/bin/sleep infinity
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now mock-worker.service 2>/dev/null || true

# Q7 generate test error log
logger -p user.err "LFCS_MOCK3_CRITICAL_ERR system failure simulation" 2>/dev/null || true

# Q8 mock app daemon with trap
(trap 'echo "RELOAD_ACK" >> /var/tmp/mock-lfcs-3/app_ack.log' HUP; while true; do sleep 1; done) &
echo $! | sudo tee /var/run/mock-app.pid >/dev/null

# Q10 start minimal backends on 8081 and 8082
mkdir -p /var/tmp/mock-lfcs-3/b1 /var/tmp/mock-lfcs-3/b2
echo "Backend 1 Response" > /var/tmp/mock-lfcs-3/b1/index.html
echo "Backend 2 Response" > /var/tmp/mock-lfcs-3/b2/index.html
(cd /var/tmp/mock-lfcs-3/b1 && python3 -m http.server 8081 &>/dev/null) &
(cd /var/tmp/mock-lfcs-3/b2 && python3 -m http.server 8082 &>/dev/null) &

# Q11 dummy interface for bridge
sudo ip link del veth-br1 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
sudo ip link add veth-br1 type dummy 2>/dev/null || true

# Q14 dummy0 interface for routing
sudo modprobe dummy 2>/dev/null || true
sudo ip link add dummy0 type dummy 2>/dev/null || true
sudo ip addr add 10.99.99.1/24 dev dummy0 2>/dev/null || true
sudo ip link set dummy0 up 2>/dev/null || true

# Q16 autofs image
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/auto.img bs=1M count=40 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-3/auto.img 2>/dev/null || true
mkdir -p /tmp/tmp_auto
sudo mount -o loop /var/tmp/mock-lfcs-3/auto.img /tmp/tmp_auto 2>/dev/null || true
echo "autofs verification success" | sudo tee /tmp/tmp_auto/auto_test.txt >/dev/null
sudo umount /tmp/tmp_auto 2>/dev/null || true
rm -rf /tmp/tmp_auto

# Q17 thin storage image & VG
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/thin_storage.img bs=1M count=100 2>/dev/null || true
LOOP_THIN=$(sudo losetup -f --show /var/tmp/mock-lfcs-3/thin_storage.img 2>/dev/null || true)
if [ -n "$LOOP_THIN" ]; then
    sudo pvcreate "$LOOP_THIN" 2>/dev/null || true
    sudo vgcreate mock-vg3 "$LOOP_THIN" 2>/dev/null || true
fi

# Q18 secure store image
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/secure_store.img bs=1M count=50 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-3/secure_store.img 2>/dev/null || true

# Q19 user developer
sudo userdel -r developer 2>/dev/null || true
sudo useradd -m developer 2>/dev/null || true

# Q20 devteam group
sudo groupadd devteam 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show mock-lfcs-3"
