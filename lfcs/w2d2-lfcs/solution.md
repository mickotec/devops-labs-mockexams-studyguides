# [LFCS W2D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Extract IPs:
```bash
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/tmp/auth_sample.log | sort -u > /var/tmp/auth_ips.txt
```

2. Filter PAM rules:
```bash
grep -riE 'pam|login' /etc/security/ | grep -vE '^[^:]+:[[:space:]]*#' > /var/tmp/pam_rules.txt
```

3. Count failure lines:
```bash
grep -E 'Failed password|authentication failure' /var/tmp/auth_sample.log | wc -l > /var/tmp/error_count.txt
```
