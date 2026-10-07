# [LFCS W3D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Cache cleaner timer:
`/etc/systemd/system/cache-cleaner.service`:
```ini
[Unit]
Description=Cache Cleaner
[Service]
Type=oneshot
ExecStart=/usr/bin/find /var/tmp/cache -type f -mtime +7 -delete
```
`/etc/systemd/system/cache-cleaner.timer`:
```ini
[Unit]
Description=Hourly Cache Cleaner Timer
[Timer]
OnCalendar=hourly
Persistent=true
[Install]
WantedBy=timers.target
```
`sudo systemctl daemon-reload && sudo systemctl enable --now cache-cleaner.timer`

2. Fix `/etc/systemd/system/payment-bridge.service`:
Change `ExecStart=/usr/local/bin/payment-bridge.sh`
`sudo systemctl daemon-reload && sudo systemctl restart payment-bridge.service`

3. Create `/etc/security/limits.d/50-worker.conf`:
```
student hard nofile 4096
student hard nproc 2048
```
