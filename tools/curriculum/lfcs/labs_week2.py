"""
Dedicated LFCS Lab Definitions for Week 2 (Days 1 to 6).
"""

WEEK_2_LABS = [
    {
        "day": 1,
        "date": '2026-10-05',
        "title": 'File Searching with Find and Locate',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Find Large Files
Search the `/var/log` directory for all files strictly larger than `500KB` (`+500k`). Save the list of full paths to `/var/tmp/large_logs.txt`.

### Task 2: Find by Modification Time and Permissions
Find all files in `/etc` that were modified within the last `7 days` (`-mtime -7`) and have permissions `644`. Output their paths to `/var/tmp/recent_configs.txt`.

### Task 3: Locate Database Indexing
Update the `mlocate` / `plocate` database (`sudo updatedb`) and use `locate` to find all configuration files ending in `.conf` located inside `/etc/systemd`. Save the results to `/var/tmp/systemd_confs.txt`.""",
        "setup": 'sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt',
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/large_logs.txt...${NC}"
if [ -f /var/tmp/large_logs.txt ] && [ -s /var/tmp/large_logs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/large_logs.txt created with entries.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/large_logs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/recent_configs.txt...${NC}"
if [ -f /var/tmp/recent_configs.txt ] && [ -s /var/tmp/recent_configs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/recent_configs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/recent_configs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/systemd_confs.txt...${NC}"
if [ -f /var/tmp/systemd_confs.txt ] && grep -q "/etc/systemd" /var/tmp/systemd_confs.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/systemd_confs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_confs.txt missing or lacks systemd configs.${NC}"
fi""",
        "solution": """1. Large files:
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
```""",
        "reset": 'sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt',
        "lfcs_title": 'File Searching with Find and Locate',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Find Large Files
Search the `/var/log` directory for all files strictly larger than `500KB` (`+500k`). Save the list of full paths to `/var/tmp/large_logs.txt`.

### Task 2: Find by Modification Time and Permissions
Find all files in `/etc` that were modified within the last `7 days` (`-mtime -7`) and have permissions `644`. Output their paths to `/var/tmp/recent_configs.txt`.

### Task 3: Locate Database Indexing
Update the `mlocate` / `plocate` database (`sudo updatedb`) and use `locate` to find all configuration files ending in `.conf` located inside `/etc/systemd`. Save the results to `/var/tmp/systemd_confs.txt`.""",
        "lfcs_setup": 'sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt',
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/large_logs.txt...${NC}"
if [ -f /var/tmp/large_logs.txt ] && [ -s /var/tmp/large_logs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/large_logs.txt created with entries.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/large_logs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/recent_configs.txt...${NC}"
if [ -f /var/tmp/recent_configs.txt ] && [ -s /var/tmp/recent_configs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/recent_configs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/recent_configs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/systemd_confs.txt...${NC}"
if [ -f /var/tmp/systemd_confs.txt ] && grep -q "/etc/systemd" /var/tmp/systemd_confs.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/systemd_confs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_confs.txt missing or lacks systemd configs.${NC}"
fi""",
        "lfcs_solution": """1. Large files:
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
```""",
        "lfcs_reset": 'sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt',
    },
    {
        "day": 2,
        "date": '2026-10-06',
        "title": 'Text Processing: Grep & Regular Expressions',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Extract IPv4 Addresses
From `/var/tmp/auth_sample.log`, extract all distinct IPv4 addresses that attempted connection. Save them sorted uniquely to `/var/tmp/auth_ips.txt`.

### Task 2: Case-Insensitive Pattern Filtering
In `/etc/security/`, find all configuration lines that contain `pam` or `login` ignoring case, excluding commented lines starting with `#`. Save to `/var/tmp/pam_rules.txt`.

### Task 3: Log Error Frequency Count
In `/var/tmp/auth_sample.log`, count how many lines contain `Failed password` or `authentication failure`. Output the integer count to `/var/tmp/error_count.txt`.""",
        "setup": """sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt
cat << 'EOF' > /var/tmp/auth_sample.log
Sep 14 10:00:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 45231 ssh2
Sep 14 10:00:05 server sshd[1235]: Failed password for root from 10.0.0.15 port 51234 ssh2
Sep 14 10:00:10 server sshd[1236]: Accepted publickey for student from 172.16.16.1 port 38291 ssh2
Sep 14 10:00:12 server sshd[1237]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50
Sep 14 10:00:15 server sshd[1238]: Failed password for root from 192.168.1.50 port 45233 ssh2
EOF""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/auth_ips.txt...${NC}"
if [ -f /var/tmp/auth_ips.txt ] && grep -q "192.168.1.50" /var/tmp/auth_ips.txt && grep -q "10.0.0.15" /var/tmp/auth_ips.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/auth_ips.txt contains extracted IP addresses.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/auth_ips.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/pam_rules.txt...${NC}"
if [ -f /var/tmp/pam_rules.txt ] && [ -s /var/tmp/pam_rules.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/pam_rules.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/pam_rules.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/error_count.txt...${NC}"
if [ -f /var/tmp/error_count.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/error_count.txt)" == "4" ]; then
  echo -e "${GREEN}[PASS] Error count matched expected count of 4.${NC}"
  SCORE=$((SCORE + 1))
else
  ACTUAL=$(cat /var/tmp/error_count.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Error count was '$ACTUAL' (expected 4).${NC}"
fi""",
        "solution": """1. Extract IPs:
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
```""",
        "reset": 'sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt /var/tmp/auth_sample.log',
        "lfcs_title": 'Text Processing: Grep & Regular Expressions',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Extract IPv4 Addresses
From `/var/tmp/auth_sample.log`, extract all distinct IPv4 addresses that attempted connection. Save them sorted uniquely to `/var/tmp/auth_ips.txt`.

### Task 2: Case-Insensitive Pattern Filtering
In `/etc/security/`, find all configuration lines that contain `pam` or `login` ignoring case, excluding commented lines starting with `#`. Save to `/var/tmp/pam_rules.txt`.

### Task 3: Log Error Frequency Count
In `/var/tmp/auth_sample.log`, count how many lines contain `Failed password` or `authentication failure`. Output the integer count to `/var/tmp/error_count.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt
cat << 'EOF' > /var/tmp/auth_sample.log
Sep 14 10:00:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 45231 ssh2
Sep 14 10:00:05 server sshd[1235]: Failed password for root from 10.0.0.15 port 51234 ssh2
Sep 14 10:00:10 server sshd[1236]: Accepted publickey for student from 172.16.16.1 port 38291 ssh2
Sep 14 10:00:12 server sshd[1237]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50
Sep 14 10:00:15 server sshd[1238]: Failed password for root from 192.168.1.50 port 45233 ssh2
EOF""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/auth_ips.txt...${NC}"
if [ -f /var/tmp/auth_ips.txt ] && grep -q "192.168.1.50" /var/tmp/auth_ips.txt && grep -q "10.0.0.15" /var/tmp/auth_ips.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/auth_ips.txt contains extracted IP addresses.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/auth_ips.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/pam_rules.txt...${NC}"
if [ -f /var/tmp/pam_rules.txt ] && [ -s /var/tmp/pam_rules.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/pam_rules.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/pam_rules.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/error_count.txt...${NC}"
if [ -f /var/tmp/error_count.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/error_count.txt)" == "4" ]; then
  echo -e "${GREEN}[PASS] Error count matched expected count of 4.${NC}"
  SCORE=$((SCORE + 1))
else
  ACTUAL=$(cat /var/tmp/error_count.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Error count was '$ACTUAL' (expected 4).${NC}"
fi""",
        "lfcs_solution": """1. Extract IPs:
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
```""",
        "lfcs_reset": 'sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt /var/tmp/auth_sample.log',
    },
    {
        "day": 3,
        "date": '2026-10-07',
        "title": 'Advanced Stream Analysis: Sed & Awk Fundamentals',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Awk Field Extraction
Extract users from `/etc/passwd` whose UID is >= 1000 and print formatted output:
`User: <name> (UID: <uid>, Shell: <shell>)`
Save output to `/var/tmp/regular_users.txt`.

### Task 2: Sed Stream Editing
In file `/var/tmp/config_sample.ini`:
1. Replace all occurrences of `PORT = 8080` with `PORT = 443`.
2. Delete any line containing `DEBUG = True`.
3. Insert `ENVIRONMENT = Production` on a new line immediately after `[server]`.

### Task 3: CSV Aggregation with Awk
Given `/var/tmp/sales.csv`, compute the total sum of the values in column 2 (revenue).
Output the total number as plain text to `/var/tmp/sales_total.txt`.""",
        "setup": """sudo rm -f /var/tmp/regular_users.txt /var/tmp/sales_total.txt
cat << 'EOF' > /var/tmp/config_sample.ini
[server]
HOST = 0.0.0.0
PORT = 8080
DEBUG = True
TIMEOUT = 60
EOF

cat << 'EOF' > /var/tmp/sales.csv
item,price,quantity
widget,25,10
gadget,50,4
gizmo,15,20
EOF""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Awk regular users report...${NC}"
if [ -f /var/tmp/regular_users.txt ] && grep -q "UID:" /var/tmp/regular_users.txt; then
  echo -e "${GREEN}[PASS] Awk user report verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/regular_users.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sed transformations...${NC}"
CONF=$(cat /var/tmp/config_sample.ini 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 443" && echo "$CONF" | grep -q "ENVIRONMENT = Production" && ! echo "$CONF" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Sed transformations verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Transformations missing in /var/tmp/config_sample.ini.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Sales sum...${NC}"
if [ -f /var/tmp/sales_total.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/sales_total.txt)" == "90" ]; then
  echo -e "${GREEN}[PASS] Sales sum matched 90 (25 + 50 + 15).${NC}"
  SCORE=$((SCORE + 1))
else
  VAL=$(cat /var/tmp/sales_total.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Sales sum was '$VAL' (expected 90).${NC}"
fi""",
        "solution": """1. Awk user extraction:
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
```""",
        "reset": 'sudo rm -f /var/tmp/regular_users.txt /var/tmp/config_sample.ini /var/tmp/sales.csv /var/tmp/sales_total.txt',
        "lfcs_title": 'Advanced Stream Analysis: Sed & Awk Fundamentals',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Awk Field Extraction
Extract users from `/etc/passwd` whose UID is >= 1000 and print formatted output:
`User: <name> (UID: <uid>, Shell: <shell>)`
Save output to `/var/tmp/regular_users.txt`.

### Task 2: Sed Stream Editing
In file `/var/tmp/config_sample.ini`:
1. Replace all occurrences of `PORT = 8080` with `PORT = 443`.
2. Delete any line containing `DEBUG = True`.
3. Insert `ENVIRONMENT = Production` on a new line immediately after `[server]`.

### Task 3: CSV Aggregation with Awk
Given `/var/tmp/sales.csv`, compute the total sum of the values in column 2 (revenue).
Output the total number as plain text to `/var/tmp/sales_total.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/regular_users.txt /var/tmp/sales_total.txt
cat << 'EOF' > /var/tmp/config_sample.ini
[server]
HOST = 0.0.0.0
PORT = 8080
DEBUG = True
TIMEOUT = 60
EOF

cat << 'EOF' > /var/tmp/sales.csv
item,price,quantity
widget,25,10
gadget,50,4
gizmo,15,20
EOF""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Awk regular users report...${NC}"
if [ -f /var/tmp/regular_users.txt ] && grep -q "UID:" /var/tmp/regular_users.txt; then
  echo -e "${GREEN}[PASS] Awk user report verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/regular_users.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sed transformations...${NC}"
CONF=$(cat /var/tmp/config_sample.ini 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 443" && echo "$CONF" | grep -q "ENVIRONMENT = Production" && ! echo "$CONF" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Sed transformations verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Transformations missing in /var/tmp/config_sample.ini.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Sales sum...${NC}"
if [ -f /var/tmp/sales_total.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/sales_total.txt)" == "90" ]; then
  echo -e "${GREEN}[PASS] Sales sum matched 90 (25 + 50 + 15).${NC}"
  SCORE=$((SCORE + 1))
else
  VAL=$(cat /var/tmp/sales_total.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Sales sum was '$VAL' (expected 90).${NC}"
fi""",
        "lfcs_solution": """1. Awk user extraction:
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
```""",
        "lfcs_reset": 'sudo rm -f /var/tmp/regular_users.txt /var/tmp/config_sample.ini /var/tmp/sales.csv /var/tmp/sales_total.txt',
    },
    {
        "day": 4,
        "date": '2026-10-08',
        "title": 'I/O Redirection & Stream Multiplexing',
        "diff": 'Medium',
        "time": '25m',
        "tasks": """### Task 1: Separate Standard Streams
Search the `/etc` directory for files containing `shadow`:
- Redirect all stdout matches to `/var/tmp/stdout.log` (`1>`).
- Redirect all stderr permission errors to `/var/tmp/stderr.log` (`2>`).

### Task 2: Tee Pipeline Logging
Using `ps -ef` and `tee`, generate a process snapshot:
- Write the full output to `/var/tmp/process_dump.txt`.
- Simultaneously count the total number of lines into `/var/tmp/process_count.txt` via pipe.

### Task 3: Automated Health Report via Heredoc
Write a bash script `/var/tmp/gen_health.sh`:
- When executed, it uses a Here-Document (`cat << 'EOF' > ...`) to write `/var/tmp/health.report`.
- The report must contain lines for `HOST: $(hostname)` and `KERNEL: $(uname -r)`.
- Execute the script and ensure `/var/tmp/health.report` exists.""",
        "setup": 'sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report',
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Separated standard streams...${NC}"
if [ -f /var/tmp/stdout.log ] && [ -f /var/tmp/stderr.log ]; then
  echo -e "${GREEN}[PASS] stdout.log and stderr.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Stream files missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Process dump and count...${NC}"
if [ -f /var/tmp/process_dump.txt ] && [ -f /var/tmp/process_count.txt ] && [ -s /var/tmp/process_count.txt ]; then
  echo -e "${GREEN}[PASS] Process dump and count verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Process dump files missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Health report via heredoc...${NC}"
if [ -f /var/tmp/health.report ] && grep -q "HOST:" /var/tmp/health.report && grep -q "KERNEL:" /var/tmp/health.report; then
  echo -e "${GREEN}[PASS] Health report generated with HOST and KERNEL.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/health.report missing or incomplete.${NC}"
fi""",
        "solution": """1. Stream separation:
```bash
find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log
```

2. Process tee pipeline:
```bash
ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt
```

3. Health script with heredoc:
```bash
cat << 'EOF' > /var/tmp/gen_health.sh
#!/usr/bin/env bash
cat << 'REPORT' > /var/tmp/health.report
HOST: $(hostname)
KERNEL: $(uname -r)
REPORT
EOF
chmod +x /var/tmp/gen_health.sh
bash /var/tmp/gen_health.sh
```""",
        "reset": 'sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report',
        "lfcs_title": 'I/O Redirection & Stream Multiplexing',
        "lfcs_diff": 'Medium',
        "lfcs_time": '25m',
        "lfcs_tasks": """### Task 1: Separate Standard Streams
Search the `/etc` directory for files containing `shadow`:
- Redirect all stdout matches to `/var/tmp/stdout.log` (`1>`).
- Redirect all stderr permission errors to `/var/tmp/stderr.log` (`2>`).

### Task 2: Tee Pipeline Logging
Using `ps -ef` and `tee`, generate a process snapshot:
- Write the full output to `/var/tmp/process_dump.txt`.
- Simultaneously count the total number of lines into `/var/tmp/process_count.txt` via pipe.

### Task 3: Automated Health Report via Heredoc
Write a bash script `/var/tmp/gen_health.sh`:
- When executed, it uses a Here-Document (`cat << 'EOF' > ...`) to write `/var/tmp/health.report`.
- The report must contain lines for `HOST: $(hostname)` and `KERNEL: $(uname -r)`.
- Execute the script and ensure `/var/tmp/health.report` exists.""",
        "lfcs_setup": 'sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report',
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Separated standard streams...${NC}"
if [ -f /var/tmp/stdout.log ] && [ -f /var/tmp/stderr.log ]; then
  echo -e "${GREEN}[PASS] stdout.log and stderr.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Stream files missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Process dump and count...${NC}"
if [ -f /var/tmp/process_dump.txt ] && [ -f /var/tmp/process_count.txt ] && [ -s /var/tmp/process_count.txt ]; then
  echo -e "${GREEN}[PASS] Process dump and count verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Process dump files missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Health report via heredoc...${NC}"
if [ -f /var/tmp/health.report ] && grep -q "HOST:" /var/tmp/health.report && grep -q "KERNEL:" /var/tmp/health.report; then
  echo -e "${GREEN}[PASS] Health report generated with HOST and KERNEL.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/health.report missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Stream separation:
```bash
find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log
```

2. Process tee pipeline:
```bash
ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt
```

3. Health script with heredoc:
```bash
cat << 'EOF' > /var/tmp/gen_health.sh
#!/usr/bin/env bash
cat << 'REPORT' > /var/tmp/health.report
HOST: $(hostname)
KERNEL: $(uname -r)
REPORT
EOF
chmod +x /var/tmp/gen_health.sh
bash /var/tmp/gen_health.sh
```""",
        "lfcs_reset": 'sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report',
    },
    {
        "day": 5,
        "date": '2026-10-09',
        "title": 'Archiving, Compression & Remote Backups',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Gzip Compressed Tar Archive
Create a compressed tar archive of `/etc/systemd/` saved to `/var/tmp/systemd_backup.tar.gz`. Preserve all file permissions (`-p`).

### Task 2: Extract to Alternate Target
Extract `/var/tmp/systemd_backup.tar.gz` into directory `/var/tmp/extracted_systemd/` without changing your current directory.

### Task 3: Tarball Content Verification
List the table of contents of `/var/tmp/systemd_backup.tar.gz` (`-tzf`) and save the file list to `/var/tmp/archive_manifest.txt`.""",
        "setup": 'sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt',
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/systemd_backup.tar.gz...${NC}"
if [ -f /var/tmp/systemd_backup.tar.gz ] && tar -tzf /var/tmp/systemd_backup.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Gzip tar archive created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_backup.tar.gz missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Extracted directory...${NC}"
if [ -d /var/tmp/extracted_systemd/etc/systemd ] || [ -d /var/tmp/extracted_systemd/systemd ]; then
  echo -e "${GREEN}[PASS] Archive extracted to target directory.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Extracted directory structure missing.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/archive_manifest.txt...${NC}"
if [ -f /var/tmp/archive_manifest.txt ] && grep -q "system.conf" /var/tmp/archive_manifest.txt; then
  echo -e "${GREEN}[PASS] Archive manifest verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/archive_manifest.txt missing or empty.${NC}"
fi""",
        "solution": """1. Create archive:
```bash
sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd
```

2. Extract to destination:
```bash
mkdir -p /var/tmp/extracted_systemd
sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd
```

3. Manifest:
```bash
tar -tzf /var/tmp/systemd_backup.tar.gz > /var/tmp/archive_manifest.txt
```""",
        "reset": 'sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt',
        "lfcs_title": 'Archiving, Compression & Remote Backups',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Gzip Compressed Tar Archive
Create a compressed tar archive of `/etc/systemd/` saved to `/var/tmp/systemd_backup.tar.gz`. Preserve all file permissions (`-p`).

### Task 2: Extract to Alternate Target
Extract `/var/tmp/systemd_backup.tar.gz` into directory `/var/tmp/extracted_systemd/` without changing your current directory.

### Task 3: Tarball Content Verification
List the table of contents of `/var/tmp/systemd_backup.tar.gz` (`-tzf`) and save the file list to `/var/tmp/archive_manifest.txt`.""",
        "lfcs_setup": 'sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt',
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/systemd_backup.tar.gz...${NC}"
if [ -f /var/tmp/systemd_backup.tar.gz ] && tar -tzf /var/tmp/systemd_backup.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Gzip tar archive created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_backup.tar.gz missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Extracted directory...${NC}"
if [ -d /var/tmp/extracted_systemd/etc/systemd ] || [ -d /var/tmp/extracted_systemd/systemd ]; then
  echo -e "${GREEN}[PASS] Archive extracted to target directory.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Extracted directory structure missing.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/archive_manifest.txt...${NC}"
if [ -f /var/tmp/archive_manifest.txt ] && grep -q "system.conf" /var/tmp/archive_manifest.txt; then
  echo -e "${GREEN}[PASS] Archive manifest verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/archive_manifest.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Create archive:
```bash
sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd
```

2. Extract to destination:
```bash
mkdir -p /var/tmp/extracted_systemd
sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd
```

3. Manifest:
```bash
tar -tzf /var/tmp/systemd_backup.tar.gz > /var/tmp/archive_manifest.txt
```""",
        "lfcs_reset": 'sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt',
    },
    {
        "day": 6,
        "date": '2026-10-10',
        "title": 'Week 2 Speed Drills & Git Version Control',
        "diff": 'Hard (Milestone Assessment 2)',
        "time": '45m',
        "tasks": """### Milestone 2 Triathlon Tasks:
1. Initialize a git repository in `/srv/repo`.
2. Create and commit a configuration file `system.conf` with content `config=v1`.
3. Create a branch `feature-audit`, modify `system.conf` to `config=v2`, commit with message `feat: update v2`, switch back to `main` (or `master`), and merge `feature-audit`.
4. Create a tar.gz backup of the entire git repo into `/var/backups/repo.tar.gz`.""",
        "setup": 'sudo rm -rf /srv/repo /var/backups/repo.tar.gz',
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Git repository initialized...${NC}"
if [ -d /srv/repo/.git ]; then
  echo -e "${GREEN}[PASS] Git repo initialized in /srv/repo.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /srv/repo/.git directory not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2 & 3: Branch merge & system.conf...${NC}"
sudo git config --system --add safe.directory /srv/repo 2>/dev/null || true
CONF=$(cat /srv/repo/system.conf 2>/dev/null || echo "None")
COMMITS=$(git -C /srv/repo rev-list --count HEAD 2>/dev/null || sudo git -C /srv/repo rev-list --count HEAD 2>/dev/null || echo "0")
if [ "$CONF" == "config=v2" ] && [ "$COMMITS" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Branch merged with config=v2 and commit history.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] system.conf: $CONF, commits: $COMMITS.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Backup archive...${NC}"
if [ -f /var/backups/repo.tar.gz ] && tar -tzf /var/backups/repo.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Repository backup archive verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/repo.tar.gz missing or invalid.${NC}"
fi""",
        "solution": """1. Init repo:
```bash
sudo mkdir -p /srv/repo
sudo chown -R $(whoami):$(whoami) /srv/repo
cd /srv/repo
git init -b main
git config user.name "Student"
git config user.email "student@example.com"
echo "config=v1" > system.conf
git add system.conf
git commit -m "initial commit"
```

2. Branch and merge:
```bash
git checkout -b feature-audit
echo "config=v2" > system.conf
git commit -am "feat: update v2"
git checkout main
git merge feature-audit
```

3. Tarball backup:
```bash
sudo mkdir -p /var/backups
sudo tar -czf /var/backups/repo.tar.gz -C /srv repo
```""",
        "reset": 'sudo rm -rf /srv/repo /var/backups/repo.tar.gz',
        "lfcs_title": 'Week 2 Speed Drills & Git Version Control',
        "lfcs_diff": 'Hard (Milestone Assessment 2)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 2 Triathlon Tasks:
1. Initialize a git repository in `/srv/repo`.
2. Create and commit a configuration file `system.conf` with content `config=v1`.
3. Create a branch `feature-audit`, modify `system.conf` to `config=v2`, commit with message `feat: update v2`, switch back to `main` (or `master`), and merge `feature-audit`.
4. Create a tar.gz backup of the entire git repo into `/var/backups/repo.tar.gz`.""",
        "lfcs_setup": 'sudo rm -rf /srv/repo /var/backups/repo.tar.gz',
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Git repository initialized...${NC}"
if [ -d /srv/repo/.git ]; then
  echo -e "${GREEN}[PASS] Git repo initialized in /srv/repo.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /srv/repo/.git directory not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2 & 3: Branch merge & system.conf...${NC}"
sudo git config --system --add safe.directory /srv/repo 2>/dev/null || true
CONF=$(cat /srv/repo/system.conf 2>/dev/null || echo "None")
COMMITS=$(git -C /srv/repo rev-list --count HEAD 2>/dev/null || sudo git -C /srv/repo rev-list --count HEAD 2>/dev/null || echo "0")
if [ "$CONF" == "config=v2" ] && [ "$COMMITS" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Branch merged with config=v2 and commit history.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] system.conf: $CONF, commits: $COMMITS.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Backup archive...${NC}"
if [ -f /var/backups/repo.tar.gz ] && tar -tzf /var/backups/repo.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Repository backup archive verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/repo.tar.gz missing or invalid.${NC}"
fi""",
        "lfcs_solution": """1. Init repo:
```bash
sudo mkdir -p /srv/repo
sudo chown -R $(whoami):$(whoami) /srv/repo
cd /srv/repo
git init -b main
git config user.name "Student"
git config user.email "student@example.com"
echo "config=v1" > system.conf
git add system.conf
git commit -m "initial commit"
```

2. Branch and merge:
```bash
git checkout -b feature-audit
echo "config=v2" > system.conf
git commit -am "feat: update v2"
git checkout main
git merge feature-audit
```

3. Tarball backup:
```bash
sudo mkdir -p /var/backups
sudo tar -czf /var/backups/repo.tar.gz -C /srv repo
```""",
        "lfcs_reset": 'sudo rm -rf /srv/repo /var/backups/repo.tar.gz',
    },
]
