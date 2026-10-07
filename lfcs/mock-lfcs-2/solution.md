# [LFCS MOCK-LFCS-2] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: Sed Editing
```bash
sed -i 's/PORT = 8080/PORT = 9000/' /var/tmp/mock-lfcs-2/app.conf
sed -i '/DEBUG/d' /var/tmp/mock-lfcs-2/app.conf
sed -i '/\[app\]/a ENV = production' /var/tmp/mock-lfcs-2/app.conf
```

#### Q2: Syslog Pipeline
```bash
awk '{print $5}' /var/tmp/mock-lfcs-2/sample_syslog | sed 's/\[.*//' | sort | uniq -c | sort -nr | head -n 3 > /var/tmp/mock-lfcs-2/top_loggers.txt
```

#### Q3: Diff and Patch
```bash
diff -u /var/tmp/mock-lfcs-2/fileA /var/tmp/mock-lfcs-2/fileB > /var/tmp/mock-lfcs-2/patch.diff
patch /var/tmp/mock-lfcs-2/fileTarget < /var/tmp/mock-lfcs-2/patch.diff
```

#### Q4: Largest Files
```bash
sudo find /var/log -type f -exec ls -s {} + 2>/dev/null | sort -nr | head -n 3 > /var/tmp/mock-lfcs-2/largest_files.txt
```

#### Q5: Systemd Timer
```bash
sudo tee /etc/systemd/system/mock-cleanup.service << 'EOF'
[Unit]
Description=Mock Cleanup Service
[Service]
Type=oneshot
ExecStart=/bin/echo "cleanup run"
EOF

sudo tee /etc/systemd/system/mock-cleanup.timer << 'EOF'
[Unit]
Description=Mock Cleanup Timer
[Timer]
OnCalendar=*:0/15
Persistent=true
[Install]
WantedBy=timers.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now mock-cleanup.timer
```

#### Q6: Renice Process
```bash
sleep 600 &
PID=$!
sudo renice -n 15 -p $PID
ps -o pid,ni,comm -p $PID > /var/tmp/mock-lfcs-2/nice_proc.txt
```

#### Q7: Rsyslog Rule
```bash
echo "local5.* /var/log/custom-app.log" | sudo tee /etc/rsyslog.d/40-custom.conf
sudo systemctl restart rsyslog
```

#### Q8: Default Target
```bash
systemctl get-default > /var/tmp/mock-lfcs-2/boot-target.txt
```

#### Q9: Apt Pinning
```bash
sudo tee /etc/apt/preferences.d/pin-package << 'EOF'
Package: nginx
Pin: release *
Pin-Priority: 999
EOF
```

#### Q10: Dummy Interface
```bash
sudo ip link add dummy0 type dummy
sudo ip addr add 10.99.99.1/24 dev dummy0
sudo ip link set dummy0 up
```

#### Q11: IPTables Rule
```bash
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo iptables -L INPUT -n > /var/tmp/mock-lfcs-2/iptables.txt
```

#### Q12: SSH PID
```bash
ss -tlpn | grep ":22 " > /var/tmp/mock-lfcs-2/ssh-proc.txt
```

#### Q13: DNS Server
```bash
resolvectl status > /var/tmp/mock-lfcs-2/dns-server.txt || systemd-resolve --status > /var/tmp/mock-lfcs-2/dns-server.txt
```

#### Q14: Static Route
```bash
sudo ip route add 192.168.100.0/24 via 10.99.99.254 dev dummy0 onlink
```

#### Q15: LVM Snapshot
```bash
sudo lvcreate -s -L 20M -n data-snap /dev/mock-vg2/data-lv
```

#### Q16: Tune2fs
```bash
sudo tune2fs -m 1 /var/tmp/mock-lfcs-2/tunable.img
```

#### Q17: Fstab Entry
```bash
echo "/var/tmp/mock-lfcs-2/mnt-point /var/tmp/mock-lfcs-2/mnt-point none bind,noatime,nodev 0 0" | sudo tee -a /etc/fstab
```

#### Q18: Swap Space
```bash
sudo dd if=/dev/zero of=/var/tmp/mock-lfcs-2/swapfile2 bs=1M count=128
sudo chmod 600 /var/tmp/mock-lfcs-2/swapfile2
sudo mkswap /var/tmp/mock-lfcs-2/swapfile2
sudo swapon /var/tmp/mock-lfcs-2/swapfile2
```

#### Q19: Password Aging
```bash
sudo chage -M 60 -m 7 -W 14 student
```

#### Q20: Skeleton & New User
```bash
echo "export LAB_ENV=lfcs-certified" | sudo tee /etc/skel/.custom_profile
sudo useradd -m newhire
```
