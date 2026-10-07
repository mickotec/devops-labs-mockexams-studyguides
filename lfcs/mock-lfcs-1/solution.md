# [LFCS MOCK-LFCS-1] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: Git Repo
```bash
mkdir -p /var/tmp/mock-lfcs-1/git-repo && cd /var/tmp/mock-lfcs-1/git-repo
git init -b main
echo "# Master Repo" > README.md
git add README.md && git commit -m "initial commit"
git checkout -b feature
echo "new feature" > feature.txt
git add feature.txt && git commit -m "add feature"
git checkout main
git merge feature
```

#### Q2: Custom Service
```bash
sudo tee /usr/local/bin/mock_monitor.sh << 'EOF'
#!/bin/bash
while true; do date >> /var/tmp/mock-lfcs-1/monitor.log; sleep 5; done
EOF
sudo chmod +x /usr/local/bin/mock_monitor.sh

sudo tee /etc/systemd/system/mock-monitor.service << 'EOF'
[Unit]
Description=Mock Monitor Service
[Service]
ExecStart=/usr/local/bin/mock_monitor.sh
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now mock-monitor.service
```

#### Q3: Find Large Files
```bash
find /var/tmp/mock-lfcs-1 -type f -mtime -7 -size +100k > /var/tmp/mock-lfcs-1/large-files.txt
```

#### Q4: SSL Cert Info
```bash
openssl x509 -in /var/tmp/mock-lfcs-1/exam.crt -noout -subject -issuer -dates > /var/tmp/mock-lfcs-1/cert-info.txt
```

#### Q5: Swappiness
```bash
echo "vm.swappiness = 10" | sudo tee /etc/sysctl.d/99-swappiness.conf
sudo sysctl --system
```

#### Q6: Cron Job
```bash
(crontab -u student -l 2>/dev/null; echo "30 2 * * 1-5 /bin/echo 'Cron job executed'") | crontab -u student -
```

#### Q7: Package Files
```bash
dpkg -L tar > /var/tmp/mock-lfcs-1/pkg-files.txt
```

#### Q8: Background Process PID
```bash
sleep 9999 &
echo $! > /var/tmp/mock-lfcs-1/sleep.pid
```

#### Q9: Run Container
```bash
docker run -d --name mock-web -p 8088:80 nginx:alpine || podman run -d --name mock-web -p 8088:80 nginx:alpine
```

#### Q10: Hosts Entry
```bash
echo "127.0.0.1 exam.local" | sudo tee -a /etc/hosts
```

#### Q11: Time Status
```bash
timedatectl status > /var/tmp/mock-lfcs-1/time-status.txt
```

#### Q12: Listening Ports
```bash
ss -tlpn > /var/tmp/mock-lfcs-1/listening-ports.txt
```

#### Q13: SSH Hardening Drop-in
```bash
sudo mkdir -p /etc/ssh/sshd_config.d
sudo tee /etc/ssh/sshd_config.d/99-hardening.conf << 'EOF'
PermitRootLogin no
MaxAuthTries 3
EOF
sudo sshd -t
```

#### Q14: Firewall Status
```bash
sudo ufw status verbose > /var/tmp/mock-lfcs-1/firewall-rules.txt || sudo iptables -L -n > /var/tmp/mock-lfcs-1/firewall-rules.txt
```

#### Q15: Ext4 Disk Image
```bash
dd if=/dev/zero of=/var/tmp/mock-lfcs-1/disk1.img bs=1M count=100
mkfs.ext4 -F /var/tmp/mock-lfcs-1/disk1.img
```

#### Q16 & Q17: LVM Setup & Extend
```bash
LOOP=$(sudo losetup -f --show /var/tmp/mock-lfcs-1/disk1.img)
sudo pvcreate $LOOP
sudo vgcreate mock-vg $LOOP
sudo lvcreate -L 50M -n mock-lv mock-vg
sudo mkfs.ext4 /dev/mock-vg/mock-lv
mkdir -p /var/tmp/mock-lfcs-1/lvm-mount
sudo mount /dev/mock-vg/mock-lv /var/tmp/mock-lfcs-1/lvm-mount
# Q17 extend
sudo lvextend -L 80M /dev/mock-vg/mock-lv
sudo resize2fs /dev/mock-vg/mock-lv
```

#### Q18: Swapfile
```bash
sudo dd if=/dev/zero of=/var/tmp/mock-lfcs-1/swapfile bs=1M count=64
sudo chmod 600 /var/tmp/mock-lfcs-1/swapfile
sudo mkswap /var/tmp/mock-lfcs-1/swapfile
sudo swapon /var/tmp/mock-lfcs-1/swapfile
```

#### Q19: Users, Group and ACL
```bash
sudo groupadd -g 3001 infrateam
sudo useradd -u 2001 -m devops
sudo useradd -u 2002 -m tester
sudo setfacl -m g:infrateam:rwx /var/tmp/mock-lfcs-1/shared
```

#### Q20: Limits & Password Aging
```bash
echo "student soft nofile 4096" | sudo tee -a /etc/security/limits.conf
echo "student hard nofile 4096" | sudo tee -a /etc/security/limits.conf
sudo chage -M 90 student
```
