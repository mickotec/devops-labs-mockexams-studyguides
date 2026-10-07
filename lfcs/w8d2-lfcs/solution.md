# [LFCS W8D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. User & Group:
`sudo groupadd -g 2500 finance`
`sudo useradd -u 2500 -g finance -G finance -s /bin/bash -m auditor`

2. Directory Permissions:
`sudo mkdir -p /srv/finance`
`sudo chown root:finance /srv/finance`
`sudo chmod 2770 /srv/finance`

3. Cron job:
`echo "30 3 * * * root /bin/sync" | sudo tee /etc/cron.d/audit_sync`

4. Systemd unit:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/heartbeat.service
[Unit]
Description=Heartbeat Logger

[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo heartbeat >> /var/log/heartbeat.log"

[Install]
WantedBy=multi-user.target
EOF'
sudo systemctl daemon-reload
sudo systemctl enable --now heartbeat.service
```
