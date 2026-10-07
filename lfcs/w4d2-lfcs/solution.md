# [LFCS W4D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. System crontab:
`echo "*/15 * * * * root /bin/echo "Sync executed at \$(date)" >> /var/log/sync-audit.log" | sudo tee /etc/cron.d/sync-audit`
`sudo chmod 644 /etc/cron.d/sync-audit`

2. User crontab:
`(crontab -u student -l 2>/dev/null; echo "30 3 * * * /bin/date >> /var/tmp/daily_timestamp.txt") | crontab -u student -`

3. At allow:
`echo "student" | sudo tee /etc/at.allow`
`sudo rm -f /etc/at.deny`
