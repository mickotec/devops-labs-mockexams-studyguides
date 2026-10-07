# [LFCS MOCK-LFCS-3] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: Web Server Error Log Parsing
```bash
awk '$9 ~ /^[45]/ {print $1}' /var/tmp/mock-lfcs-3/web_access.log | sort -u > /var/tmp/mock-lfcs-3/error_ips.txt
```

#### Q2: SSL CSR with SAN
```bash
openssl req -new -newkey rsa:2048 -nodes   -keyout /var/tmp/mock-lfcs-3/server.key   -out /var/tmp/mock-lfcs-3/server.csr   -subj "/CN=lfcs.local/O=MockCorp"   -addext "subjectAltName=DNS:lfcs.local,DNS:api.lfcs.local"
```

#### Q3: Multi-threaded Compressed Archive
```bash
XZ_OPT="-T0" tar -cJf /var/tmp/mock-lfcs-3/backup.tar.xz -C /var/tmp/mock-lfcs-3 source_data
cd /var/tmp/mock-lfcs-3 && sha256sum backup.tar.xz > backup.tar.xz.sha256
```

#### Q4: Git Annotated Tag and Release Branch
```bash
cd /var/tmp/mock-lfcs-3/git-app
git tag -a v1.2.0 -m "Production Release 1.2.0"
git checkout -b release-1.2 v1.2.0
```

#### Q5: Systemd Cgroup Resource Drop-in
```bash
sudo mkdir -p /etc/systemd/system/mock-worker.service.d
sudo tee /etc/systemd/system/mock-worker.service.d/limits.conf << 'EOF'
[Service]
MemoryMax=64M
CPUQuota=40%
EOF
sudo systemctl daemon-reload
sudo systemctl restart mock-worker.service
```

#### Q6: Kernel Module Blacklisting
```bash
sudo tee /etc/modprobe.d/blacklist-cramfs.conf << 'EOF'
blacklist cramfs
install cramfs /bin/true
EOF
sudo modprobe -r cramfs 2>/dev/null || true
```

#### Q7: Journalctl Diagnostic Log Extraction
```bash
journalctl --since "2026-01-01" -p err..emerg --no-pager > /var/tmp/mock-lfcs-3/system_errors.log
```

#### Q8: Graceful Process Reload Script
```bash
sudo tee /usr/local/bin/reload_mock_app.sh << 'EOF'
#!/usr/bin/env bash
if [ -f /var/run/mock-app.pid ]; then
    PID=$(cat /var/run/mock-app.pid)
    kill -HUP "$PID"
    echo "$(date) RELOAD SIGNAL SENT" >> /var/tmp/mock-lfcs-3/signal.log
fi
EOF
sudo chmod +x /usr/local/bin/reload_mock_app.sh
```

#### Q9: Run Container with Podman
```bash
podman run -d --name mock-web-c3 --restart always -p 8085:80 docker.io/library/nginx:alpine
```

#### Q10: Nginx Reverse Proxy Load Balancer
```bash
sudo tee /etc/nginx/conf.d/proxy-balance.conf << 'EOF'
upstream backend_nodes {
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
}

server {
    listen 8080;
    server_name _;

    location / {
        proxy_pass http://backend_nodes;
        proxy_set_header Host $host;
    }
}
EOF
sudo nginx -t && sudo systemctl restart nginx
```

#### Q11: Network Bridge Configuration
```bash
sudo ip link add br0 type bridge
sudo ip link set veth-br1 master br0
sudo ip addr add 192.168.50.1/24 dev br0
sudo ip link set veth-br1 up
sudo ip link set br0 up
```

#### Q12: Iptables NAT Port Redirection
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 8443 -j REDIRECT --to-ports 443
sudo iptables -t nat -L PREROUTING -n > /var/tmp/mock-lfcs-3/nat-rules.txt
```

#### Q13: Network Packet Capture with tcpdump
```bash
sudo tcpdump -i lo -c 5 -w /var/tmp/mock-lfcs-3/traffic.pcap tcp port 9999
```

#### Q14: Static Route with Metric
```bash
sudo ip route add 10.150.0.0/16 via 10.99.99.1 dev dummy0 metric 150 onlink
```

#### Q15: Storage Performance Monitoring
```bash
iostat -x -d 1 3 > /var/tmp/mock-lfcs-3/io-report.txt
sar -d 1 3 > /var/tmp/mock-lfcs-3/sar-disk.txt
```

#### Q16: Filesystem Automounter Direct Map
```bash
echo "/- /etc/auto.direct --timeout=60" | sudo tee /etc/auto.master.d/direct.autofs
echo "/mnt/auto-data -fstype=ext4,loop,rw :/var/tmp/mock-lfcs-3/auto.img" | sudo tee /etc/auto.direct
sudo systemctl restart autofs
ls /mnt/auto-data
```

#### Q17: LVM Thin Provisioning
```bash
sudo lvcreate -L 50M -T mock-vg3/mock-pool
sudo lvcreate -V 150M -T mock-vg3/mock-pool -n mock-thin
sudo mkfs.ext4 /dev/mock-vg3/mock-thin
```

#### Q18: Persistent Mount by UUID
```bash
UUID_VAL=$(sudo blkid -s UUID -o value /var/tmp/mock-lfcs-3/secure_store.img)
sudo mkdir -p /mnt/secure-data
echo "UUID=$UUID_VAL /mnt/secure-data ext4 loop,noexec,nosuid,nodev 0 0" | sudo tee -a /etc/fstab
sudo mount -a
```

#### Q19: Granular Sudoers File
```bash
echo "developer ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-developer
sudo chmod 0440 /etc/sudoers.d/90-developer
```

#### Q20: SGID and Sticky Bit Directory
```bash
sudo mkdir -p /var/tmp/mock-lfcs-3/team_collab/dropzone
sudo chown student:devteam /var/tmp/mock-lfcs-3/team_collab
sudo chmod 2775 /var/tmp/mock-lfcs-3/team_collab
sudo chmod 1777 /var/tmp/mock-lfcs-3/team_collab/dropzone
```
