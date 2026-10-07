# [LFCS W2D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Large files:
```bash
find /var/log -type f -size +500k > /var/tmp/large_logs.txt
```

2. Recent configs:
```bash
find /etc -type f -mtime -7 -perm 644 > /var/tmp/recent_configs.txt
```

3. Locate query:
```bash
sudo updatedb && locate '/etc/systemd/*.conf' > /var/tmp/systemd_confs.txt
```
