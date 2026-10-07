# [LFCS W2D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Awk user extraction:
```bash
awk -F: '$3 >= 1000 { printf "User: %s (UID: %s, Shell: %s)\n", $1, $3, $7 }' /etc/passwd > /var/tmp/regular_users.txt
```

2. Sed transformations:
```bash
sed -i 's/PORT = 8080/PORT = 443/' /var/tmp/config_sample.ini
sed -i '/DEBUG = True/d' /var/tmp/config_sample.ini
sed -i '/\[server\]/a ENVIRONMENT = Production' /var/tmp/config_sample.ini
```

3. CSV aggregation:
```bash
awk -F, 'NR>1 { sum += $2 } END { print sum }' /var/tmp/sales.csv > /var/tmp/sales_total.txt
```
