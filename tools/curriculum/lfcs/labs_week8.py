"""
Dedicated LFCS Lab Definitions for Week 8 (Days 1 to 6).
"""

WEEK_8_LABS = [
    {
        "day": 1,
        "date": '2026-11-16',
        "title": 'Containers & Virtual Machines on Linux',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Launch Detached Web Container
1. Ensure `podman` or `docker` is available on the system.
2. Run a detached container named `web-container` using image `docker.io/library/nginx:alpine` (or `nginx:alpine`):
   - Publish port `8085` on host to port `80` in container.

### Task 2: Container Volume Bind Mount
1. Create directory `/var/data/worker` on the host:
   `sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker`
2. Run a container named `data-worker` using image `docker.io/library/busybox:1.36` (or `busybox:1.36`):
   - Mount host directory `/var/data/worker` to `/data` in the container.
   - Command: `sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"`

### Task 3: Extract Container IP Address
1. Use `podman inspect` or `docker inspect` to extract the IP address (or NetworkSettings IP) of `web-container`.
2. Save the IP address to `/var/tmp/container_ip.txt`.""",
        "setup": """which podman >/dev/null 2>&1 || (sudo apt-get update -y && sudo apt-get install -y podman 2>/dev/null || true)
podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: web-container running and port mapped
if podman ps --format "{{.Names}}" 2>/dev/null | grep -q "web-container"; then
  echo -e "${GREEN}[PASS] Task 1: Container web-container is running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Container web-container is not running.${NC}"
fi

# Task 2: data-worker running and timestamps written
if [ -s /var/data/worker/timestamp.log ]; then
  echo -e "${GREEN}[PASS] Task 2: Container data-worker volume mount verified (/var/data/worker/timestamp.log).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/data/worker/timestamp.log missing or empty.${NC}"
fi

# Task 3: container IP extracted
if [ -s /var/tmp/container_ip.txt ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/container_ip.txt contains container IP details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/container_ip.txt missing or empty.${NC}"
fi""",
        "solution": """1. Run web container:
`podman run -d --name web-container -p 8085:80 docker.io/library/nginx:alpine`

2. Run data worker with volume:
```bash
sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker
podman run -d --name data-worker -v /var/data/worker:/data:Z docker.io/library/busybox:1.36 sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"
```

3. Extract IP:
`podman inspect web-container --format '{{.NetworkSettings.IPAddress}}' > /var/tmp/container_ip.txt`
If empty (host networking / rootless), extract container ID:
`podman inspect web-container --format '{{.Id}}' > /var/tmp/container_ip.txt`""",
        "reset": """podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt""",
        "lfcs_title": 'Containers & Virtual Machines on Linux',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Launch Detached Web Container
1. Ensure `podman` or `docker` is available on the system.
2. Run a detached container named `web-container` using image `docker.io/library/nginx:alpine` (or `nginx:alpine`):
   - Publish port `8085` on host to port `80` in container.

### Task 2: Container Volume Bind Mount
1. Create directory `/var/data/worker` on the host:
   `sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker`
2. Run a container named `data-worker` using image `docker.io/library/busybox:1.36` (or `busybox:1.36`):
   - Mount host directory `/var/data/worker` to `/data` in the container.
   - Command: `sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"`

### Task 3: Extract Container IP Address
1. Use `podman inspect` or `docker inspect` to extract the IP address (or NetworkSettings IP) of `web-container`.
2. Save the IP address to `/var/tmp/container_ip.txt`.""",
        "lfcs_setup": """which podman >/dev/null 2>&1 || (sudo apt-get update -y && sudo apt-get install -y podman 2>/dev/null || true)
podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: web-container running and port mapped
if podman ps --format "{{.Names}}" 2>/dev/null | grep -q "web-container"; then
  echo -e "${GREEN}[PASS] Task 1: Container web-container is running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Container web-container is not running.${NC}"
fi

# Task 2: data-worker running and timestamps written
if [ -s /var/data/worker/timestamp.log ]; then
  echo -e "${GREEN}[PASS] Task 2: Container data-worker volume mount verified (/var/data/worker/timestamp.log).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/data/worker/timestamp.log missing or empty.${NC}"
fi

# Task 3: container IP extracted
if [ -s /var/tmp/container_ip.txt ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/container_ip.txt contains container IP details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/container_ip.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Run web container:
`podman run -d --name web-container -p 8085:80 docker.io/library/nginx:alpine`

2. Run data worker with volume:
```bash
sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker
podman run -d --name data-worker -v /var/data/worker:/data:Z docker.io/library/busybox:1.36 sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"
```

3. Extract IP:
`podman inspect web-container --format '{{.NetworkSettings.IPAddress}}' > /var/tmp/container_ip.txt`
If empty (host networking / rootless), extract container ID:
`podman inspect web-container --format '{{.Id}}' > /var/tmp/container_ip.txt`""",
        "lfcs_reset": """podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt""",
    },
    {
        "day": 2,
        "date": '2026-11-17',
        "title": 'Timed Mock Exam 1 (Strict Exam Conditions)',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: User & Group Administration
1. Create a system group named `finance` with GID `2500`.
2. Create a user named `auditor`:
   - UID: `2500`
   - Supplementary group: `finance`
   - Shell: `/bin/bash`
   - Home directory: `/home/auditor`

### Task 2: Directory SGID Permissions
1. Create directory `/srv/finance`.
2. Set directory owner to `root` and group to `finance`.
3. Set permissions to `2770` (`rwxrws---`), ensuring the SGID bit is set for group inheritance.

### Task 3: Cron Automation
1. Create a cron configuration file `/etc/cron.d/audit_sync`.
2. Schedule the command `/bin/sync` to run every day at `03:30 AM` as user `root`.

### Task 4: Custom Systemd Service
1. Create a systemd unit `/etc/systemd/system/heartbeat.service`:
   - `Type=oneshot`
   - `ExecStart=/bin/sh -c "echo heartbeat >> /var/log/heartbeat.log"`
2. Reload systemd daemon (`sudo systemctl daemon-reload`).
3. Enable and start the service, verifying `/var/log/heartbeat.log` contains an entry.""",
        "setup": """sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: auditor user and finance group
U_GID=$(id -u auditor 2>/dev/null || echo "0")
G_MEM=$(id -nG auditor 2>/dev/null || echo "")
if [ "$U_GID" == "2500" ] && echo "$G_MEM" | grep -q "finance"; then
  echo -e "${GREEN}[PASS] Task 1: User auditor (UID 2500) and group finance verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: auditor user or finance group mismatch (UID=$U_GID, groups=$G_MEM).${NC}"
fi

# Task 2: /srv/finance permissions 2770 and group finance
DIR_PERM=$(stat -c "%a" /srv/finance 2>/dev/null || echo "000")
DIR_GRP=$(stat -c "%G" /srv/finance 2>/dev/null || echo "")
if [ "$DIR_PERM" == "2770" ] && [ "$DIR_GRP" == "finance" ]; then
  echo -e "${GREEN}[PASS] Task 2: Directory /srv/finance has permissions 2770 and group finance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /srv/finance perms=$DIR_PERM (exp 2770), group=$DIR_GRP (exp finance).${NC}"
fi

# Task 3: Cron job /etc/cron.d/audit_sync
if [ -f /etc/cron.d/audit_sync ] && grep -q "30 3 \* \* \* root /bin/sync" /etc/cron.d/audit_sync; then
  echo -e "${GREEN}[PASS] Task 3: Scheduled cron job /etc/cron.d/audit_sync verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Cron job syntax or file missing in /etc/cron.d/audit_sync.${NC}"
fi

# Task 4: heartbeat.service and log
if [ -f /etc/systemd/system/heartbeat.service ] && [ -s /var/log/heartbeat.log ] && grep -q "heartbeat" /var/log/heartbeat.log; then
  echo -e "${GREEN}[PASS] Task 4: heartbeat.service verified and log generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: heartbeat.service or /var/log/heartbeat.log invalid.${NC}"
fi""",
        "solution": """1. User & Group:
`sudo groupadd -g 2500 finance`
`sudo useradd -u 2500 -g finance -G finance -s /bin/bash -m auditor`

2. Directory Permissions:
`sudo mkdir -p /srv/finance`
`sudo chown root:finance /srv/finance`
`sudo chmod 2770 /srv/finance`

3. Cron job:
`echo "30 3 * * * root /bin/sync" | sudo tee /etc/cron.d/audit_sync`

4. Systemd unit:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/heartbeat.service
[Unit]
Description=Heartbeat Logger

[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo heartbeat >> /var/log/heartbeat.log"

[Install]
WantedBy=multi-user.target
EOF'
sudo systemctl daemon-reload
sudo systemctl enable --now heartbeat.service
```""",
        "reset": """sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true""",
        "lfcs_title": 'Timed Mock Exam 1 (Strict Exam Conditions)',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: User & Group Administration
1. Create a system group named `finance` with GID `2500`.
2. Create a user named `auditor`:
   - UID: `2500`
   - Supplementary group: `finance`
   - Shell: `/bin/bash`
   - Home directory: `/home/auditor`

### Task 2: Directory SGID Permissions
1. Create directory `/srv/finance`.
2. Set directory owner to `root` and group to `finance`.
3. Set permissions to `2770` (`rwxrws---`), ensuring the SGID bit is set for group inheritance.

### Task 3: Cron Automation
1. Create a cron configuration file `/etc/cron.d/audit_sync`.
2. Schedule the command `/bin/sync` to run every day at `03:30 AM` as user `root`.

### Task 4: Custom Systemd Service
1. Create a systemd unit `/etc/systemd/system/heartbeat.service`:
   - `Type=oneshot`
   - `ExecStart=/bin/sh -c "echo heartbeat >> /var/log/heartbeat.log"`
2. Reload systemd daemon (`sudo systemctl daemon-reload`).
3. Enable and start the service, verifying `/var/log/heartbeat.log` contains an entry.""",
        "lfcs_setup": """sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: auditor user and finance group
U_GID=$(id -u auditor 2>/dev/null || echo "0")
G_MEM=$(id -nG auditor 2>/dev/null || echo "")
if [ "$U_GID" == "2500" ] && echo "$G_MEM" | grep -q "finance"; then
  echo -e "${GREEN}[PASS] Task 1: User auditor (UID 2500) and group finance verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: auditor user or finance group mismatch (UID=$U_GID, groups=$G_MEM).${NC}"
fi

# Task 2: /srv/finance permissions 2770 and group finance
DIR_PERM=$(stat -c "%a" /srv/finance 2>/dev/null || echo "000")
DIR_GRP=$(stat -c "%G" /srv/finance 2>/dev/null || echo "")
if [ "$DIR_PERM" == "2770" ] && [ "$DIR_GRP" == "finance" ]; then
  echo -e "${GREEN}[PASS] Task 2: Directory /srv/finance has permissions 2770 and group finance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /srv/finance perms=$DIR_PERM (exp 2770), group=$DIR_GRP (exp finance).${NC}"
fi

# Task 3: Cron job /etc/cron.d/audit_sync
if [ -f /etc/cron.d/audit_sync ] && grep -q "30 3 \* \* \* root /bin/sync" /etc/cron.d/audit_sync; then
  echo -e "${GREEN}[PASS] Task 3: Scheduled cron job /etc/cron.d/audit_sync verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Cron job syntax or file missing in /etc/cron.d/audit_sync.${NC}"
fi

# Task 4: heartbeat.service and log
if [ -f /etc/systemd/system/heartbeat.service ] && [ -s /var/log/heartbeat.log ] && grep -q "heartbeat" /var/log/heartbeat.log; then
  echo -e "${GREEN}[PASS] Task 4: heartbeat.service verified and log generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: heartbeat.service or /var/log/heartbeat.log invalid.${NC}"
fi""",
        "lfcs_solution": """1. User & Group:
`sudo groupadd -g 2500 finance`
`sudo useradd -u 2500 -g finance -G finance -s /bin/bash -m auditor`

2. Directory Permissions:
`sudo mkdir -p /srv/finance`
`sudo chown root:finance /srv/finance`
`sudo chmod 2770 /srv/finance`

3. Cron job:
`echo "30 3 * * * root /bin/sync" | sudo tee /etc/cron.d/audit_sync`

4. Systemd unit:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/heartbeat.service
[Unit]
Description=Heartbeat Logger

[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo heartbeat >> /var/log/heartbeat.log"

[Install]
WantedBy=multi-user.target
EOF'
sudo systemctl daemon-reload
sudo systemctl enable --now heartbeat.service
```""",
        "lfcs_reset": """sudo userdel -r auditor 2>/dev/null || true
sudo groupdel finance 2>/dev/null || true
sudo rm -rf /srv/finance /etc/cron.d/audit_sync /etc/systemd/system/heartbeat.service /var/log/heartbeat.log
sudo systemctl daemon-reload 2>/dev/null || true""",
    },
    {
        "day": 3,
        "date": '2026-11-18',
        "title": 'Timed Mock Exam 2 (Strict Exam Conditions)',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Archive & Compression
1. Find all `.conf` files in `/etc` and package them into a gzip-compressed tar archive at `/var/tmp/etc_configs.tar.gz`.

### Task 2: Swap Space Management
1. Create a 128MB swap file at `/swapfile_mock2`.
2. Secure permissions to `0600`.
3. Format as swap using `mkswap` and enable it immediately with `swapon`.

### Task 3: Process Priority (Niceness)
1. Launch a background sleep command with a nice priority of `+10`:
   `nice -n 10 sleep 7200 &`

### Task 4: Package Log Analysis
1. Count the number of lines in `/var/log/dpkg.log` (or `/var/log/dpkg.log.1`) containing the word `status`.
2. Write the exact integer count into `/var/tmp/auth_summary.txt`.""",
        "setup": """sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: tar archive exists and valid
if [ -s /var/tmp/etc_configs.tar.gz ] && tar -tzf /var/tmp/etc_configs.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/etc_configs.tar.gz is a valid gzip archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/etc_configs.tar.gz missing or invalid archive.${NC}"
fi

# Task 2: swap active
if swapon --show | grep -q "/swapfile_mock2"; then
  echo -e "${GREEN}[PASS] Task 2: Swap file /swapfile_mock2 active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /swapfile_mock2 not active in swapon.${NC}"
fi

# Task 3: nice +10 process
NICE_VAL=$(ps -eo nice,cmd | grep "sleep 7200" | grep -v grep | awk '{print $1}' | head -n 1 || echo "")
if [ "$NICE_VAL" == "10" ]; then
  echo -e "${GREEN}[PASS] Task 3: sleep 7200 running with nice priority +10.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: sleep 7200 nice value is '$NICE_VAL' (expected 10).${NC}"
fi

# Task 4: log count integer
if [ -s /var/tmp/auth_summary.txt ] && grep -E -q '^[0-9]+$' /var/tmp/auth_summary.txt; then
  echo -e "${GREEN}[PASS] Task 4: /var/tmp/auth_summary.txt contains valid count: $(cat /var/tmp/auth_summary.txt).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/tmp/auth_summary.txt missing or not an integer.${NC}"
fi""",
        "solution": """1. Archive config files:
`sudo find /etc -name "*.conf" | tar -czf /var/tmp/etc_configs.tar.gz -T - 2>/dev/null`

2. Create and enable swap:
```bash
sudo fallocate -l 128M /swapfile_mock2 || sudo dd if=/dev/zero of=/swapfile_mock2 bs=1M count=128
sudo chmod 0600 /swapfile_mock2
sudo mkswap /swapfile_mock2
sudo swapon /swapfile_mock2
```

3. Launch process with nice +10:
`nice -n 10 sleep 7200 &`

4. Count status in dpkg log:
`grep "status" /var/log/dpkg.log* 2>/dev/null | wc -l > /var/tmp/auth_summary.txt`""",
        "reset": """sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true""",
        "lfcs_title": 'Timed Mock Exam 2 (Strict Exam Conditions)',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: Archive & Compression
1. Find all `.conf` files in `/etc` and package them into a gzip-compressed tar archive at `/var/tmp/etc_configs.tar.gz`.

### Task 2: Swap Space Management
1. Create a 128MB swap file at `/swapfile_mock2`.
2. Secure permissions to `0600`.
3. Format as swap using `mkswap` and enable it immediately with `swapon`.

### Task 3: Process Priority (Niceness)
1. Launch a background sleep command with a nice priority of `+10`:
   `nice -n 10 sleep 7200 &`

### Task 4: Package Log Analysis
1. Count the number of lines in `/var/log/dpkg.log` (or `/var/log/dpkg.log.1`) containing the word `status`.
2. Write the exact integer count into `/var/tmp/auth_summary.txt`.""",
        "lfcs_setup": """sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: tar archive exists and valid
if [ -s /var/tmp/etc_configs.tar.gz ] && tar -tzf /var/tmp/etc_configs.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/etc_configs.tar.gz is a valid gzip archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/etc_configs.tar.gz missing or invalid archive.${NC}"
fi

# Task 2: swap active
if swapon --show | grep -q "/swapfile_mock2"; then
  echo -e "${GREEN}[PASS] Task 2: Swap file /swapfile_mock2 active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /swapfile_mock2 not active in swapon.${NC}"
fi

# Task 3: nice +10 process
NICE_VAL=$(ps -eo nice,cmd | grep "sleep 7200" | grep -v grep | awk '{print $1}' | head -n 1 || echo "")
if [ "$NICE_VAL" == "10" ]; then
  echo -e "${GREEN}[PASS] Task 3: sleep 7200 running with nice priority +10.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: sleep 7200 nice value is '$NICE_VAL' (expected 10).${NC}"
fi

# Task 4: log count integer
if [ -s /var/tmp/auth_summary.txt ] && grep -E -q '^[0-9]+$' /var/tmp/auth_summary.txt; then
  echo -e "${GREEN}[PASS] Task 4: /var/tmp/auth_summary.txt contains valid count: $(cat /var/tmp/auth_summary.txt).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/tmp/auth_summary.txt missing or not an integer.${NC}"
fi""",
        "lfcs_solution": """1. Archive config files:
`sudo find /etc -name "*.conf" | tar -czf /var/tmp/etc_configs.tar.gz -T - 2>/dev/null`

2. Create and enable swap:
```bash
sudo fallocate -l 128M /swapfile_mock2 || sudo dd if=/dev/zero of=/swapfile_mock2 bs=1M count=128
sudo chmod 0600 /swapfile_mock2
sudo mkswap /swapfile_mock2
sudo swapon /swapfile_mock2
```

3. Launch process with nice +10:
`nice -n 10 sleep 7200 &`

4. Count status in dpkg log:
`grep "status" /var/log/dpkg.log* 2>/dev/null | wc -l > /var/tmp/auth_summary.txt`""",
        "lfcs_reset": """sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true""",
    },
    {
        "day": 4,
        "date": '2026-11-19',
        "title": 'Timed Mock Exam 3 (Strict Exam Conditions)',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Access Control Lists (ACLs)
1. Create directory `/var/mock3_shared`.
2. Using `setfacl`, grant user `student` read, write, and execute permissions (`rwx`) on `/var/mock3_shared`.
3. Set the same default ACL permissions on `/var/mock3_shared` for user `student` (`-d -m u:student:rwx`).

### Task 2: SUID Binary Audit
1. Search `/usr/bin` for all regular files having the SUID permission bit set (`-perm -4000`).
2. Sort the list of absolute paths alphabetically and save it to `/var/tmp/suid_binaries.txt`.

### Task 3: Persistent Kernel Module
1. Load the `dummy` network kernel module using `modprobe dummy`.
2. Configure `/etc/modules-load.d/dummy.conf` so that `dummy` is loaded automatically at boot.

### Task 4: Firewall Egress Restriction
1. Using iptables, add a rule to the `OUTPUT` chain to drop all outbound TCP traffic to IP `198.51.100.1` on port `443`:
   `sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`""",
        "setup": """sudo rm -rf /var/mock3_shared /var/tmp/suid_binaries.txt /etc/modules-load.d/dummy.conf
sudo iptables -D OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: ACL on /var/mock3_shared
ACL_CHK=$(getfacl /var/mock3_shared 2>/dev/null || true)
if echo "$ACL_CHK" | grep -q "user:student:rwx" && echo "$ACL_CHK" | grep -q "default:user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 1: ACL and default ACL for user student verified on /var/mock3_shared.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ACL missing on /var/mock3_shared.${NC}"
fi

# Task 2: SUID audit
if [ -s /var/tmp/suid_binaries.txt ] && grep -q "/usr/bin/" /var/tmp/suid_binaries.txt; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/suid_binaries.txt contains SUID executable paths.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/suid_binaries.txt missing or empty.${NC}"
fi

# Task 3: dummy kernel module loaded and persistent
MOD_LOADED=$(lsmod | grep -q "^dummy" && echo "yes" || echo "no")
MOD_CONF=$(grep -E "^dummy" /etc/modules-load.d/dummy.conf 2>/dev/null || true)
if [ "$MOD_LOADED" == "yes" ] && [ -n "$MOD_CONF" ]; then
  echo -e "${GREEN}[PASS] Task 3: dummy kernel module active and configured in /etc/modules-load.d/dummy.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: dummy module not loaded or persistent config missing.${NC}"
fi

# Task 4: OUTPUT drop rule
if sudo iptables -S OUTPUT | grep -q -- "-d 198.51.100.1/32 -p tcp -m tcp --dport 443 -j DROP\|-d 198.51.100.1 -p tcp --dport 443 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 4: Iptables OUTPUT drop rule for 198.51.100.1:443 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Iptables OUTPUT drop rule missing.${NC}"
fi""",
        "solution": """1. Set ACL:
```bash
sudo mkdir -p /var/mock3_shared
sudo setfacl -m u:student:rwx /var/mock3_shared
sudo setfacl -d -m u:student:rwx /var/mock3_shared
```

2. Audit SUID binaries:
`find /usr/bin -type f -perm -4000 | sort > /var/tmp/suid_binaries.txt`

3. Kernel module:
```bash
sudo modprobe dummy
echo "dummy" | sudo tee /etc/modules-load.d/dummy.conf
```

4. Firewall rule:
`sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`""",
        "reset": """sudo rm -rf /var/mock3_shared /var/tmp/suid_binaries.txt /etc/modules-load.d/dummy.conf
sudo iptables -D OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP 2>/dev/null || true""",
        "lfcs_title": 'Timed Mock Exam 3 (Strict Exam Conditions)',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: Access Control Lists (ACLs)
1. Create directory `/var/mock3_shared`.
2. Using `setfacl`, grant user `student` read, write, and execute permissions (`rwx`) on `/var/mock3_shared`.
3. Set the same default ACL permissions on `/var/mock3_shared` for user `student` (`-d -m u:student:rwx`).

### Task 2: SUID Binary Audit
1. Search `/usr/bin` for all regular files having the SUID permission bit set (`-perm -4000`).
2. Sort the list of absolute paths alphabetically and save it to `/var/tmp/suid_binaries.txt`.

### Task 3: Persistent Kernel Module
1. Load the `dummy` network kernel module using `modprobe dummy`.
2. Configure `/etc/modules-load.d/dummy.conf` so that `dummy` is loaded automatically at boot.

### Task 4: Firewall Egress Restriction
1. Using iptables, add a rule to the `OUTPUT` chain to drop all outbound TCP traffic to IP `198.51.100.1` on port `443`:
   `sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`""",
        "lfcs_setup": """sudo rm -rf /var/mock3_shared /var/tmp/suid_binaries.txt /etc/modules-load.d/dummy.conf
sudo iptables -D OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: ACL on /var/mock3_shared
ACL_CHK=$(getfacl /var/mock3_shared 2>/dev/null || true)
if echo "$ACL_CHK" | grep -q "user:student:rwx" && echo "$ACL_CHK" | grep -q "default:user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 1: ACL and default ACL for user student verified on /var/mock3_shared.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ACL missing on /var/mock3_shared.${NC}"
fi

# Task 2: SUID audit
if [ -s /var/tmp/suid_binaries.txt ] && grep -q "/usr/bin/" /var/tmp/suid_binaries.txt; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/suid_binaries.txt contains SUID executable paths.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/suid_binaries.txt missing or empty.${NC}"
fi

# Task 3: dummy kernel module loaded and persistent
MOD_LOADED=$(lsmod | grep -q "^dummy" && echo "yes" || echo "no")
MOD_CONF=$(grep -E "^dummy" /etc/modules-load.d/dummy.conf 2>/dev/null || true)
if [ "$MOD_LOADED" == "yes" ] && [ -n "$MOD_CONF" ]; then
  echo -e "${GREEN}[PASS] Task 3: dummy kernel module active and configured in /etc/modules-load.d/dummy.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: dummy module not loaded or persistent config missing.${NC}"
fi

# Task 4: OUTPUT drop rule
if sudo iptables -S OUTPUT | grep -q -- "-d 198.51.100.1/32 -p tcp -m tcp --dport 443 -j DROP\|-d 198.51.100.1 -p tcp --dport 443 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 4: Iptables OUTPUT drop rule for 198.51.100.1:443 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Iptables OUTPUT drop rule missing.${NC}"
fi""",
        "lfcs_solution": """1. Set ACL:
```bash
sudo mkdir -p /var/mock3_shared
sudo setfacl -m u:student:rwx /var/mock3_shared
sudo setfacl -d -m u:student:rwx /var/mock3_shared
```

2. Audit SUID binaries:
`find /usr/bin -type f -perm -4000 | sort > /var/tmp/suid_binaries.txt`

3. Kernel module:
```bash
sudo modprobe dummy
echo "dummy" | sudo tee /etc/modules-load.d/dummy.conf
```

4. Firewall rule:
`sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`""",
        "lfcs_reset": """sudo rm -rf /var/mock3_shared /var/tmp/suid_binaries.txt /etc/modules-load.d/dummy.conf
sudo iptables -D OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP 2>/dev/null || true""",
    },
    {
        "day": 5,
        "date": '2026-11-20',
        "title": 'Timed Mock Exam 4 & Final Speed Marathon',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Custom Systemd Timer
1. Create a systemd service `/etc/systemd/system/tmp_cleanup.service`:
   - `Type=oneshot`
   - `ExecStart=/bin/sh -c "/bin/rm -rf /tmp/mock_cache_*"`
2. Create a systemd timer `/etc/systemd/system/tmp_cleanup.timer`:
   - Runs every 10 minutes (`OnCalendar=*:0/10` or `OnUnitActiveSec=10min`).
3. Reload daemon and enable/start `tmp_cleanup.timer`.

### Task 2: Process Limits Configuration
1. In `/etc/security/limits.d/99-student-limits.conf`, configure the following limits for user `student`:
   - `student soft nofile 65535`
   - `student hard nofile 65535`
   - `student soft nproc 2048`
   - `student hard nproc 2048`

### Task 3: Virtual Interface Tuning
1. Create a dummy interface named `net-speed0`:
   `sudo ip link add net-speed0 type dummy`
2. Set MTU to `1400`.
3. Assign IP `10.99.1.1/24` and bring it UP.

### Task 4: Automated Log Rotation
1. Create a logrotate configuration `/etc/logrotate.d/mock4_logs` for `/var/log/mock4.log`:
   - Rotate daily (`daily`)
   - Keep 4 rotations (`rotate 4`)
   - Compress old files (`compress`)
   - Ignore missing log (`missingok`)
   - Do not rotate empty file (`notifempty`)
2. Validate syntax using `sudo logrotate -d /etc/logrotate.d/mock4_logs`.""",
        "setup": """sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: systemd timer active
TIMER_STATUS=$(systemctl is-active tmp_cleanup.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_STATUS" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: tmp_cleanup.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: tmp_cleanup.timer status is $TIMER_STATUS (expected active).${NC}"
fi

# Task 2: limits file
if [ -f /etc/security/limits.d/99-student-limits.conf ] && grep -q "student.*nofile.*65535" /etc/security/limits.d/99-student-limits.conf && grep -q "student.*nproc.*2048" /etc/security/limits.d/99-student-limits.conf; then
  echo -e "${GREEN}[PASS] Task 2: Process limits in /etc/security/limits.d/99-student-limits.conf verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Process limits missing or incorrect in 99-student-limits.conf.${NC}"
fi

# Task 3: net-speed0 MTU 1400, IP, UP
MTU_VAL=$(ip link show dev net-speed0 2>/dev/null | grep -o "mtu 1400" || echo "")
IP_VAL=$(ip addr show dev net-speed0 2>/dev/null | grep -o "10.99.1.1/24" || echo "")
if [ "$MTU_VAL" == "mtu 1400" ] && [ "$IP_VAL" == "10.99.1.1/24" ]; then
  echo -e "${GREEN}[PASS] Task 3: net-speed0 MTU 1400 and IP 10.99.1.1/24 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: net-speed0 MTU or IP incorrect (mtu=$MTU_VAL, ip=$IP_VAL).${NC}"
fi

# Task 4: logrotate config test
if [ -f /etc/logrotate.d/mock4_logs ] && sudo logrotate -d /etc/logrotate.d/mock4_logs >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 4: Logrotate configuration /etc/logrotate.d/mock4_logs syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /etc/logrotate.d/mock4_logs missing or syntax error.${NC}"
fi""",
        "solution": """1. Systemd service and timer:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.service
[Unit]
Description=Clean Temporary Cache Files

[Service]
Type=oneshot
ExecStart=/bin/sh -c "/bin/rm -rf /tmp/mock_cache_*"
EOF'

sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.timer
[Unit]
Description=Timer for Clean Temporary Cache Files

[Timer]
OnCalendar=*:0/10
Persistent=true

[Install]
WantedBy=timers.target
EOF'

sudo systemctl daemon-reload
sudo systemctl enable --now tmp_cleanup.timer
```

2. Process limits:
```bash
sudo bash -c 'cat << "EOF" > /etc/security/limits.d/99-student-limits.conf
student soft nofile 65535
student hard nofile 65535
student soft nproc 2048
student hard nproc 2048
EOF'
```

3. Dummy interface:
```bash
sudo ip link add net-speed0 type dummy
sudo ip link set mtu 1400 net-speed0
sudo ip addr add 10.99.1.1/24 dev net-speed0
sudo ip link set net-speed0 up
```

4. Logrotate:
```bash
sudo bash -c 'cat << "EOF" > /etc/logrotate.d/mock4_logs
/var/log/mock4.log {
    daily
    rotate 4
    compress
    missingok
    notifempty
}
EOF'
sudo logrotate -d /etc/logrotate.d/mock4_logs
```""",
        "reset": """sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true""",
        "lfcs_title": 'Timed Mock Exam 4 & Final Speed Marathon',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: Custom Systemd Timer
1. Create a systemd service `/etc/systemd/system/tmp_cleanup.service`:
   - `Type=oneshot`
   - `ExecStart=/bin/sh -c "/bin/rm -rf /tmp/mock_cache_*"`
2. Create a systemd timer `/etc/systemd/system/tmp_cleanup.timer`:
   - Runs every 10 minutes (`OnCalendar=*:0/10` or `OnUnitActiveSec=10min`).
3. Reload daemon and enable/start `tmp_cleanup.timer`.

### Task 2: Process Limits Configuration
1. In `/etc/security/limits.d/99-student-limits.conf`, configure the following limits for user `student`:
   - `student soft nofile 65535`
   - `student hard nofile 65535`
   - `student soft nproc 2048`
   - `student hard nproc 2048`

### Task 3: Virtual Interface Tuning
1. Create a dummy interface named `net-speed0`:
   `sudo ip link add net-speed0 type dummy`
2. Set MTU to `1400`.
3. Assign IP `10.99.1.1/24` and bring it UP.

### Task 4: Automated Log Rotation
1. Create a logrotate configuration `/etc/logrotate.d/mock4_logs` for `/var/log/mock4.log`:
   - Rotate daily (`daily`)
   - Keep 4 rotations (`rotate 4`)
   - Compress old files (`compress`)
   - Ignore missing log (`missingok`)
   - Do not rotate empty file (`notifempty`)
2. Validate syntax using `sudo logrotate -d /etc/logrotate.d/mock4_logs`.""",
        "lfcs_setup": """sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: systemd timer active
TIMER_STATUS=$(systemctl is-active tmp_cleanup.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_STATUS" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: tmp_cleanup.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: tmp_cleanup.timer status is $TIMER_STATUS (expected active).${NC}"
fi

# Task 2: limits file
if [ -f /etc/security/limits.d/99-student-limits.conf ] && grep -q "student.*nofile.*65535" /etc/security/limits.d/99-student-limits.conf && grep -q "student.*nproc.*2048" /etc/security/limits.d/99-student-limits.conf; then
  echo -e "${GREEN}[PASS] Task 2: Process limits in /etc/security/limits.d/99-student-limits.conf verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Process limits missing or incorrect in 99-student-limits.conf.${NC}"
fi

# Task 3: net-speed0 MTU 1400, IP, UP
MTU_VAL=$(ip link show dev net-speed0 2>/dev/null | grep -o "mtu 1400" || echo "")
IP_VAL=$(ip addr show dev net-speed0 2>/dev/null | grep -o "10.99.1.1/24" || echo "")
if [ "$MTU_VAL" == "mtu 1400" ] && [ "$IP_VAL" == "10.99.1.1/24" ]; then
  echo -e "${GREEN}[PASS] Task 3: net-speed0 MTU 1400 and IP 10.99.1.1/24 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: net-speed0 MTU or IP incorrect (mtu=$MTU_VAL, ip=$IP_VAL).${NC}"
fi

# Task 4: logrotate config test
if [ -f /etc/logrotate.d/mock4_logs ] && sudo logrotate -d /etc/logrotate.d/mock4_logs >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 4: Logrotate configuration /etc/logrotate.d/mock4_logs syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /etc/logrotate.d/mock4_logs missing or syntax error.${NC}"
fi""",
        "lfcs_solution": """1. Systemd service and timer:
```bash
sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.service
[Unit]
Description=Clean Temporary Cache Files

[Service]
Type=oneshot
ExecStart=/bin/sh -c "/bin/rm -rf /tmp/mock_cache_*"
EOF'

sudo bash -c 'cat << "EOF" > /etc/systemd/system/tmp_cleanup.timer
[Unit]
Description=Timer for Clean Temporary Cache Files

[Timer]
OnCalendar=*:0/10
Persistent=true

[Install]
WantedBy=timers.target
EOF'

sudo systemctl daemon-reload
sudo systemctl enable --now tmp_cleanup.timer
```

2. Process limits:
```bash
sudo bash -c 'cat << "EOF" > /etc/security/limits.d/99-student-limits.conf
student soft nofile 65535
student hard nofile 65535
student soft nproc 2048
student hard nproc 2048
EOF'
```

3. Dummy interface:
```bash
sudo ip link add net-speed0 type dummy
sudo ip link set mtu 1400 net-speed0
sudo ip addr add 10.99.1.1/24 dev net-speed0
sudo ip link set net-speed0 up
```

4. Logrotate:
```bash
sudo bash -c 'cat << "EOF" > /etc/logrotate.d/mock4_logs
/var/log/mock4.log {
    daily
    rotate 4
    compress
    missingok
    notifempty
}
EOF'
sudo logrotate -d /etc/logrotate.d/mock4_logs
```""",
        "lfcs_reset": """sudo systemctl stop tmp_cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/tmp_cleanup.* /etc/security/limits.d/99-student-limits.conf /etc/logrotate.d/mock4_logs
sudo ip link del net-speed0 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true""",
    },
    {
        "day": 6,
        "date": '2026-11-21',
        "title": 'Certification Gate Review & Readiness Audit',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Storage & Filesystem Health Audit
1. Execute a command to inspect filesystem type, mount point, and space for `/` (e.g. `df -hT /`).
2. Save the output to `/var/log/storage_audit.log`.

### Task 2: Service Security Audit
1. Check for any failed systemd units on the system using `systemctl --failed --no-legend`.
2. Save the list of failed services (or string `ALL_SERVICES_OPERATIONAL` if none failed) to `/var/log/security_audit.log`.

### Task 3: Automated System Backup Script
1. Create an executable script `/usr/local/bin/system_backup.sh`.
2. The script must package `/etc/systemd` and `/etc/default` into a gzip-compressed tar archive at `/var/backups/etc_backup_audit.tar.gz`.
3. Set executable permissions on `/usr/local/bin/system_backup.sh` and execute it once to create the backup archive.

### Task 4: Student User Security Validation
1. Verify permissions on `/home/student/.ssh`:
   - Directory permissions must be `0700`.
   - File permissions on `/home/student/.ssh/authorized_keys` must be `0600`.
   - Ownership of `/home/student/.ssh` must be `student:student`.""",
        "setup": 'sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh',
        "verify": """SCORE=0; TOTAL=4
# Task 1: Storage audit log exists
if [ -s /var/log/storage_audit.log ] && grep -q "/" /var/log/storage_audit.log; then
  echo -e "${GREEN}[PASS] Task 1: /var/log/storage_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/log/storage_audit.log missing or empty.${NC}"
fi

# Task 2: Security audit log exists
if [ -s /var/log/security_audit.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/security_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/security_audit.log missing or empty.${NC}"
fi

# Task 3: Backup script and archive
if [ -x /usr/local/bin/system_backup.sh ] && [ -s /var/backups/etc_backup_audit.tar.gz ] && tar -tzf /var/backups/etc_backup_audit.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 3: /usr/local/bin/system_backup.sh and /var/backups/etc_backup_audit.tar.gz verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Backup script or archive missing/corrupt.${NC}"
fi

# Task 4: Student ssh permissions
SSH_PERM=$(stat -c "%a" /home/student/.ssh 2>/dev/null || echo "000")
AUTH_PERM=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$SSH_PERM" == "700" ] && [ "$AUTH_PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 4: /home/student/.ssh permissions (700) and authorized_keys (600) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Permissions incorrect (.ssh=$SSH_PERM, authorized_keys=$AUTH_PERM).${NC}"
fi""",
        "solution": """1. Storage audit:
`df -hT / | sudo tee /var/log/storage_audit.log >/dev/null`

2. Service security audit:
```bash
FAILED=$(systemctl --failed --no-legend)
if [ -z "$FAILED" ]; then
  echo "ALL_SERVICES_OPERATIONAL" | sudo tee /var/log/security_audit.log >/dev/null
else
  echo "$FAILED" | sudo tee /var/log/security_audit.log >/dev/null
fi
```

3. Backup script:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/system_backup.sh
#!/usr/bin/env bash
mkdir -p /var/backups
tar -czf /var/backups/etc_backup_audit.tar.gz /etc/systemd /etc/default 2>/dev/null
EOF'
sudo chmod +x /usr/local/bin/system_backup.sh
sudo /usr/local/bin/system_backup.sh
```

4. SSH permissions:
```bash
chmod 700 /home/student/.ssh
chmod 600 /home/student/.ssh/authorized_keys
chown -R student:student /home/student/.ssh
```""",
        "reset": 'sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh',
        "lfcs_title": 'Certification Gate Review & Readiness Audit',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: Storage & Filesystem Health Audit
1. Execute a command to inspect filesystem type, mount point, and space for `/` (e.g. `df -hT /`).
2. Save the output to `/var/log/storage_audit.log`.

### Task 2: Service Security Audit
1. Check for any failed systemd units on the system using `systemctl --failed --no-legend`.
2. Save the list of failed services (or string `ALL_SERVICES_OPERATIONAL` if none failed) to `/var/log/security_audit.log`.

### Task 3: Automated System Backup Script
1. Create an executable script `/usr/local/bin/system_backup.sh`.
2. The script must package `/etc/systemd` and `/etc/default` into a gzip-compressed tar archive at `/var/backups/etc_backup_audit.tar.gz`.
3. Set executable permissions on `/usr/local/bin/system_backup.sh` and execute it once to create the backup archive.

### Task 4: Student User Security Validation
1. Verify permissions on `/home/student/.ssh`:
   - Directory permissions must be `0700`.
   - File permissions on `/home/student/.ssh/authorized_keys` must be `0600`.
   - Ownership of `/home/student/.ssh` must be `student:student`.""",
        "lfcs_setup": 'sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh',
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: Storage audit log exists
if [ -s /var/log/storage_audit.log ] && grep -q "/" /var/log/storage_audit.log; then
  echo -e "${GREEN}[PASS] Task 1: /var/log/storage_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/log/storage_audit.log missing or empty.${NC}"
fi

# Task 2: Security audit log exists
if [ -s /var/log/security_audit.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/security_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/security_audit.log missing or empty.${NC}"
fi

# Task 3: Backup script and archive
if [ -x /usr/local/bin/system_backup.sh ] && [ -s /var/backups/etc_backup_audit.tar.gz ] && tar -tzf /var/backups/etc_backup_audit.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 3: /usr/local/bin/system_backup.sh and /var/backups/etc_backup_audit.tar.gz verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Backup script or archive missing/corrupt.${NC}"
fi

# Task 4: Student ssh permissions
SSH_PERM=$(stat -c "%a" /home/student/.ssh 2>/dev/null || echo "000")
AUTH_PERM=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$SSH_PERM" == "700" ] && [ "$AUTH_PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 4: /home/student/.ssh permissions (700) and authorized_keys (600) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Permissions incorrect (.ssh=$SSH_PERM, authorized_keys=$AUTH_PERM).${NC}"
fi""",
        "lfcs_solution": """1. Storage audit:
`df -hT / | sudo tee /var/log/storage_audit.log >/dev/null`

2. Service security audit:
```bash
FAILED=$(systemctl --failed --no-legend)
if [ -z "$FAILED" ]; then
  echo "ALL_SERVICES_OPERATIONAL" | sudo tee /var/log/security_audit.log >/dev/null
else
  echo "$FAILED" | sudo tee /var/log/security_audit.log >/dev/null
fi
```

3. Backup script:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/system_backup.sh
#!/usr/bin/env bash
mkdir -p /var/backups
tar -czf /var/backups/etc_backup_audit.tar.gz /etc/systemd /etc/default 2>/dev/null
EOF'
sudo chmod +x /usr/local/bin/system_backup.sh
sudo /usr/local/bin/system_backup.sh
```

4. SSH permissions:
```bash
chmod 700 /home/student/.ssh
chmod 600 /home/student/.ssh/authorized_keys
chown -R student:student /home/student/.ssh
```""",
        "lfcs_reset": 'sudo rm -f /var/log/storage_audit.log /var/log/security_audit.log /var/backups/etc_backup_audit.tar.gz /usr/local/bin/system_backup.sh',
    },
]
