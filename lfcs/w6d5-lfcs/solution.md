# [LFCS W6D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create `/usr/local/bin/check-disk.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
df -hT > /var/tmp/disk_audit.txt
df -hP | awk '0+$5 >= 85 {print "WARNING: High disk utilization on "$1" ("$5")"}' >> /var/log/disk_alert.log || true
```
`sudo chmod 755 /usr/local/bin/check-disk.sh`
`sudo /usr/local/bin/check-disk.sh`
