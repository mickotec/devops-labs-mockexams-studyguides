# [LFCS W3D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Set default target:
`sudo systemctl set-default multi-user.target`

2. Create `/etc/systemd/system/maintenance.target`:
```ini
[Unit]
Description=Maintenance Mode Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes
```
`sudo systemctl daemon-reload`

3. Save status:
`systemctl get-default > /var/tmp/default_target.txt`
