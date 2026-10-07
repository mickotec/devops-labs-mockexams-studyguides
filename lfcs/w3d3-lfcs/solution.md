# [LFCS W3D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create script `/usr/local/bin/worker-daemon.sh`:
```bash
#!/usr/bin/env bash
while true; do
  echo "Worker ping: $(date)" >> /var/log/worker-daemon.log
  sleep 3
done
```
`sudo chmod 755 /usr/local/bin/worker-daemon.sh`

2. Create `/etc/systemd/system/worker-daemon.service`:
```ini
[Unit]
Description=Worker Daemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/worker-daemon.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
`sudo systemctl daemon-reload`
`sudo systemctl enable --now worker-daemon.service`
