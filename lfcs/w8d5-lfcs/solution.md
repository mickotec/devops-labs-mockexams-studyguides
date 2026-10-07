# [LFCS W8D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Systemd service and timer:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.service
[Unit]
Description=Clean Temporary Cache Files

[Service]
Type=oneshot
ExecStart=/bin/sh -c "/bin/rm -rf /tmp/mock_cache_*"
EOF'

sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.timer
[Unit]
Description=Timer for Clean Temporary Cache Files

[Timer]
OnCalendar=*:0/10
Persistent=true

[Install]
WantedBy=timers.target
EOF'

sudo systemctl daemon-reload
sudo systemctl enable --now tmp_cleanup.timer
```

2. Process limits:
```bash
sudo bash -c 'cat << "EOF" > /etc/security/limits.d/99-student-limits.conf
student soft nofile 65535
student hard nofile 65535
student soft nproc 2048
student hard nproc 2048
EOF'
```

3. Dummy interface:
```bash
sudo ip link add net-speed0 type dummy
sudo ip link set mtu 1400 net-speed0
sudo ip addr add 10.99.1.1/24 dev net-speed0
sudo ip link set net-speed0 up
```

4. Logrotate:
```bash
sudo bash -c 'cat << "EOF" > /etc/logrotate.d/mock4_logs
/var/log/mock4.log {
    daily
    rotate 4
    compress
    missingok
    notifempty
}
EOF'
sudo logrotate -d /etc/logrotate.d/mock4_logs
```
