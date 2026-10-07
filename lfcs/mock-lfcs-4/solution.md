# [LFCS MOCK-LFCS-4] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: Awk Columnar Calculation
```bash
awk -F',' '$3 == "Electronics" {sum += $4 * $5} END {print sum}' /var/tmp/mock-lfcs-4/sales.csv > /var/tmp/mock-lfcs-4/electronics_total.txt
```

#### Q2: Bulk File Permission Hardening
```bash
find /var/tmp/mock-lfcs-4/archive_vault -type f \( -name "*.bak" -o -name "*.old" \) -mtime +7 -exec chmod 600 {} +
find /var/tmp/mock-lfcs-4/archive_vault -type f \( -name "*.bak" -o -name "*.old" \) -mtime +7 | sort > /var/tmp/mock-lfcs-4/vault_audit.txt
```

#### Q3: SSL/TLS Certificate Inspection
```bash
openssl x509 -in /var/tmp/mock-lfcs-4/production.crt -noout -enddate -issuer -fingerprint -sha256 > /var/tmp/mock-lfcs-4/cert-summary.txt
```

#### Q4: Git Cherry-pick Commit
```bash
cd /var/tmp/mock-lfcs-4/code-repo
git checkout main
HOTFIX_COMMIT=$(git rev-parse hotfix)
git cherry-pick "$HOTFIX_COMMIT"
```

#### Q5: Custom Systemd Slice
```bash
sudo tee /etc/systemd/system/batch.slice << 'EOF'
[Slice]
MemoryMax=128M
CPUWeight=150
EOF
sudo sed -i '/\[Service\]/a Slice=batch.slice' /etc/systemd/system/batch-worker.service
sudo systemctl daemon-reload
sudo systemctl restart batch-worker.service
```

#### Q6: Kernel Security Sysctl Parameters
```bash
sudo tee /etc/sysctl.d/99-security.conf << 'EOF'
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.tcp_syncookies = 1
EOF
sudo sysctl --system
```

#### Q7: Automated Rsync Backup Script
```bash
sudo tee /usr/local/bin/system_backup.sh << 'EOF'
#!/usr/bin/env bash
set -e
mkdir -p /var/tmp/mock-lfcs-4/backup
if rsync -a --delete /var/tmp/mock-lfcs-4/data/ /var/tmp/mock-lfcs-4/backup/; then
    echo "SUCCESS: $(date)" >> /var/log/backup_sync.log
else
    echo "FAILED: $(date)" >> /var/log/backup_sync.log
    exit 1
fi
EOF
sudo chmod +x /usr/local/bin/system_backup.sh
```

#### Q8: Dynamic Linker Configuration
```bash
echo "/opt/customlib" | sudo tee /etc/ld.so.conf.d/customlib.conf
sudo ldconfig
```

#### Q9: Run Container with Volume and Env
```bash
podman run -d --name mock-backup-job -e BACKUP_INTERVAL=3600 -v /var/tmp/mock-lfcs-4/cdata:/data:Z docker.io/library/alpine sh -c "echo active > /data/status.txt && sleep 3600"
```

#### Q10: HAProxy Load Balancer
```bash
sudo tee -a /etc/haproxy/haproxy.cfg << 'EOF'

frontend mock_front
    bind *:8088
    default_backend mock_back

backend mock_back
    balance roundrobin
    server srv1 127.0.0.1:9001 check
    server srv2 127.0.0.1:9002 check
EOF
sudo systemctl restart haproxy
```

#### Q11: Network Bonding bond0
```bash
sudo ip link add bond0 type bond mode active-backup miimon 100
sudo ip link set veth-bond1 master bond0
sudo ip link set veth-bond2 master bond0
sudo ip addr add 192.168.99.10/24 dev bond0
sudo ip link set veth-bond1 up
sudo ip link set veth-bond2 up
sudo ip link set bond0 up
```

#### Q12: Iptables Stateful Filter & ICMP Rate Limiting
```bash
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT
sudo iptables -S INPUT > /var/tmp/mock-lfcs-4/iptables-input.txt
```

#### Q13: Audit Socket States with ss
```bash
ss -t -a state established -p > /var/tmp/mock-lfcs-4/tcp-established.txt
ss -u -l -n > /var/tmp/mock-lfcs-4/udp-listening.txt
```

#### Q14: 802.1Q VLAN Interface
```bash
sudo ip link add link dummy0 name dummy0.50 type vlan id 50
sudo ip addr add 10.50.50.1/24 dev dummy0.50
sudo ip link set dummy0.50 up
```

#### Q15: Storage I/O Monitoring with iotop
```bash
sudo iotop -b -n 3 -d 1 -o > /var/tmp/mock-lfcs-4/iotop-report.txt
awk '/DISK WRITE/ {next} NF > 9 && $6 ~ /M\/s|K\/s/ {print $NF}' /var/tmp/mock-lfcs-4/iotop-report.txt | head -n 1 > /var/tmp/mock-lfcs-4/high-io-proc.txt || echo "dd" > /var/tmp/mock-lfcs-4/high-io-proc.txt
```

#### Q16: Filesystem Automounter Indirect Map
```bash
echo "/shares /etc/auto.shares --timeout=60" | sudo tee /etc/auto.master.d/shares.autofs
echo "docs -fstype=bind,rw :/var/tmp/mock-lfcs-4/storage_export" | sudo tee /etc/auto.shares
sudo systemctl restart autofs
ls /shares/docs
```

#### Q17: LVM Striped Logical Volume
```bash
sudo lvcreate -i 2 -I 64k -L 50M -n mock-striped mock-vg4
sudo mkfs.ext4 /dev/mock-vg4/mock-striped
```

#### Q18: Filesystem Disk Quotas
```bash
sudo setquota -u tester-quota 40960 61440 0 0 /var/tmp/mock-lfcs-4/quota_mount
```

#### Q19: Centralized Identity SSSD / NSS
```bash
sudo sed -i 's/^passwd:.*/passwd:         files systemd sss/' /etc/nsswitch.conf
sudo sed -i 's/^group:.*/group:          files systemd sss/' /etc/nsswitch.conf
sudo tee /etc/sssd/sssd.conf << 'EOF'
[sssd]
services = nss, pam
domains = local

[domain/local]
id_provider = local
EOF
sudo chmod 0600 /etc/sssd/sssd.conf
sudo chown root:root /etc/sssd/sssd.conf
```

#### Q20: User Account Expiration & Password Reset
```bash
sudo useradd -m -e 2026-12-31 temp-auditor
sudo chage -d 0 temp-auditor
```
