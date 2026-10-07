# [LFCS W4D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Script `/usr/local/bin/log-auditor.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
mkdir -p /var/log/audit
journalctl --since "2 hours ago" -p err..emerg --no-pager > /var/log/audit/recent_errors.log 2>/dev/null || true
COUNT=$(wc -l < /var/log/audit/recent_errors.log || echo 0)
echo "[$(date)] Found $COUNT errors" >> /var/log/audit/summary.log
```
`sudo chmod 755 /usr/local/bin/log-auditor.sh`

2. Cron:
`echo "*/30 * * * * root /usr/local/bin/log-auditor.sh" | sudo tee /etc/cron.d/log-audit`
`sudo chmod 644 /etc/cron.d/log-audit`

3. Hold package:
`sudo apt-mark hold tar`
