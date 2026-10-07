# [LFCS W4D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Query error logs:
`journalctl -b -p err..emerg --no-pager > /var/tmp/system_errors.log`

2. SSH service logs:
`journalctl -u ssh -n 20 --no-pager > /var/tmp/ssh_service.log`

3. Journal disk usage:
`journalctl --disk-usage > /var/tmp/journal_usage.txt`
