"""
Dedicated LFCS Mock Exam Lab Definitions.
"""

MOCK_LABS = [
    {
        "lab_id": 'mock-lfcs-1',
        "track": 'LFCS',
        "date": '2026-11-17',
        "title": 'LFCS Full-Scale Timed Mock Exam 1',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# LFCS Full-Scale Timed Mock Exam 1

**Passing Score:** 67% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Environment:** VirtualBox Ubuntu LFCS VM (`student@172.16.16.16`)

---

### Linux Foundation Official Domain Weights:
1. **Operations Deployment (25%)**
   - Configure kernel parameters, persistent and non-persistent
   - Diagnose, identify, manage, and troubleshoot processes and services
   - Manage or schedule jobs for executing commands
   - Search for, install, validate, and maintain software packages or repositories
   - Recover from hardware, operating system, or filesystem failures
   - Manage Virtual Machines (libvirt)
   - Configure container engines, create and manage containers
   - Create and enforce MAC using SELinux
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Set and synchronize system time using time servers
   - Monitor and troubleshoot networking
   - Configure the OpenSSH server and client
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Use remote filesystems and network block devices
   - Configure and manage swap space
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Basic Git Operations
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Determine application and service specific constraints
   - Troubleshoot diskspace issues
   - Work with SSL certificates
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits
   - Configure and manage ACLs
   - Configure the system to use LDAP user and group accounts

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** Initialize a standard Git source code management workflow for a project in `/var/tmp/mock-lfcs-1/git-repo`:
  - Create a new Git repository in `/var/tmp/mock-lfcs-1/git-repo`.
  - Add a file named `README.md` with the content `# Master Repo` and commit it to branch `main`.
  - Create and switch to a new branch named `feature`.
  - In branch `feature`, add a file named `feature.txt` with content `new feature` and commit the file.
  - Return to branch `main` and merge branch `feature` into `main` so the commit history records the integration.
- **Q2:** A custom monitoring script `/usr/local/bin/mock_monitor.sh` needs to be managed as a continuous background daemon:
  - Create a custom systemd service unit file at `/etc/systemd/system/mock-monitor.service`.
  - Configure the unit to run `/usr/local/bin/mock_monitor.sh` (which logs timestamps to `/var/tmp/mock-lfcs-1/monitor.log`).
  - Reload systemd daemon configuration, enable the service to start at boot, and start it immediately.
  - Verify that the service status is active and running.
- **Q3:** Perform a disk space audit to identify recently modified large files in `/var/tmp/mock-lfcs-1`:
  - Locate all regular files within `/var/tmp/mock-lfcs-1` that were modified within the past 7 days and exceed 100 Kilobytes in size.
  - Save the list of matched file paths into `/var/tmp/mock-lfcs-1/large-files.txt`.
- **Q4:** Extract metadata from an X.509 certificate for a security compliance audit:
  - Inspect the SSL/TLS certificate located at `/var/tmp/mock-lfcs-1/exam.crt`.
  - Extract the certificate's subject, issuer, and expiration date.
  - Save the extracted certificate details into `/var/tmp/mock-lfcs-1/cert-info.txt`.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Optimize memory management by tuning the kernel swappiness parameter:
  - Set the kernel parameter `vm.swappiness` to value `10`.
  - Ensure the setting persists across system reboots by placing a sysctl configuration file at `/etc/sysctl.d/99-swappiness.conf`.
  - Apply the change immediately to the active kernel without rebooting the system.
- **Q6:** Establish an automated cron job for administrative logging under user `student`:
  - Configure a user crontab for user `student`.
  - Schedule command `/bin/echo 'Cron job executed'` to run at 02:30 AM every weekday (Monday through Friday).
  - Confirm the schedule is installed and visible in `student`'s crontab listing.
- **Q7:** Query the package management database to audit installed package artifacts:
  - Query all installed files belonging to the package `tar`.
  - Write the complete file listing into `/var/tmp/mock-lfcs-1/pkg-files.txt`.
- **Q8:** Launch an asynchronous background process and record its process ID for operational tracking:
  - Launch the command `sleep 9999` in the background.
  - Determine the process ID (PID) of this active command.
  - Write only the numeric PID to file `/var/tmp/mock-lfcs-1/sleep.pid`.
- **Q9:** Provision a lightweight containerized web server to verify container runtime functionality:
  - Using the available container engine (Docker or Podman), run a detached container named `mock-web`.
  - Deploy using container image `nginx:alpine`.
  - Expose container port 80 by publishing it to host port `8088`.
  - Verify that `mock-web` is running.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Configure static host name resolution for local system services:
  - Edit the system's static host lookup table (`/etc/hosts`).
  - Map host name `exam.local` to the loopback IPv4 address `127.0.0.1`.
- **Q11:** Inspect and document the system's time synchronization and timezone configuration:
  - Query the status of system time, time zone, and network time synchronization.
  - Save the command output to file `/var/tmp/mock-lfcs-1/time-status.txt`.
- **Q12:** Conduct a network port audit to document all actively listening TCP sockets:
  - Query all listening TCP sockets along with associated process identifiers.
  - Write the socket table output into `/var/tmp/mock-lfcs-1/listening-ports.txt`.
- **Q13:** Implement SSH server hardening in accordance with corporate security standards:
  - Create a drop-in configuration file at `/etc/ssh/sshd_config.d/99-hardening.conf`.
  - Disable direct remote root login (`PermitRootLogin no`).
  - Restrict the maximum authentication attempts per connection to 3 (`MaxAuthTries 3`).
  - Validate the SSH configuration syntax to confirm no syntax errors exist.
- **Q14:** Document active firewall packet filtering rules for network security auditing:
  - Query the system's active packet filtering rules and chains.
  - Save the active firewall rules table to file `/var/tmp/mock-lfcs-1/firewall-rules.txt`.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Provision a raw block storage container file and create an ext4 filesystem:
  - Create a 100 Megabyte zero-filled image file at `/var/tmp/mock-lfcs-1/disk1.img`.
  - Format the image file with an `ext4` filesystem.
  - Confirm filesystem creation.
- **Q16:** Configure Logical Volume Management (LVM) storage components on loop storage:
  - Associate `/var/tmp/mock-lfcs-1/disk1.img` with a loop device and initialize it as an LVM Physical Volume.
  - Create a Volume Group named `mock-vg` using the physical volume.
  - Within `mock-vg`, create a Logical Volume named `mock-lv` with an initial size of `50MB`.
  - Format `mock-lv` as `ext4` and mount it at directory `/var/tmp/mock-lfcs-1/lvm-mount`.
- **Q17:** Dynamically expand logical volume storage to accommodate capacity growth:
  - Extend logical volume `mock-lv` in volume group `mock-vg` to a total size of `80MB`.
  - Resize the underlying `ext4` filesystem online so the additional storage is immediately available.
  - Verify that `lvs` and filesystem reports show the updated 80MB size.
- **Q18:** Allocate and activate additional virtual memory swap storage:
  - Create a 64 Megabyte swap file at `/var/tmp/mock-lfcs-1/swapfile`.
  - Secure the file permissions so that only the root user has read and write access.
  - Format the file as swap space and enable it immediately.
  - Verify that the swap file is active in system swap allocations.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Create project accounts and configure granular POSIX filesystem access controls:
  - Create user `devops` with specific UID `2001`.
  - Create user `tester` with specific UID `2002`.
  - Create group `infrateam` with specific GID `3001`.
  - Configure POSIX Access Control Lists (ACLs) on directory `/var/tmp/mock-lfcs-1/shared` granting group `infrateam` read, write, and execute (`rwx`) permissions.
- **Q20:** Configure process resource limits and user password aging policies:
  - In `/etc/security/limits.conf`, set both soft and hard open file limits (`nofile`) to `4096` for user `student`.
  - Configure password aging for user `student` such that passwords must be changed at least every 90 days.""",
        "setup": """sudo rm -rf /var/tmp/mock-lfcs-1 /etc/sysctl.d/99-swappiness.conf /etc/systemd/system/mock-monitor.service /etc/ssh/sshd_config.d/99-hardening.conf
sudo mkdir -p /var/tmp/mock-lfcs-1/shared && sudo chown -R student:student /var/tmp/mock-lfcs-1 && sudo chmod -R 777 /var/tmp/mock-lfcs-1
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/key.pem -out /var/tmp/mock-lfcs-1/exam.crt -subj "/CN=exam.local/O=MockCorp" 2>/dev/null || true
rm -f /tmp/key.pem
# Create sample file for Q3
dd if=/dev/urandom of=/var/tmp/mock-lfcs-1/sample_large.bin bs=1K count=150 2>/dev/null || true
# Ensure users/groups clean
sudo userdel -r devops 2>/dev/null || true
sudo userdel -r tester 2>/dev/null || true
sudo groupdel infrateam 2>/dev/null || true""",
        "verify": """# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 1 against Linux Foundation Domain Weights...${NC}"

# Q1: Git repo (Essential Commands - 20%)
if [ -d /var/tmp/mock-lfcs-1/git-repo/.git ] && git -C /var/tmp/mock-lfcs-1/git-repo log --oneline 2>/dev/null | grep -q "feature"; then
  echo -e "${GREEN}[PASS] Q1: Git repository and feature branch merge verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: Git repo or feature commit missing.${NC}"
fi

# Q2: Systemd service (Essential Commands - 20%)
if systemctl is-active mock-monitor.service &>/dev/null; then
  echo -e "${GREEN}[PASS] Q2: mock-monitor.service is active.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: mock-monitor.service not active.${NC}"
fi

# Q3: Large files find (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-1/large-files.txt ] && grep -q "sample_large.bin" /var/tmp/mock-lfcs-1/large-files.txt; then
  echo -e "${GREEN}[PASS] Q3: Large files report verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: large-files.txt missing or lacks entries.${NC}"
fi

# Q4: SSL Cert Info (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-1/cert-info.txt ] && grep -qi "exam.local" /var/tmp/mock-lfcs-1/cert-info.txt; then
  echo -e "${GREEN}[PASS] Q4: cert-info.txt verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: cert-info.txt missing or lacks subject info.${NC}"
fi

# Q5: Swappiness (Operations Deployment - 25%)
if [ -f /etc/sysctl.d/99-swappiness.conf ] && [ "$(sysctl -n vm.swappiness)" == "10" ]; then
  echo -e "${GREEN}[PASS] Q5: vm.swappiness=10 persistently configured.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: vm.swappiness is $(sysctl -n vm.swappiness) (expected 10).${NC}"
fi

# Q6: Crontab student (Operations Deployment - 25%)
if crontab -u student -l 2>/dev/null | grep -q "30 2 \* \* 1-5"; then
  echo -e "${GREEN}[PASS] Q6: Crontab schedule verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: Crontab entry for student missing.${NC}"
fi

# Q7: Package file count (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-1/pkg-files.txt ] && [ -s /var/tmp/mock-lfcs-1/pkg-files.txt ]; then
  echo -e "${GREEN}[PASS] Q7: Package files query recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: pkg-files.txt missing or empty.${NC}"
fi

# Q8: Sleep PID (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-1/sleep.pid ] && pgrep -F /var/tmp/mock-lfcs-1/sleep.pid &>/dev/null; then
  echo -e "${GREEN}[PASS] Q8: Process PID recorded and running.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: Process PID missing or not running.${NC}"
fi

# Q9: Container mock-web (Operations Deployment - 25%)
if (docker ps 2>/dev/null || podman ps 2>/dev/null) | grep -q "mock-web"; then
  echo -e "${GREEN}[PASS] Q9: Container mock-web is running.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-web not running.${NC}"
fi

# Q10: /etc/hosts entry (Networking - 25%)
if grep -q "exam.local" /etc/hosts; then
  echo -e "${GREEN}[PASS] Q10: /etc/hosts contains exam.local.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: /etc/hosts lacks exam.local.${NC}"
fi

# Q11: Timedatectl (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/time-status.txt ] && grep -qi "Time zone" /var/tmp/mock-lfcs-1/time-status.txt; then
  echo -e "${GREEN}[PASS] Q11: time-status.txt verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: time-status.txt missing.${NC}"
fi

# Q12: Listening ports (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/listening-ports.txt ] && grep -qi "LISTEN" /var/tmp/mock-lfcs-1/listening-ports.txt; then
  echo -e "${GREEN}[PASS] Q12: listening-ports.txt verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: listening-ports.txt missing or empty.${NC}"
fi

# Q13: SSH drop-in config (Networking - 25%)
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -qi "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf; then
  echo -e "${GREEN}[PASS] Q13: SSH hardening drop-in verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: 99-hardening.conf missing or incomplete.${NC}"
fi

# Q14: Firewall status (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/firewall-rules.txt ] && [ -s /var/tmp/mock-lfcs-1/firewall-rules.txt ]; then
  echo -e "${GREEN}[PASS] Q14: Firewall rules report verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: firewall-rules.txt missing.${NC}"
fi

# Q15: Ext4 Disk Image (Storage - 20%)
if [ -f /var/tmp/mock-lfcs-1/disk1.img ] && file /var/tmp/mock-lfcs-1/disk1.img | grep -qi "ext4"; then
  echo -e "${GREEN}[PASS] Q15: disk1.img created and formatted as ext4.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: disk1.img missing or not ext4.${NC}"
fi

# Q16: LVM volume mount (Storage - 20%)
if mountpoint -q /var/tmp/mock-lfcs-1/lvm-mount 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q16: LVM logical volume mounted at lvm-mount.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: lvm-mount is not mounted.${NC}"
fi

# Q17: LVM extend size (Storage - 20%)
LV_SIZE=$(lvs --noheadings -o lv_size mock-vg/mock-lv 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SIZE" | grep -q "80"; then
  echo -e "${GREEN}[PASS] Q17: Logical volume extended to 80M.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: LV size is '$LV_SIZE' (expected 80M).${NC}"
fi

# Q18: Swapfile (Storage - 20%)
if swapon --show | grep -q "mock-lfcs-1/swapfile"; then
  echo -e "${GREEN}[PASS] Q18: Swapfile active.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: swapfile is not active.${NC}"
fi

# Q19: Users, Group & ACL (Users and Groups - 10%)
ACL_CHECK=$(getfacl /var/tmp/mock-lfcs-1/shared 2>/dev/null || true)
if id devops &>/dev/null && id tester &>/dev/null && echo "$ACL_CHECK" | grep -q "group:infrateam:rwx"; then
  echo -e "${GREEN}[PASS] Q19: Users devops, tester and ACL on shared directory verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: Users or ACL missing on /var/tmp/mock-lfcs-1/shared.${NC}"
fi

# Q20: Limits & Password aging (Users and Groups - 10%)
CHAGE_VAL=$(chage -l student 2>/dev/null | grep -i "Maximum" | awk -F: '{print $2}' | tr -d ' ' || echo "0")
if [ "$CHAGE_VAL" == "90" ] && grep -q "student.*nofile.*4096" /etc/security/limits.conf; then
  echo -e "${GREEN}[PASS] Q20: Password max age (90 days) and nofile limits verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: chage max age is '$CHAGE_VAL' (expected 90) or limits.conf missing.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: Git Repo
```bash
mkdir -p /var/tmp/mock-lfcs-1/git-repo && cd /var/tmp/mock-lfcs-1/git-repo
git init -b main
echo "# Master Repo" > README.md
git add README.md && git commit -m "initial commit"
git checkout -b feature
echo "new feature" > feature.txt
git add feature.txt && git commit -m "add feature"
git checkout main
git merge feature
```

#### Q2: Custom Service
```bash
sudo tee /usr/local/bin/mock_monitor.sh << 'EOF'
#!/bin/bash
while true; do date >> /var/tmp/mock-lfcs-1/monitor.log; sleep 5; done
EOF
sudo chmod +x /usr/local/bin/mock_monitor.sh

sudo tee /etc/systemd/system/mock-monitor.service << 'EOF'
[Unit]
Description=Mock Monitor Service
[Service]
ExecStart=/usr/local/bin/mock_monitor.sh
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now mock-monitor.service
```

#### Q3: Find Large Files
```bash
find /var/tmp/mock-lfcs-1 -type f -mtime -7 -size +100k > /var/tmp/mock-lfcs-1/large-files.txt
```

#### Q4: SSL Cert Info
```bash
openssl x509 -in /var/tmp/mock-lfcs-1/exam.crt -noout -subject -issuer -dates > /var/tmp/mock-lfcs-1/cert-info.txt
```

#### Q5: Swappiness
```bash
echo "vm.swappiness = 10" | sudo tee /etc/sysctl.d/99-swappiness.conf
sudo sysctl --system
```

#### Q6: Cron Job
```bash
(crontab -u student -l 2>/dev/null; echo "30 2 * * 1-5 /bin/echo 'Cron job executed'") | crontab -u student -
```

#### Q7: Package Files
```bash
dpkg -L tar > /var/tmp/mock-lfcs-1/pkg-files.txt
```

#### Q8: Background Process PID
```bash
sleep 9999 &
echo $! > /var/tmp/mock-lfcs-1/sleep.pid
```

#### Q9: Run Container
```bash
docker run -d --name mock-web -p 8088:80 nginx:alpine || podman run -d --name mock-web -p 8088:80 nginx:alpine
```

#### Q10: Hosts Entry
```bash
echo "127.0.0.1 exam.local" | sudo tee -a /etc/hosts
```

#### Q11: Time Status
```bash
timedatectl status > /var/tmp/mock-lfcs-1/time-status.txt
```

#### Q12: Listening Ports
```bash
ss -tlpn > /var/tmp/mock-lfcs-1/listening-ports.txt
```

#### Q13: SSH Hardening Drop-in
```bash
sudo mkdir -p /etc/ssh/sshd_config.d
sudo tee /etc/ssh/sshd_config.d/99-hardening.conf << 'EOF'
PermitRootLogin no
MaxAuthTries 3
EOF
sudo sshd -t
```

#### Q14: Firewall Status
```bash
sudo ufw status verbose > /var/tmp/mock-lfcs-1/firewall-rules.txt || sudo iptables -L -n > /var/tmp/mock-lfcs-1/firewall-rules.txt
```

#### Q15: Ext4 Disk Image
```bash
dd if=/dev/zero of=/var/tmp/mock-lfcs-1/disk1.img bs=1M count=100
mkfs.ext4 -F /var/tmp/mock-lfcs-1/disk1.img
```

#### Q16 & Q17: LVM Setup & Extend
```bash
LOOP=$(sudo losetup -f --show /var/tmp/mock-lfcs-1/disk1.img)
sudo pvcreate $LOOP
sudo vgcreate mock-vg $LOOP
sudo lvcreate -L 50M -n mock-lv mock-vg
sudo mkfs.ext4 /dev/mock-vg/mock-lv
mkdir -p /var/tmp/mock-lfcs-1/lvm-mount
sudo mount /dev/mock-vg/mock-lv /var/tmp/mock-lfcs-1/lvm-mount
# Q17 extend
sudo lvextend -L 80M /dev/mock-vg/mock-lv
sudo resize2fs /dev/mock-vg/mock-lv
```

#### Q18: Swapfile
```bash
sudo dd if=/dev/zero of=/var/tmp/mock-lfcs-1/swapfile bs=1M count=64
sudo chmod 600 /var/tmp/mock-lfcs-1/swapfile
sudo mkswap /var/tmp/mock-lfcs-1/swapfile
sudo swapon /var/tmp/mock-lfcs-1/swapfile
```

#### Q19: Users, Group and ACL
```bash
sudo groupadd -g 3001 infrateam
sudo useradd -u 2001 -m devops
sudo useradd -u 2002 -m tester
sudo setfacl -m g:infrateam:rwx /var/tmp/mock-lfcs-1/shared
```

#### Q20: Limits & Password Aging
```bash
echo "student soft nofile 4096" | sudo tee -a /etc/security/limits.conf
echo "student hard nofile 4096" | sudo tee -a /etc/security/limits.conf
sudo chage -M 90 student
```""",
        "reset": """sudo systemctl stop mock-monitor.service 2>/dev/null || true
sudo systemctl disable mock-monitor.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/mock-monitor.service /usr/local/bin/mock_monitor.sh
sudo systemctl daemon-reload
sudo swapoff /var/tmp/mock-lfcs-1/swapfile 2>/dev/null || true
sudo umount /var/tmp/mock-lfcs-1/lvm-mount 2>/dev/null || true
sudo lvremove -f /dev/mock-vg/mock-lv 2>/dev/null || true
sudo vgremove -f mock-vg 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-1" | cut -d: -f1); do
  sudo losetup -d "$l" 2>/dev/null || true
done
docker rm -f mock-web 2>/dev/null || podman rm -f mock-web 2>/dev/null || true
sudo userdel -r devops 2>/dev/null || true
sudo userdel -r tester 2>/dev/null || true
sudo groupdel infrateam 2>/dev/null || true
crontab -u student -r 2>/dev/null || true
sudo sed -i '/exam.local/d' /etc/hosts
sudo sed -i '/student.*nofile/d' /etc/security/limits.conf
sudo rm -rf /var/tmp/mock-lfcs-1 /etc/sysctl.d/99-swappiness.conf /etc/ssh/sshd_config.d/99-hardening.conf""",
    },
    {
        "lab_id": 'mock-lfcs-2',
        "track": 'LFCS',
        "date": '2026-11-18',
        "title": 'LFCS Full-Scale Timed Mock Exam 2',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# LFCS Full-Scale Timed Mock Exam 2

**Passing Score:** 67% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Environment:** VirtualBox Ubuntu LFCS VM (`student@172.16.16.16`)

---

### Linux Foundation Official Domain Weights:
1. **Operations Deployment (25%)**
   - Configure kernel parameters, persistent and non-persistent
   - Diagnose, identify, manage, and troubleshoot processes and services
   - Manage or schedule jobs for executing commands
   - Search for, install, validate, and maintain software packages or repositories
   - Recover from hardware, operating system, or filesystem failures
   - Manage Virtual Machines (libvirt)
   - Configure container engines, create and manage containers
   - Create and enforce MAC using SELinux
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Set and synchronize system time using time servers
   - Monitor and troubleshoot networking
   - Configure the OpenSSH server and client
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Use remote filesystems and network block devices
   - Configure and manage swap space
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Basic Git Operations
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Determine application and service specific constraints
   - Troubleshoot diskspace issues
   - Work with SSL certificates
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits
   - Configure and manage ACLs
   - Configure the system to use LDAP user and group accounts

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** An automated deployment pipeline requires applying text modifications to an application configuration file:
  - In `/var/tmp/mock-lfcs-2/app.conf`, change the listener port by updating line `PORT = 8080` to `PORT = 9000`.
  - Remove all lines containing the string `DEBUG`.
  - Insert a new configuration line `ENV = production` immediately following the section header `[app]`.
  - Save the changes directly to `/var/tmp/mock-lfcs-2/app.conf`.
- **Q2:** Analyze system log files to identify active services generating excessive log volume:
  - Process the log entries in `/var/tmp/mock-lfcs-2/sample_syslog`.
  - Calculate message frequencies by process name and determine the top 3 processes generating the most log messages.
  - Save the top process ranking into `/var/tmp/mock-lfcs-2/top_loggers.txt`.
- **Q3:** Generate and apply a unified diff patch between software source revisions:
  - Compare `/var/tmp/mock-lfcs-2/fileA` and `/var/tmp/mock-lfcs-2/fileB` and create a unified diff patch file saved to `/var/tmp/mock-lfcs-2/patch.diff`.
  - Apply the generated patch to target file `/var/tmp/mock-lfcs-2/fileTarget` so its contents are updated to match `fileB`.
- **Q4:** Conduct a storage utilization audit under the system log directory:
  - Inspect directory `/var/log` to find the 3 largest regular files.
  - Record their full file paths and sizes into `/var/tmp/mock-lfcs-2/largest_files.txt`.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Schedule a periodic maintenance task using native systemd timer units:
  - Create a systemd service unit `/etc/systemd/system/mock-cleanup.service` executing `/bin/echo 'Cleaning temporary cache'`.
  - Create a companion timer unit `/etc/systemd/system/mock-cleanup.timer` scheduled to trigger every 15 minutes.
  - Reload systemd, enable the timer, and activate it so it is actively scheduled.
- **Q6:** Manage process scheduling priorities by launching and renicing a running process:
  - Start the command `sleep 600` with an initial scheduling nice value of `10`.
  - While running, dynamically adjust the process's nice priority to `15`.
  - Verify the modified scheduling priority and save the process PID and nice level to `/var/tmp/mock-lfcs-2/nice_proc.txt`.
- **Q7:** Route application facility log messages to a dedicated log destination:
  - In `/etc/rsyslog.d/`, create configuration file `40-custom.conf`.
  - Configure the logging daemon to route all messages from facility `local5.*` to file `/var/log/custom-app.log`.
  - Restart or reload the rsyslog daemon to apply the new logging rule.
- **Q8:** Document the operating system target configuration:
  - Query the system service manager to identify the current default systemd target.
  - Write the exact default target name into file `/var/tmp/mock-lfcs-2/boot-target.txt`.
- **Q9:** Prevent unexpected major software updates by configuring package pinning:
  - In directory `/etc/apt/preferences.d/`, create an APT preferences file named `pin-package`.
  - Configure package pinning for package `nginx` setting its package pin priority to `999`.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Create a virtual network interface for localized software testing:
  - Create a virtual dummy network interface named `dummy0`.
  - Assign the IPv4 address `10.99.99.1` with subnet mask `/24` to `dummy0`.
  - Bring the interface to an `UP` state and verify its address assignment.
- **Q11:** Open inbound network access for a web service through the firewall:
  - Add an iptables packet filtering rule to allow incoming TCP traffic on destination port `8080` in the `INPUT` chain.
  - Export the active `INPUT` chain rule set with numeric addresses and ports to `/var/tmp/mock-lfcs-2/iptables.txt`.
- **Q12:** Identify the daemon bound to the remote access port for a security audit:
  - Inspect the system socket table to determine which process is listening on TCP port 22.
  - Save the process name and process ID (PID) to `/var/tmp/mock-lfcs-2/ssh-proc.txt`.
- **Q13:** Verify DNS resolver configuration:
  - Query the local DNS stub resolver status.
  - Record the current active upstream DNS server IP address into `/var/tmp/mock-lfcs-2/dns-server.txt`.
- **Q14:** Configure static network routing for remote network communication:
  - Add a static route for destination network `192.168.100.0/24`.
  - Route traffic via next-hop gateway `10.99.99.254` reachable over interface `dummy0` (enable onlink if required).
  - Confirm the route is registered in the kernel routing table.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Create a point-in-time storage snapshot for backup verification:
  - In volume group `mock-vg2`, locate logical volume `data-lv`.
  - Create a 20 Megabyte snapshot named `data-snap` of the logical volume.
  - Confirm the snapshot is active in logical volume reporting tools.
- **Q16:** Optimize disk space availability on an ext4 filesystem:
  - Examine the ext4 filesystem image at `/var/tmp/mock-lfcs-2/tunable.img`.
  - Modify the reserved blocks percentage allocated to the super-user so that it is reduced to `1%`.
  - Verify the change in filesystem parameters.
- **Q17:** Configure persistent filesystem mounting with performance and security options:
  - Add an entry to `/etc/fstab` to persistently mount filesystem path `/var/tmp/mock-lfcs-2/mnt-point`.
  - Apply mount options `noatime` (suppress access time updates) and `nodev` (prevent device node interpretation).
- **Q18:** Create and activate a secure virtual memory swap file:
  - Create a 128 Megabyte swap file at `/var/tmp/mock-lfcs-2/swapfile2`.
  - Set file permissions so only root has read and write privileges (`600`).
  - Format the file for swap and activate it immediately.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Implement strict password security policies for user accounts:
  - Configure password aging parameters for user `student`:
    - Maximum password lifetime: 60 days
    - Minimum days required between password changes: 7 days
    - Advance warning period prior to expiration: 14 days
  - Verify the password aging policy using account aging utilities.
- **Q20:** Establish default skeleton files for new user provisioning:
  - In the default user skeleton directory `/etc/skel`, add a file named `.custom_profile` (containing `# Custom User Profile`).
  - Create a new user account named `newhire` ensuring standard home directory initialization.
  - Confirm `/home/newhire/.custom_profile` was automatically provisioned upon account creation.""",
        "setup": """sudo rm -rf /var/tmp/mock-lfcs-2 /etc/rsyslog.d/40-custom.conf /etc/apt/preferences.d/pin-package /etc/skel/.custom_profile
sudo mkdir -p /var/tmp/mock-lfcs-2/mnt-point && sudo chown -R student:student /var/tmp/mock-lfcs-2 && sudo chmod -R 777 /var/tmp/mock-lfcs-2
# Q1 sample
cat << 'EOF' > /var/tmp/mock-lfcs-2/app.conf
[app]
HOST = 0.0.0.0
PORT = 8080
DEBUG = true
TIMEOUT = 30
EOF
# Q2 syslog sample
cat << 'EOF' > /var/tmp/mock-lfcs-2/sample_syslog
Sep 14 10:00:01 host sshd[100]: session opened
Sep 14 10:00:02 host kernel: [0.123] disk ok
Sep 14 10:00:03 host sshd[101]: session closed
Sep 14 10:00:04 host systemd[1]: started timer
Sep 14 10:00:05 host sshd[102]: login ok
EOF
# Q3 diff sample
echo -e "line1
line2" > /var/tmp/mock-lfcs-2/fileA
echo -e "line1
line2_modified
line3" > /var/tmp/mock-lfcs-2/fileB
cp /var/tmp/mock-lfcs-2/fileA /var/tmp/mock-lfcs-2/fileTarget
# Q15 LVM setup
dd if=/dev/zero of=/var/tmp/mock-lfcs-2/lvm2.img bs=1M count=100 2>/dev/null || true
LOOP=$(sudo losetup -f --show /var/tmp/mock-lfcs-2/lvm2.img 2>/dev/null || true)
if [ -n "$LOOP" ]; then
  sudo pvcreate "$LOOP" 2>/dev/null || true
  sudo vgcreate mock-vg2 "$LOOP" 2>/dev/null || true
  sudo lvcreate -L 40M -n data-lv mock-vg2 2>/dev/null || true
  sudo mkfs.ext4 /dev/mock-vg2/data-lv 2>/dev/null || true
fi
# Q16 tunable image
dd if=/dev/zero of=/var/tmp/mock-lfcs-2/tunable.img bs=1M count=50 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-2/tunable.img 2>/dev/null || true
sudo userdel -r newhire 2>/dev/null || true""",
        "verify": """# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 2 against Linux Foundation Domain Weights...${NC}"

# Q1: Sed editing (Essential Commands - 20%)
CONF1=$(cat /var/tmp/mock-lfcs-2/app.conf 2>/dev/null || true)
if echo "$CONF1" | grep -q "PORT = 9000" && echo "$CONF1" | grep -q "ENV = production" && ! echo "$CONF1" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Q1: app.conf sed editing verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: app.conf modifications incomplete.${NC}"
fi

# Q2: Top loggers (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-2/top_loggers.txt ] && grep -q "sshd" /var/tmp/mock-lfcs-2/top_loggers.txt; then
  echo -e "${GREEN}[PASS] Q2: top_loggers.txt syslog analysis verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: top_loggers.txt missing or empty.${NC}"
fi

# Q3: Patch (Essential Commands - 20%)
if grep -q "line2_modified" /var/tmp/mock-lfcs-2/fileTarget 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q3: Patch successfully applied to fileTarget.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: fileTarget not patched.${NC}"
fi

# Q4: Largest files (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-2/largest_files.txt ] && [ -s /var/tmp/mock-lfcs-2/largest_files.txt ]; then
  echo -e "${GREEN}[PASS] Q4: largest_files.txt created.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: largest_files.txt missing.${NC}"
fi

# Q5: Systemd timer (Operations Deployment - 25%)
if systemctl is-active mock-cleanup.timer &>/dev/null; then
  echo -e "${GREEN}[PASS] Q5: mock-cleanup.timer is active.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: mock-cleanup.timer not active.${NC}"
fi

# Q6: Nice process (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-2/nice_proc.txt ] && grep -q "15" /var/tmp/mock-lfcs-2/nice_proc.txt; then
  echo -e "${GREEN}[PASS] Q6: Process nice level 15 recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: nice_proc.txt missing or lacks nice 15.${NC}"
fi

# Q7: Rsyslog rule (Operations Deployment - 25%)
if [ -f /etc/rsyslog.d/40-custom.conf ] && grep -q "local5" /etc/rsyslog.d/40-custom.conf; then
  echo -e "${GREEN}[PASS] Q7: rsyslog rule verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: 40-custom.conf missing.${NC}"
fi

# Q8: Default target (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-2/boot-target.txt ] && grep -q "\.target" /var/tmp/mock-lfcs-2/boot-target.txt; then
  echo -e "${GREEN}[PASS] Q8: boot-target.txt recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: boot-target.txt missing.${NC}"
fi

# Q9: Apt pinning (Operations Deployment - 25%)
if [ -f /etc/apt/preferences.d/pin-package ] && grep -q "999" /etc/apt/preferences.d/pin-package; then
  echo -e "${GREEN}[PASS] Q9: APT package pin verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: pin-package missing or lacks 999.${NC}"
fi

# Q10: Dummy interface (Networking - 25%)
if ip link show dummy0 &>/dev/null; then
  echo -e "${GREEN}[PASS] Q10: Interface dummy0 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: dummy0 interface missing.${NC}"
fi

# Q11: IPTables rule (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/iptables.txt ] && grep -q "8080" /var/tmp/mock-lfcs-2/iptables.txt; then
  echo -e "${GREEN}[PASS] Q11: IPTables rule on port 8080 recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: iptables.txt missing or lacks 8080.${NC}"
fi

# Q12: SSH PID (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/ssh-proc.txt ] && grep -qi "sshd" /var/tmp/mock-lfcs-2/ssh-proc.txt; then
  echo -e "${GREEN}[PASS] Q12: sshd listening PID recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: ssh-proc.txt missing.${NC}"
fi

# Q13: DNS server (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/dns-server.txt ] && [ -s /var/tmp/mock-lfcs-2/dns-server.txt ]; then
  echo -e "${GREEN}[PASS] Q13: dns-server.txt recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: dns-server.txt missing.${NC}"
fi

# Q14: Static route (Networking - 25%)
if ip route show 2>/dev/null | grep -q "192.168.100.0/24.*10.99.99.254"; then
  echo -e "${GREEN}[PASS] Q14: Static route for 192.168.100.0/24 via 10.99.99.254 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: Static route for 192.168.100.0/24 missing.${NC}"
fi

# Q15: LVM Snapshot (Storage - 20%)
if lvs mock-vg2/data-snap &>/dev/null; then
  echo -e "${GREEN}[PASS] Q15: LVM snapshot data-snap verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: LVM snapshot data-snap missing.${NC}"
fi

# Q16: Tune2fs reserved blocks (Storage - 20%)
RES_BLOCKS=$(sudo tune2fs -l /var/tmp/mock-lfcs-2/tunable.img 2>/dev/null | grep -i "Reserved block count:" | awk '{print $NF}' || echo "0")
if [ "$RES_BLOCKS" -eq 128 ]; then
  echo -e "${GREEN}[PASS] Q16: tune2fs 1% reserved blocks verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: tune2fs reserved blocks: $RES_BLOCKS (expected 128 blocks / 1%).${NC}"
fi

# Q17: Fstab entry (Storage - 20%)
if grep -q "mnt-point.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Q17: /etc/fstab entry verified with noatime.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: /etc/fstab lacks mnt-point entry.${NC}"
fi

# Q18: Swapfile (Storage - 20%)
if swapon --show 2>/dev/null | grep -q "mock-lfcs-2/swapfile2"; then
  echo -e "${GREEN}[PASS] Q18: Swap file swapfile2 verified active.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: swapfile2 missing or not active.${NC}"
fi

# Q19: Chage password aging (Users and Groups - 10%)
CHAGE_OUT=$(chage -l student 2>/dev/null || true)
if echo "$CHAGE_OUT" | grep -q "Maximum.*60" && echo "$CHAGE_OUT" | grep -q "Minimum.*7"; then
  echo -e "${GREEN}[PASS] Q19: Password aging policy (60/7/14) verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: chage aging settings mismatch.${NC}"
fi

# Q20: Skeleton & user (Users and Groups - 10%)
if id newhire &>/dev/null && [ -f /home/newhire/.custom_profile ]; then
  echo -e "${GREEN}[PASS] Q20: User newhire and populated skeleton verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: user newhire missing or .custom_profile not populated.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: Sed Editing
```bash
sed -i 's/PORT = 8080/PORT = 9000/' /var/tmp/mock-lfcs-2/app.conf
sed -i '/DEBUG/d' /var/tmp/mock-lfcs-2/app.conf
sed -i '/\[app\]/a ENV = production' /var/tmp/mock-lfcs-2/app.conf
```

#### Q2: Syslog Pipeline
```bash
awk '{print $5}' /var/tmp/mock-lfcs-2/sample_syslog | sed 's/\[.*//' | sort | uniq -c | sort -nr | head -n 3 > /var/tmp/mock-lfcs-2/top_loggers.txt
```

#### Q3: Diff and Patch
```bash
diff -u /var/tmp/mock-lfcs-2/fileA /var/tmp/mock-lfcs-2/fileB > /var/tmp/mock-lfcs-2/patch.diff
patch /var/tmp/mock-lfcs-2/fileTarget < /var/tmp/mock-lfcs-2/patch.diff
```

#### Q4: Largest Files
```bash
sudo find /var/log -type f -exec ls -s {} + 2>/dev/null | sort -nr | head -n 3 > /var/tmp/mock-lfcs-2/largest_files.txt
```

#### Q5: Systemd Timer
```bash
sudo tee /etc/systemd/system/mock-cleanup.service << 'EOF'
[Unit]
Description=Mock Cleanup Service
[Service]
Type=oneshot
ExecStart=/bin/echo "cleanup run"
EOF

sudo tee /etc/systemd/system/mock-cleanup.timer << 'EOF'
[Unit]
Description=Mock Cleanup Timer
[Timer]
OnCalendar=*:0/15
Persistent=true
[Install]
WantedBy=timers.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now mock-cleanup.timer
```

#### Q6: Renice Process
```bash
sleep 600 &
PID=$!
sudo renice -n 15 -p $PID
ps -o pid,ni,comm -p $PID > /var/tmp/mock-lfcs-2/nice_proc.txt
```

#### Q7: Rsyslog Rule
```bash
echo "local5.* /var/log/custom-app.log" | sudo tee /etc/rsyslog.d/40-custom.conf
sudo systemctl restart rsyslog
```

#### Q8: Default Target
```bash
systemctl get-default > /var/tmp/mock-lfcs-2/boot-target.txt
```

#### Q9: Apt Pinning
```bash
sudo tee /etc/apt/preferences.d/pin-package << 'EOF'
Package: nginx
Pin: release *
Pin-Priority: 999
EOF
```

#### Q10: Dummy Interface
```bash
sudo ip link add dummy0 type dummy
sudo ip addr add 10.99.99.1/24 dev dummy0
sudo ip link set dummy0 up
```

#### Q11: IPTables Rule
```bash
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo iptables -L INPUT -n > /var/tmp/mock-lfcs-2/iptables.txt
```

#### Q12: SSH PID
```bash
ss -tlpn | grep ":22 " > /var/tmp/mock-lfcs-2/ssh-proc.txt
```

#### Q13: DNS Server
```bash
resolvectl status > /var/tmp/mock-lfcs-2/dns-server.txt || systemd-resolve --status > /var/tmp/mock-lfcs-2/dns-server.txt
```

#### Q14: Static Route
```bash
sudo ip route add 192.168.100.0/24 via 10.99.99.254 dev dummy0 onlink
```

#### Q15: LVM Snapshot
```bash
sudo lvcreate -s -L 20M -n data-snap /dev/mock-vg2/data-lv
```

#### Q16: Tune2fs
```bash
sudo tune2fs -m 1 /var/tmp/mock-lfcs-2/tunable.img
```

#### Q17: Fstab Entry
```bash
echo "/var/tmp/mock-lfcs-2/mnt-point /var/tmp/mock-lfcs-2/mnt-point none bind,noatime,nodev 0 0" | sudo tee -a /etc/fstab
```

#### Q18: Swap Space
```bash
sudo dd if=/dev/zero of=/var/tmp/mock-lfcs-2/swapfile2 bs=1M count=128
sudo chmod 600 /var/tmp/mock-lfcs-2/swapfile2
sudo mkswap /var/tmp/mock-lfcs-2/swapfile2
sudo swapon /var/tmp/mock-lfcs-2/swapfile2
```

#### Q19: Password Aging
```bash
sudo chage -M 60 -m 7 -W 14 student
```

#### Q20: Skeleton & New User
```bash
echo "export LAB_ENV=lfcs-certified" | sudo tee /etc/skel/.custom_profile
sudo useradd -m newhire
```""",
        "reset": """sudo systemctl stop mock-cleanup.timer 2>/dev/null || true
sudo systemctl disable mock-cleanup.timer 2>/dev/null || true
sudo rm -f /etc/systemd/system/mock-cleanup.*
sudo systemctl daemon-reload
sudo ip route del 192.168.100.0/24 dev dummy0 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo swapoff /var/tmp/mock-lfcs-2/swapfile2 2>/dev/null || true
sudo lvremove -f /dev/mock-vg2/data-snap 2>/dev/null || true
sudo lvremove -f /dev/mock-vg2/data-lv 2>/dev/null || true
sudo vgremove -f mock-vg2 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-2" | cut -d: -f1); do
  sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r newhire 2>/dev/null || true
sudo rm -f /etc/skel/.custom_profile
sudo sed -i '/mnt-point/d' /etc/fstab
sudo rm -rf /var/tmp/mock-lfcs-2 /etc/rsyslog.d/40-custom.conf /etc/apt/preferences.d/pin-package""",
    },
    {
        "lab_id": 'mock-lfcs-3',
        "track": 'LFCS',
        "date": '2026-11-24',
        "title": 'LFCS Full-Scale Timed Mock Exam 3',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# LFCS Full-Scale Timed Mock Exam 3

**Passing Score:** 67% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Environment:** VirtualBox Ubuntu LFCS VM (`student@172.16.16.16`)

---

### Linux Foundation Official Domain Weights:
1. **Operations Deployment (25%)**
   - Configure kernel parameters, persistent and non-persistent
   - Diagnose, identify, manage, and troubleshoot processes and services
   - Manage or schedule jobs for executing commands
   - Search for, install, validate, and maintain software packages or repositories
   - Manage Virtual Machines and containers
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Monitor and troubleshoot networking
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Text manipulation and log analysis
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Archive and compress files
   - Work with SSL certificates and Git
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits and granular privilege escalation (sudoers)
   - Configure and manage ACLs and special permissions (SGID, sticky bit)

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** An Apache HTTP web server log file `/var/tmp/mock-lfcs-3/web_access.log` records client interactions.
  - Parse the log file to extract all unique client IP addresses (column 1) that received HTTP client/server error response status codes (`4xx` or `5xx` in column 9).
  - Sort the IP addresses numerically and save the unique list into `/var/tmp/mock-lfcs-3/error_ips.txt`.
- **Q2:** Generate an SSL Certificate Signing Request (CSR) and Private Key for an internal service:
  - Generate an RSA 2048-bit private key without passphrase at `/var/tmp/mock-lfcs-3/server.key`.
  - Create a Certificate Signing Request (CSR) at `/var/tmp/mock-lfcs-3/server.csr` with Common Name `lfcs.local` and Subject Alternative Names `DNS:lfcs.local,DNS:api.lfcs.local`.
- **Q3:** Create a multi-threaded compressed archive and verify its integrity:
  - Archive directory `/var/tmp/mock-lfcs-3/source_data` into `/var/tmp/mock-lfcs-3/backup.tar.xz` using `tar` with multithreaded `xz` compression (`-T0`).
  - Calculate the SHA256 checksum of `/var/tmp/mock-lfcs-3/backup.tar.xz` and save it to `/var/tmp/mock-lfcs-3/backup.tar.xz.sha256` in standard checksum format (`<sha256sum>  <filename>`).
- **Q4:** In Git repository `/var/tmp/mock-lfcs-3/git-app`:
  - Create an annotated release tag named `v1.2.0` on the current HEAD commit with annotation message `"Production Release 1.2.0"`.
  - Create and checkout a new branch named `release-1.2` starting from this tag.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Enforce cgroup resource control drop-in for systemd service `mock-worker.service`:
  - Create a systemd drop-in configuration directory at `/etc/systemd/system/mock-worker.service.d/` and drop-in file `limits.conf`.
  - Configure resource limits: `MemoryMax=64M` and `CPUQuota=40%`.
  - Reload systemd daemon configuration and restart `mock-worker.service`.
- **Q6:** Permanently blacklist legacy kernel module `cramfs`:
  - Create configuration file `/etc/modprobe.d/blacklist-cramfs.conf` containing `blacklist cramfs` and `install cramfs /bin/true`.
  - Ensure the module is unloaded from the running kernel.
- **Q7:** Query systemd journal logs to diagnose priority failures:
  - Use `journalctl` to extract all system log messages with priority level `err` or higher (`-p err..emerg`) generated since `2026-01-01`.
  - Save the extracted diagnostic log entries to `/var/tmp/mock-lfcs-3/system_errors.log`.
- **Q8:** Implement a graceful daemon reload script:
  - A running application PID is recorded in `/var/run/mock-app.pid`.
  - Create an executable bash script `/usr/local/bin/reload_mock_app.sh`.
  - When executed, the script must read `/var/run/mock-app.pid`, send signal `SIGHUP` (`kill -HUP $PID`) to trigger configuration reload without killing the daemon, and append `"RELOAD SIGNAL SENT"` with the timestamp to `/var/tmp/mock-lfcs-3/signal.log`.
- **Q9:** Container lifecycle and restart management with Podman:
  - Launch a detached Podman container named `mock-web-c3` from image `docker.io/library/nginx:alpine`.
  - Configure restart policy `--restart always` and map host port `8085` to container port `80` (`-p 8085:80`).
  - Verify the container status is running.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Configure Nginx as an HTTP Reverse Proxy Load Balancer:
  - Two backend applications are running on ports `8081` and `8082`.
  - Configure Nginx in `/etc/nginx/conf.d/proxy-balance.conf` with upstream `backend_nodes` distributing requests across `127.0.0.1:8081` and `127.0.0.1:8082` using round-robin.
  - Configure a server block listening on port `8080` that proxies all incoming requests (`location /`) to `http://backend_nodes`.
  - Test configuration syntax and reload or restart Nginx.
- **Q11:** Linux Network Bridge Configuration:
  - Create a network bridge interface named `br0` (`ip link add br0 type bridge`).
  - Attach interface `veth-br1` as a slave port to `br0` (`ip link set veth-br1 master br0`).
  - Assign IP address `192.168.50.1/24` to `br0` and bring both `br0` and `veth-br1` up.
- **Q12:** Port Redirection with Iptables NAT:
  - In `iptables` NAT table, append a PREROUTING rule to redirect incoming TCP traffic destined for port `8443` to local port `443` (`-p tcp --dport 8443 -j REDIRECT --to-ports 443`).
  - Save the active NAT table rules to `/var/tmp/mock-lfcs-3/nat-rules.txt`.
- **Q13:** Network Packet Capture with `tcpdump`:
  - Run `tcpdump` to capture exactly 5 TCP packets arriving on loopback interface `lo` for destination port `9999`.
  - Save the captured raw packets to `/var/tmp/mock-lfcs-3/traffic.pcap`.
- **Q14:** Static Network Route with Metric:
  - Add a static network route for destination network `10.150.0.0/16` via gateway `10.99.99.1` on device `dummy0` with a specific route metric of `150`.
  - Ensure the route appears in the active kernel routing table.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Storage Performance and I/O Activity Monitoring:
  - Use `iostat -x -d 1 3` to collect extended disk utilization statistics and write the output to `/var/tmp/mock-lfcs-3/io-report.txt`.
  - Use `sar -d 1 3` to record real-time block I/O activity and save the report to `/var/tmp/mock-lfcs-3/sar-disk.txt`.
  - Both reports must include device metrics (`%util` or `await`).
- **Q16:** Filesystem Automounter (`autofs`) Direct Map:
  - Configure `autofs` direct automount:
    - Create direct master map configuration `/etc/auto.master.d/direct.autofs` containing `/- /etc/auto.direct --timeout=60`.
    - In `/etc/auto.direct`, configure direct mountpoint `/mnt/auto-data` pointing to ext4 disk `/var/tmp/mock-lfcs-3/auto.img` with options `-fstype=ext4,loop,rw`.
    - Restart `autofs` (`systemctl restart autofs`) and verify accessing `/mnt/auto-data` automatically mounts the volume.
- **Q17:** LVM Thin Provisioning:
  - Inside Volume Group `mock-vg3`, create an LVM thin pool named `mock-pool` with data size `50MB` (`lvcreate -L 50M -T mock-vg3/mock-pool`).
  - Create a thin provisioned volume named `mock-thin` with virtual size `150MB` from `mock-pool` (`lvcreate -V 150M -T mock-vg3/mock-pool -n mock-thin`).
  - Format `/dev/mock-vg3/mock-thin` with filesystem `ext4`.
- **Q18:** Persistent Mount by UUID with Security Mount Options:
  - Obtain the filesystem UUID of `/var/tmp/mock-lfcs-3/secure_store.img` using `blkid`.
  - Create mount directory `/mnt/secure-data`.
  - Configure `/etc/fstab` to persistently mount the filesystem by its UUID (`UUID=<uuid>`) to `/mnt/secure-data` with options `noexec,nosuid,nodev`.
  - Mount the filesystem using `mount -a`.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Granular Sudoers Delegation (`/etc/sudoers.d/`):
  - User `developer` requires administrative privileges restricted strictly to commands `/usr/bin/systemctl restart nginx` and `/usr/bin/journalctl`.
  - Create a sudoers drop-in file at `/etc/sudoers.d/90-developer` with file mode `0440`.
  - Grant user `developer` execution privileges for those two commands without requiring a password prompt (`NOPASSWD:`).
- **Q20:** SGID and Sticky Bit Collaborative Workspace:
  - Create a team directory at `/var/tmp/mock-lfcs-3/team_collab` owned by user `student` and group `devteam`.
  - Set permissions to `2775` (rwxrwsr-x with SGID set).
  - Create subdirectory `/var/tmp/mock-lfcs-3/team_collab/dropzone` with permissions `1777` (rwxrwxrwt with sticky bit set) so users cannot remove files owned by others.""",
        "setup": """sudo rm -rf /var/tmp/mock-lfcs-3 /etc/systemd/system/mock-worker.service.d /etc/modprobe.d/blacklist-cramfs.conf /etc/nginx/conf.d/proxy-balance.conf /etc/auto.master.d/direct.autofs /etc/auto.direct /etc/sudoers.d/90-developer /var/run/mock-app.pid
sudo mkdir -p /var/tmp/mock-lfcs-3/source_data /var/tmp/mock-lfcs-3/git-app /mnt/secure-data
sudo chown -R student:student /var/tmp/mock-lfcs-3

# Q1 sample log
cat << 'EOF' > /var/tmp/mock-lfcs-3/web_access.log
192.168.1.10 - - [10/Nov/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 4523
192.168.1.50 - - [10/Nov/2026:10:00:05 +0000] "GET /admin HTTP/1.1" 403 342
10.0.0.12 - - [10/Nov/2026:10:01:10 +0000] "POST /api/v1/login HTTP/1.1" 500 523
172.16.0.5 - - [10/Nov/2026:10:01:25 +0000] "GET /nonexistent HTTP/1.1" 404 289
192.168.1.10 - - [10/Nov/2026:10:02:00 +0000] "GET /style.css HTTP/1.1" 200 1204
10.0.0.12 - - [10/Nov/2026:10:02:15 +0000] "GET /broken HTTP/1.1" 502 189
EOF

# Q3 sample source files
echo "Project source code file 1" > /var/tmp/mock-lfcs-3/source_data/module1.py
echo "Configuration parameters file 2" > /var/tmp/mock-lfcs-3/source_data/config.json

# Q4 sample git repo
git -C /var/tmp/mock-lfcs-3/git-app init -b main 2>/dev/null || (git -C /var/tmp/mock-lfcs-3/git-app init && git -C /var/tmp/mock-lfcs-3/git-app checkout -b main)
echo "print('App v1.0')" > /var/tmp/mock-lfcs-3/git-app/app.py
git -C /var/tmp/mock-lfcs-3/git-app add app.py
git -C /var/tmp/mock-lfcs-3/git-app -c user.name="LFCS Admin" -c user.email="admin@lfcs.local" commit -m "Initial commit v1.0" 2>/dev/null || true

# Q5 worker service
sudo tee /etc/systemd/system/mock-worker.service << 'EOF'
[Unit]
Description=Mock Worker Service
[Service]
Type=simple
ExecStart=/usr/bin/sleep infinity
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now mock-worker.service 2>/dev/null || true

# Q7 generate test error log
logger -p user.err "LFCS_MOCK3_CRITICAL_ERR system failure simulation" 2>/dev/null || true

# Q8 mock app daemon with trap
(trap 'echo "RELOAD_ACK" >> /var/tmp/mock-lfcs-3/app_ack.log' HUP; while true; do sleep 1; done) &
echo $! | sudo tee /var/run/mock-app.pid >/dev/null

# Q10 start minimal backends on 8081 and 8082
mkdir -p /var/tmp/mock-lfcs-3/b1 /var/tmp/mock-lfcs-3/b2
echo "Backend 1 Response" > /var/tmp/mock-lfcs-3/b1/index.html
echo "Backend 2 Response" > /var/tmp/mock-lfcs-3/b2/index.html
(cd /var/tmp/mock-lfcs-3/b1 && python3 -m http.server 8081 &>/dev/null) &
(cd /var/tmp/mock-lfcs-3/b2 && python3 -m http.server 8082 &>/dev/null) &

# Q11 dummy interface for bridge
sudo ip link del veth-br1 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
sudo ip link add veth-br1 type dummy 2>/dev/null || true

# Q14 dummy0 interface for routing
sudo modprobe dummy 2>/dev/null || true
sudo ip link add dummy0 type dummy 2>/dev/null || true
sudo ip addr add 10.99.99.1/24 dev dummy0 2>/dev/null || true
sudo ip link set dummy0 up 2>/dev/null || true

# Q16 autofs image
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/auto.img bs=1M count=40 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-3/auto.img 2>/dev/null || true
mkdir -p /tmp/tmp_auto
sudo mount -o loop /var/tmp/mock-lfcs-3/auto.img /tmp/tmp_auto 2>/dev/null || true
echo "autofs verification success" | sudo tee /tmp/tmp_auto/auto_test.txt >/dev/null
sudo umount /tmp/tmp_auto 2>/dev/null || true
rm -rf /tmp/tmp_auto

# Q17 thin storage image & VG
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/thin_storage.img bs=1M count=100 2>/dev/null || true
LOOP_THIN=$(sudo losetup -f --show /var/tmp/mock-lfcs-3/thin_storage.img 2>/dev/null || true)
if [ -n "$LOOP_THIN" ]; then
    sudo pvcreate "$LOOP_THIN" 2>/dev/null || true
    sudo vgcreate mock-vg3 "$LOOP_THIN" 2>/dev/null || true
fi

# Q18 secure store image
dd if=/dev/zero of=/var/tmp/mock-lfcs-3/secure_store.img bs=1M count=50 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-3/secure_store.img 2>/dev/null || true

# Q19 user developer
sudo userdel -r developer 2>/dev/null || true
sudo useradd -m developer 2>/dev/null || true

# Q20 devteam group
sudo groupadd devteam 2>/dev/null || true""",
        "verify": """# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 3 against Linux Foundation Domain Weights...${NC}"

# Q1: Web Server Error Log Parsing (Essential Commands - 20%)
if [ -s /var/tmp/mock-lfcs-3/error_ips.txt ] && grep -q "192.168.1.50" /var/tmp/mock-lfcs-3/error_ips.txt && grep -q "10.0.0.12" /var/tmp/mock-lfcs-3/error_ips.txt && ! grep -q "192.168.1.10" /var/tmp/mock-lfcs-3/error_ips.txt; then
  echo -e "${GREEN}[PASS] Q1: error_ips.txt web log analysis verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: error_ips.txt missing or incorrect IP filtering.${NC}"
fi

# Q2: SSL CSR with SAN (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-3/server.key ] && [ -f /var/tmp/mock-lfcs-3/server.csr ] && openssl req -in /var/tmp/mock-lfcs-3/server.csr -text -noout 2>/dev/null | grep -qi "lfcs.local"; then
  echo -e "${GREEN}[PASS] Q2: SSL private key and CSR with SAN verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: server.key or server.csr missing or invalid CN/SAN.${NC}"
fi

# Q3: Multi-threaded archive and checksum (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-3/backup.tar.xz ] && tar -tf /var/tmp/mock-lfcs-3/backup.tar.xz &>/dev/null && [ -f /var/tmp/mock-lfcs-3/backup.tar.xz.sha256 ] && (cd /var/tmp/mock-lfcs-3 && sha256sum -c backup.tar.xz.sha256 &>/dev/null); then
  echo -e "${GREEN}[PASS] Q3: backup.tar.xz multi-threaded archive and sha256 verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: backup.tar.xz or sha256 verification failed.${NC}"
fi

# Q4: Git annotated release tag and branch (Essential Commands - 20%)
if git -C /var/tmp/mock-lfcs-3/git-app tag -n 2>/dev/null | grep -q "v1.2.0.*Production Release 1.2.0" && git -C /var/tmp/mock-lfcs-3/git-app branch 2>/dev/null | grep -q "release-1.2"; then
  echo -e "${GREEN}[PASS] Q4: Git release tag v1.2.0 and release-1.2 branch verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: Git tag v1.2.0 or release-1.2 branch missing.${NC}"
fi

# Q5: Systemd cgroups drop-in limits (Operations Deployment - 25%)
MEM_MAX=$(systemctl show mock-worker.service -p MemoryMax --value 2>/dev/null || echo "0")
CPU_QUOTA=$(systemctl show mock-worker.service -p CPUQuotaPerSecUSec --value 2>/dev/null || echo "0")
if [ "$MEM_MAX" = "67108864" ] && [ "$CPU_QUOTA" = "400ms" ]; then
  echo -e "${GREEN}[PASS] Q5: systemd cgroups drop-in limits (64M, 40%) verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: mock-worker.service cgroup limits mismatch (Mem: $MEM_MAX, CPU: $CPU_QUOTA).${NC}"
fi

# Q6: Kernel module blacklisting (Operations Deployment - 25%)
if [ -f /etc/modprobe.d/blacklist-cramfs.conf ] && grep -q "blacklist cramfs" /etc/modprobe.d/blacklist-cramfs.conf && grep -q "install cramfs /bin/true" /etc/modprobe.d/blacklist-cramfs.conf && ! lsmod | grep -q "^cramfs "; then
  echo -e "${GREEN}[PASS] Q6: cramfs kernel module blacklisting verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: blacklist-cramfs.conf missing or cramfs still loaded.${NC}"
fi

# Q7: Journalctl priority failure log extraction (Operations Deployment - 25%)
if [ -s /var/tmp/mock-lfcs-3/system_errors.log ] && grep -q "LFCS_MOCK3_CRITICAL_ERR" /var/tmp/mock-lfcs-3/system_errors.log; then
  echo -e "${GREEN}[PASS] Q7: system_errors.log journalctl error extraction verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: system_errors.log missing or did not capture priority err logs.${NC}"
fi

# Q8: Graceful process reload script (Operations Deployment - 25%)
if [ -x /usr/local/bin/reload_mock_app.sh ] && /usr/local/bin/reload_mock_app.sh 2>/dev/null && sleep 1 && [ -f /var/tmp/mock-lfcs-3/signal.log ] && grep -q "RELOAD SIGNAL SENT" /var/tmp/mock-lfcs-3/signal.log && [ -f /var/tmp/mock-lfcs-3/app_ack.log ]; then
  echo -e "${GREEN}[PASS] Q8: reload_mock_app.sh signal delivery and logging verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: reload_mock_app.sh failed or did not deliver SIGHUP.${NC}"
fi

# Q9: Podman container mock-web-c3 (Operations Deployment - 25%)
if podman ps --format "{{.Names}} {{.Ports}}" 2>/dev/null | grep -q "mock-web-c3" && podman inspect mock-web-c3 --format '{{.HostConfig.RestartPolicy.Name}}' 2>/dev/null | grep -qi "always"; then
  echo -e "${GREEN}[PASS] Q9: Podman container mock-web-c3 running with restart always.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-web-c3 missing or restart policy not always.${NC}"
fi

# Q10: Nginx reverse proxy load balancer (Networking - 25%)
if systemctl is-active nginx &>/dev/null && [ -f /etc/nginx/conf.d/proxy-balance.conf ] && curl -s -m 2 http://127.0.0.1:8080 2>/dev/null | grep -qi "Backend"; then
  echo -e "${GREEN}[PASS] Q10: Nginx reverse proxy load balancer on port 8080 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: Nginx proxy-balance not responding on 8080 or backends unreachable.${NC}"
fi

# Q11: Network bridge br0 (Networking - 25%)
if ip link show br0 type bridge &>/dev/null && ip link show veth-br1 2>/dev/null | grep -q "master br0" && ip addr show br0 2>/dev/null | grep -q "192.168.50.1/24"; then
  echo -e "${GREEN}[PASS] Q11: Network bridge br0 with veth-br1 and 192.168.50.1/24 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: Bridge br0 missing or veth-br1 not enslaved.${NC}"
fi

# Q12: Iptables NAT port redirection (Networking - 25%)
if sudo iptables -t nat -L PREROUTING -n 2>/dev/null | grep -E "REDIRECT.*tcp.*dpt:8443.*redir ports 443" && [ -s /var/tmp/mock-lfcs-3/nat-rules.txt ]; then
  echo -e "${GREEN}[PASS] Q12: Iptables PREROUTING port 8443->443 redirection verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: Iptables NAT redirection rule missing or nat-rules.txt empty.${NC}"
fi

# Q13: Network packet capture with tcpdump (Networking - 25%)
# Send 5 test packets if not already sent
(for i in {1..5}; do nc -z -w 1 127.0.0.1 9999 2>/dev/null || true; done) &
if [ -s /var/tmp/mock-lfcs-3/traffic.pcap ] && [ "$(tcpdump -r /var/tmp/mock-lfcs-3/traffic.pcap 2>/dev/null | wc -l)" -ge 3 ]; then
  echo -e "${GREEN}[PASS] Q13: tcpdump traffic.pcap packet capture verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: traffic.pcap missing or does not contain captured TCP packets.${NC}"
fi

# Q14: Static route with metric (Networking - 25%)
if ip route show 10.150.0.0/16 2>/dev/null | grep -q "10.99.99.1.*metric 150"; then
  echo -e "${GREEN}[PASS] Q14: Static route 10.150.0.0/16 via 10.99.99.1 metric 150 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: Static route 10.150.0.0/16 missing or metric mismatch.${NC}"
fi

# Q15: Storage Performance Monitoring (Storage - 20%)
if [ -s /var/tmp/mock-lfcs-3/io-report.txt ] && grep -qiE "Device|%util|await" /var/tmp/mock-lfcs-3/io-report.txt && [ -s /var/tmp/mock-lfcs-3/sar-disk.txt ] && grep -qiE "DEV|%util|tps" /var/tmp/mock-lfcs-3/sar-disk.txt; then
  echo -e "${GREEN}[PASS] Q15: Storage I/O monitoring reports (iostat & sar) verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: io-report.txt or sar-disk.txt missing or incomplete.${NC}"
fi

# Q16: Filesystem Automounter autofs direct map (Storage - 20%)
if systemctl is-active autofs &>/dev/null && [ -f /etc/auto.master.d/direct.autofs ] && [ -f /mnt/auto-data/auto_test.txt ]; then
  echo -e "${GREEN}[PASS] Q16: autofs direct automount /mnt/auto-data verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: autofs direct map failed to mount /mnt/auto-data.${NC}"
fi

# Q17: LVM Thin Provisioning (Storage - 20%)
if sudo lvs mock-vg3/mock-pool --noheadings -o lv_attr 2>/dev/null | grep -q "t" && sudo lvs mock-vg3/mock-thin --noheadings -o lv_attr 2>/dev/null | grep -q "V" && sudo blkid /dev/mock-vg3/mock-thin 2>/dev/null | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Q17: LVM thin pool and 150M thin volume verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: mock-pool or mock-thin missing or not formatted as ext4.${NC}"
fi

# Q18: Persistent mount by UUID with security options (Storage - 20%)
if mountpoint -q /mnt/secure-data 2>/dev/null && grep -q "UUID=" /etc/fstab && grep -q "/mnt/secure-data" /etc/fstab && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "noexec" && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "nosuid" && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "nodev"; then
  echo -e "${GREEN}[PASS] Q18: Persistent UUID mount with noexec,nosuid,nodev verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: /mnt/secure-data not mounted or options/fstab incorrect.${NC}"
fi

# Q19: Granular Sudoers Delegation (Users and Groups - 10%)
SUDO_DEV=$(sudo -l -U developer 2>/dev/null || true)
if [ -f /etc/sudoers.d/90-developer ] && [ "$(stat -c %a /etc/sudoers.d/90-developer)" = "440" ] && echo "$SUDO_DEV" | grep -q "NOPASSWD: /usr/bin/systemctl restart nginx, /usr/bin/journalctl"; then
  echo -e "${GREEN}[PASS] Q19: Granular sudoers permissions for developer verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: 90-developer sudoers entry missing or permissions incorrect.${NC}"
fi

# Q20: SGID and Sticky Bit Collaborative Workspace (Users and Groups - 10%)
if [ -d /var/tmp/mock-lfcs-3/team_collab ] && [ "$(stat -c %a /var/tmp/mock-lfcs-3/team_collab)" = "2775" ] && [ "$(stat -c %G /var/tmp/mock-lfcs-3/team_collab)" = "devteam" ] && [ -d /var/tmp/mock-lfcs-3/team_collab/dropzone ] && [ "$(stat -c %a /var/tmp/mock-lfcs-3/team_collab/dropzone)" = "1777" ]; then
  echo -e "${GREEN}[PASS] Q20: SGID (2775) and sticky bit (1777) team directory verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: team_collab or dropzone permissions/group mismatch.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: Web Server Error Log Parsing
```bash
awk '$9 ~ /^[45]/ {print $1}' /var/tmp/mock-lfcs-3/web_access.log | sort -u > /var/tmp/mock-lfcs-3/error_ips.txt
```

#### Q2: SSL CSR with SAN
```bash
openssl req -new -newkey rsa:2048 -nodes   -keyout /var/tmp/mock-lfcs-3/server.key   -out /var/tmp/mock-lfcs-3/server.csr   -subj "/CN=lfcs.local/O=MockCorp"   -addext "subjectAltName=DNS:lfcs.local,DNS:api.lfcs.local"
```

#### Q3: Multi-threaded Compressed Archive
```bash
XZ_OPT="-T0" tar -cJf /var/tmp/mock-lfcs-3/backup.tar.xz -C /var/tmp/mock-lfcs-3 source_data
cd /var/tmp/mock-lfcs-3 && sha256sum backup.tar.xz > backup.tar.xz.sha256
```

#### Q4: Git Annotated Tag and Release Branch
```bash
cd /var/tmp/mock-lfcs-3/git-app
git tag -a v1.2.0 -m "Production Release 1.2.0"
git checkout -b release-1.2 v1.2.0
```

#### Q5: Systemd Cgroup Resource Drop-in
```bash
sudo mkdir -p /etc/systemd/system/mock-worker.service.d
sudo tee /etc/systemd/system/mock-worker.service.d/limits.conf << 'EOF'
[Service]
MemoryMax=64M
CPUQuota=40%
EOF
sudo systemctl daemon-reload
sudo systemctl restart mock-worker.service
```

#### Q6: Kernel Module Blacklisting
```bash
sudo tee /etc/modprobe.d/blacklist-cramfs.conf << 'EOF'
blacklist cramfs
install cramfs /bin/true
EOF
sudo modprobe -r cramfs 2>/dev/null || true
```

#### Q7: Journalctl Diagnostic Log Extraction
```bash
journalctl --since "2026-01-01" -p err..emerg --no-pager > /var/tmp/mock-lfcs-3/system_errors.log
```

#### Q8: Graceful Process Reload Script
```bash
sudo tee /usr/local/bin/reload_mock_app.sh << 'EOF'
#!/usr/bin/env bash
if [ -f /var/run/mock-app.pid ]; then
    PID=$(cat /var/run/mock-app.pid)
    kill -HUP "$PID"
    echo "$(date) RELOAD SIGNAL SENT" >> /var/tmp/mock-lfcs-3/signal.log
fi
EOF
sudo chmod +x /usr/local/bin/reload_mock_app.sh
```

#### Q9: Run Container with Podman
```bash
podman run -d --name mock-web-c3 --restart always -p 8085:80 docker.io/library/nginx:alpine
```

#### Q10: Nginx Reverse Proxy Load Balancer
```bash
sudo tee /etc/nginx/conf.d/proxy-balance.conf << 'EOF'
upstream backend_nodes {
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
}

server {
    listen 8080;
    server_name _;

    location / {
        proxy_pass http://backend_nodes;
        proxy_set_header Host $host;
    }
}
EOF
sudo nginx -t && sudo systemctl restart nginx
```

#### Q11: Network Bridge Configuration
```bash
sudo ip link add br0 type bridge
sudo ip link set veth-br1 master br0
sudo ip addr add 192.168.50.1/24 dev br0
sudo ip link set veth-br1 up
sudo ip link set br0 up
```

#### Q12: Iptables NAT Port Redirection
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 8443 -j REDIRECT --to-ports 443
sudo iptables -t nat -L PREROUTING -n > /var/tmp/mock-lfcs-3/nat-rules.txt
```

#### Q13: Network Packet Capture with tcpdump
```bash
sudo tcpdump -i lo -c 5 -w /var/tmp/mock-lfcs-3/traffic.pcap tcp port 9999
```

#### Q14: Static Route with Metric
```bash
sudo ip route add 10.150.0.0/16 via 10.99.99.1 dev dummy0 metric 150 onlink
```

#### Q15: Storage Performance Monitoring
```bash
iostat -x -d 1 3 > /var/tmp/mock-lfcs-3/io-report.txt
sar -d 1 3 > /var/tmp/mock-lfcs-3/sar-disk.txt
```

#### Q16: Filesystem Automounter Direct Map
```bash
echo "/- /etc/auto.direct --timeout=60" | sudo tee /etc/auto.master.d/direct.autofs
echo "/mnt/auto-data -fstype=ext4,loop,rw :/var/tmp/mock-lfcs-3/auto.img" | sudo tee /etc/auto.direct
sudo systemctl restart autofs
ls /mnt/auto-data
```

#### Q17: LVM Thin Provisioning
```bash
sudo lvcreate -L 50M -T mock-vg3/mock-pool
sudo lvcreate -V 150M -T mock-vg3/mock-pool -n mock-thin
sudo mkfs.ext4 /dev/mock-vg3/mock-thin
```

#### Q18: Persistent Mount by UUID
```bash
UUID_VAL=$(sudo blkid -s UUID -o value /var/tmp/mock-lfcs-3/secure_store.img)
sudo mkdir -p /mnt/secure-data
echo "UUID=$UUID_VAL /mnt/secure-data ext4 loop,noexec,nosuid,nodev 0 0" | sudo tee -a /etc/fstab
sudo mount -a
```

#### Q19: Granular Sudoers File
```bash
echo "developer ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-developer
sudo chmod 0440 /etc/sudoers.d/90-developer
```

#### Q20: SGID and Sticky Bit Directory
```bash
sudo mkdir -p /var/tmp/mock-lfcs-3/team_collab/dropzone
sudo chown student:devteam /var/tmp/mock-lfcs-3/team_collab
sudo chmod 2775 /var/tmp/mock-lfcs-3/team_collab
sudo chmod 1777 /var/tmp/mock-lfcs-3/team_collab/dropzone
```""",
        "reset": """sudo systemctl stop mock-worker.service 2>/dev/null || true
sudo systemctl disable mock-worker.service 2>/dev/null || true
sudo rm -rf /etc/systemd/system/mock-worker.service* /etc/modprobe.d/blacklist-cramfs.conf /usr/local/bin/reload_mock_app.sh /etc/nginx/conf.d/proxy-balance.conf /etc/auto.master.d/direct.autofs /etc/auto.direct /etc/sudoers.d/90-developer
sudo systemctl daemon-reload
podman stop mock-web-c3 2>/dev/null || true
podman rm -f mock-web-c3 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8443 -j REDIRECT --to-ports 443 2>/dev/null || true
sudo ip route del 10.150.0.0/16 dev dummy0 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
sudo ip link del veth-br1 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo umount /mnt/secure-data 2>/dev/null || true
sudo sed -i '/secure-data/d' /etc/fstab
sudo rm -rf /mnt/secure-data
sudo systemctl stop autofs 2>/dev/null || true
sudo umount -l /mnt/auto-data 2>/dev/null || true
sudo systemctl start autofs 2>/dev/null || true
sudo lvremove -f /dev/mock-vg3/mock-thin 2>/dev/null || true
sudo lvremove -f /dev/mock-vg3/mock-pool 2>/dev/null || true
sudo vgremove -f mock-vg3 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-3" | cut -d: -f1); do
    sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r developer 2>/dev/null || true
sudo groupdel devteam 2>/dev/null || true
sudo rm -rf /var/tmp/mock-lfcs-3 /var/run/mock-app.pid""",
    },
    {
        "lab_id": 'mock-lfcs-4',
        "track": 'LFCS',
        "date": '2026-11-26',
        "title": 'LFCS Full-Scale Timed Mock Exam 4 (Benchmark)',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# LFCS Full-Scale Timed Mock Exam 4 (Benchmark)

**Passing Score:** 67% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Environment:** VirtualBox Ubuntu LFCS VM (`student@172.16.16.16`)

---

### Linux Foundation Official Domain Weights:
1. **Operations Deployment (25%)**
   - Configure kernel parameters, persistent and non-persistent
   - Diagnose, identify, manage, and troubleshoot processes and services
   - Manage or schedule jobs for executing commands
   - Search for, install, validate, and maintain software packages or repositories
   - Manage Virtual Machines and containers
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Monitor and troubleshoot networking
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Text manipulation and log analysis
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Archive and compress files
   - Work with SSL certificates and Git
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits and granular privilege escalation
   - Configure and manage ACLs and user aging policies

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** Advanced text analysis and columnar calculation with `awk`:
  - A CSV sales report is located at `/var/tmp/mock-lfcs-4/sales.csv` with fields `ID,Product,Department,Price,Quantity`.
  - Calculate the total sales revenue (`Price * Quantity`) for all items in the `Electronics` department.
  - Write the single calculated numerical sum into `/var/tmp/mock-lfcs-4/electronics_total.txt`.
- **Q2:** Bulk file permission hardening with `find -exec`:
  - In directory tree `/var/tmp/mock-lfcs-4/archive_vault`, find all regular files ending in `.bak` or `.old` that have modification time older than 7 days (`-mtime +7`).
  - Change their file permissions to `0600` (`chmod 600`) using `find ... -exec chmod 600 {} +`.
  - Save the sorted list of matched file paths into `/var/tmp/mock-lfcs-4/vault_audit.txt`.
- **Q3:** SSL/TLS Certificate Expiration & Fingerprint Inspection:
  - A TLS certificate is located at `/var/tmp/mock-lfcs-4/production.crt`.
  - Use `openssl x509` to extract its expiration date (`-enddate`), issuer organization (`-issuer`), and SHA256 fingerprint (`-fingerprint -sha256`) without opening an editor.
  - Write the extracted details to `/var/tmp/mock-lfcs-4/cert-summary.txt`.
- **Q4:** Git Commit Cherry-picking:
  - In repository `/var/tmp/mock-lfcs-4/code-repo`, branch `hotfix` contains a critical patch with commit message `"HOTFIX: fix buffer overflow"`.
  - On branch `main`, cherry-pick this commit to integrate it into `main`.
  - Ensure the commit is recorded in `main` history.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Custom Systemd Slice Resource Management:
  - Create a custom systemd slice unit file at `/etc/systemd/system/batch.slice` with `MemoryMax=128M` and `CPUWeight=150`.
  - Configure the existing service `/etc/systemd/system/batch-worker.service` to run inside `batch.slice` (`Slice=batch.slice`).
  - Reload systemd daemon configuration and restart `batch-worker.service`.
- **Q6:** Kernel Parameter Hardening via `/etc/sysctl.d/`:
  - Configure persistent network security parameters in `/etc/sysctl.d/99-security.conf`:
    - `net.ipv4.conf.all.accept_source_route = 0`
    - `net.ipv4.icmp_echo_ignore_broadcasts = 1`
    - `net.ipv4.tcp_syncookies = 1`
  - Apply the configuration immediately using `sysctl --system`.
- **Q7:** Automated Scheduled Backup Script with Rsync:
  - Create an automated backup script at `/usr/local/bin/system_backup.sh` (executable).
  - The script must synchronize directory `/var/tmp/mock-lfcs-4/data/` to `/var/tmp/mock-lfcs-4/backup/` using `rsync -a --delete`.
  - If the rsync succeeds, append `"SUCCESS: $(date)"` to `/var/log/backup_sync.log`. If it fails, append `"FAILED: $(date)"` to `/var/log/backup_sync.log`.
- **Q8:** Dynamic Linker Shared Library Configuration:
  - A custom shared library `libcustom.so` is located in directory `/opt/customlib`.
  - Configure the dynamic linker to include `/opt/customlib` by creating configuration file `/etc/ld.so.conf.d/customlib.conf`.
  - Update the dynamic linker runtime cache with `ldconfig` and verify `/opt/customlib` is indexed in `ldconfig -p`.
- **Q9:** Container Deployment with Volume Mount and Environment Variable (Podman):
  - Run a detached Podman container named `mock-backup-job` using image `docker.io/library/alpine`.
  - Set environment variable `BACKUP_INTERVAL=3600` (`-e BACKUP_INTERVAL=3600`).
  - Mount host directory `/var/tmp/mock-lfcs-4/cdata` to `/data:Z` in the container (`-v /var/tmp/mock-lfcs-4/cdata:/data:Z`).
  - Execute command `sh -c "echo active > /data/status.txt && sleep 3600"` in detached mode.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** HAProxy Layer 7 HTTP Load Balancer Configuration:
  - Configure HAProxy (`/etc/haproxy/haproxy.cfg`) with a frontend `mock_front` binding to `*:8088` and default backend `mock_back`.
  - In `mock_back`, configure roundrobin load balancing between `127.0.0.1:9001` and `127.0.0.1:9002` with health checks (`check`).
  - Ensure HAProxy service is enabled, started, and listening on port `8088`.
- **Q11:** Network Bonding Configuration (`bond0`):
  - Create a network bonding interface named `bond0` with `mode active-backup` and `miimon 100` (`ip link add bond0 type bond mode active-backup miimon 100`).
  - Attach slave dummy interfaces `veth-bond1` and `veth-bond2` to `bond0` (`ip link set veth-bond1 master bond0`, etc.).
  - Assign IP `192.168.99.10/24` to `bond0` and bring `bond0`, `veth-bond1`, and `veth-bond2` up.
- **Q12:** Iptables Stateful Packet Filtering & Rate Limiting:
  - In `iptables` INPUT chain:
    - Append a stateful rule allowing established and related connections: `-m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`.
    - Append a rule limiting incoming ICMP echo requests to 2 per second: `-p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT`.
  - Save the INPUT chain rules to `/var/tmp/mock-lfcs-4/iptables-input.txt`.
- **Q13:** Network Socket States Audit with `ss`:
  - Use `ss` socket statistics utility:
    - Extract all established TCP sockets with process details (`ss -t -a state established -p`) and save to `/var/tmp/mock-lfcs-4/tcp-established.txt`.
    - Extract all listening UDP sockets (`ss -u -l -n`) and save to `/var/tmp/mock-lfcs-4/udp-listening.txt`.
- **Q14:** 802.1Q VLAN Tagging Interface:
  - Create an 802.1Q tagged VLAN interface named `dummy0.50` on top of base interface `dummy0` with VLAN ID `50` (`ip link add link dummy0 name dummy0.50 type vlan id 50`).
  - Assign IP address `10.50.50.1/24` to `dummy0.50` and bring the interface up.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Storage Performance Monitoring with `iotop` & Active Process Tracking:
  - Run `iotop -b -n 3 -d 1 -o` in batch mode to capture processes actively performing disk I/O and save the output to `/var/tmp/mock-lfcs-4/iotop-report.txt`.
  - A background generator script is performing high disk write activity. Parse the process command name doing the high disk write into `/var/tmp/mock-lfcs-4/high-io-proc.txt`.
- **Q16:** Automounter Indirect Map (`autofs`):
  - Configure `autofs` indirect automounting under root mount `/shares`:
    - In `/etc/auto.master.d/shares.autofs`, configure `/shares /etc/auto.shares --timeout=60`.
    - In `/etc/auto.shares`, define map entry `docs` to mount `/var/tmp/mock-lfcs-4/storage_export` with options `-fstype=bind,rw`.
    - Restart `autofs` (`systemctl restart autofs`) and verify accessing `/shares/docs` automatically mounts the export.
- **Q17:** LVM Striped Logical Volume Creation:
  - In Volume Group `mock-vg4` (composed of two physical loop volumes), create a 2-stripe Logical Volume named `mock-striped` of size `50M` with stripe size `64k` (`lvcreate -i 2 -I 64k -L 50M -n mock-striped mock-vg4`).
  - Format `/dev/mock-vg4/mock-striped` with `ext4`.
- **Q18:** Filesystem Disk Quotas:
  - A filesystem is mounted at `/var/tmp/mock-lfcs-4/quota_mount` with user quota support enabled (`usrquota`).
  - Assign user `tester-quota` a block soft limit of `40MB` (40960 KB) and hard limit of `60MB` (61440 KB) using `setquota -u tester-quota 40960 61440 0 0 /var/tmp/mock-lfcs-4/quota_mount`.
  - Confirm the quota configuration with `quota -v -u tester-quota`.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Centralized Identity Lookup Configuration (SSSD / NSS):
  - In `/etc/nsswitch.conf`, ensure `passwd:` and `group:` queries include `sss` (e.g., `passwd: files systemd sss` and `group: files systemd sss`).
  - In `/etc/sssd/sssd.conf`, ensure file permissions are `0600` owned by `root:root`.
  - Configure a basic local domain in `/etc/sssd/sssd.conf` with `domains = local`, `[domain/local]`, and `id_provider = local`.
- **Q20:** User Account Expiration & Initial Login Password Change:
  - Create a temporary auditor account named `temp-auditor` with account expiration date set to `2026-12-31` (`useradd -e 2026-12-31 temp-auditor`).
  - Force the user to change their password on their very first login (`chage -d 0 temp-auditor`).
  - Verify configuration with `chage -l temp-auditor`.""",
        "setup": """sudo rm -rf /var/tmp/mock-lfcs-4 /etc/systemd/system/batch.slice /etc/systemd/system/batch-worker.service /etc/sysctl.d/99-security.conf /usr/local/bin/system_backup.sh /etc/ld.so.conf.d/customlib.conf /opt/customlib /etc/auto.master.d/shares.autofs /etc/auto.shares /etc/sssd/sssd.conf
sudo mkdir -p /var/tmp/mock-lfcs-4/archive_vault /var/tmp/mock-lfcs-4/code-repo /var/tmp/mock-lfcs-4/data /var/tmp/mock-lfcs-4/cdata /var/tmp/mock-lfcs-4/storage_export /var/tmp/mock-lfcs-4/quota_mount /opt/customlib
sudo chown -R student:student /var/tmp/mock-lfcs-4

# Q1 sales.csv
cat << 'EOF' > /var/tmp/mock-lfcs-4/sales.csv
ID,Product,Department,Price,Quantity
101,Monitor,Electronics,150,2
102,Desk,Furniture,300,1
103,Keyboard,Electronics,50,4
104,Chair,Furniture,120,3
105,Mouse,Electronics,25,4
EOF

# Q2 archive vault files
touch -d "10 days ago" /var/tmp/mock-lfcs-4/archive_vault/old_backup.bak
touch -d "12 days ago" /var/tmp/mock-lfcs-4/archive_vault/legacy_data.old
touch -d "2 days ago" /var/tmp/mock-lfcs-4/archive_vault/recent.bak
touch -d "15 days ago" /var/tmp/mock-lfcs-4/archive_vault/notes.txt
chmod 644 /var/tmp/mock-lfcs-4/archive_vault/*

# Q3 production.crt
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/prod.key -out /var/tmp/mock-lfcs-4/production.crt -subj "/CN=prod.internal/O=EnterpriseCorp/OU=IT" 2>/dev/null || true
rm -f /tmp/prod.key

# Q4 code-repo with hotfix branch
git -C /var/tmp/mock-lfcs-4/code-repo init -b main 2>/dev/null || (git -C /var/tmp/mock-lfcs-4/code-repo init && git -C /var/tmp/mock-lfcs-4/code-repo checkout -b main)
echo "base codebase" > /var/tmp/mock-lfcs-4/code-repo/main.py
git -C /var/tmp/mock-lfcs-4/code-repo add main.py
git -C /var/tmp/mock-lfcs-4/code-repo -c user.name="LFCS Admin" -c user.email="admin@lfcs.local" commit -m "Initial commit" 2>/dev/null || true
git -C /var/tmp/mock-lfcs-4/code-repo checkout -b hotfix 2>/dev/null || true
echo "security patch applied" >> /var/tmp/mock-lfcs-4/code-repo/main.py
git -C /var/tmp/mock-lfcs-4/code-repo add main.py
git -C /var/tmp/mock-lfcs-4/code-repo -c user.name="Security Team" -c user.email="sec@lfcs.local" commit -m "HOTFIX: fix buffer overflow" 2>/dev/null || true
git -C /var/tmp/mock-lfcs-4/code-repo checkout main 2>/dev/null || true

# Q5 batch-worker service
sudo tee /etc/systemd/system/batch-worker.service << 'EOF'
[Unit]
Description=Batch Worker Service
[Service]
Type=simple
ExecStart=/usr/bin/sleep infinity
Restart=always
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now batch-worker.service 2>/dev/null || true

# Q7 backup data
echo "data file 1" > /var/tmp/mock-lfcs-4/data/file1.txt
echo "data file 2" > /var/tmp/mock-lfcs-4/data/file2.txt

# Q8 dynamic shared library
sudo cp /usr/lib/x86_64-linux-gnu/libc.so.6 /opt/customlib/libcustom.so 2>/dev/null || sudo touch /opt/customlib/libcustom.so

# Q10 HAProxy backends on 9001 and 9002
(python3 -m http.server 9001 &>/dev/null) &
(python3 -m http.server 9002 &>/dev/null) &

# Q11 bonding slave interfaces
sudo modprobe bonding 2>/dev/null || true
sudo ip link del bond0 2>/dev/null || true
sudo ip link del veth-bond1 2>/dev/null || true
sudo ip link del veth-bond2 2>/dev/null || true
sudo ip link add veth-bond1 type dummy 2>/dev/null || true
sudo ip link add veth-bond2 type dummy 2>/dev/null || true

# Q14 dummy0 interface for VLAN
sudo modprobe 8021q 2>/dev/null || true
sudo modprobe dummy 2>/dev/null || true
sudo ip link del dummy0.50 2>/dev/null || true
sudo ip link add dummy0 type dummy 2>/dev/null || true
sudo ip link set dummy0 up 2>/dev/null || true

# Q15 background disk activity
(while true; do dd if=/dev/zero of=/var/tmp/mock-lfcs-4/io_burn bs=1M count=10 oflag=direct 2>/dev/null; sleep 0.2; done) &
echo $! > /var/tmp/mock-lfcs-4/io.pid

# Q16 storage export
echo "policy content" > /var/tmp/mock-lfcs-4/storage_export/policy.pdf

# Q17 LVM striped VG
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/pv1.img bs=1M count=40 2>/dev/null || true
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/pv2.img bs=1M count=40 2>/dev/null || true
L1=$(sudo losetup -f --show /var/tmp/mock-lfcs-4/pv1.img 2>/dev/null || true)
L2=$(sudo losetup -f --show /var/tmp/mock-lfcs-4/pv2.img 2>/dev/null || true)
if [ -n "$L1" ] && [ -n "$L2" ]; then
    sudo pvcreate "$L1" "$L2" 2>/dev/null || true
    sudo vgcreate mock-vg4 "$L1" "$L2" 2>/dev/null || true
fi

# Q18 user tester-quota & quota image
sudo userdel -r tester-quota 2>/dev/null || true
sudo useradd -m tester-quota 2>/dev/null || true
dd if=/dev/zero of=/var/tmp/mock-lfcs-4/quota.img bs=1M count=100 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-4/quota.img 2>/dev/null || true
sudo mount -o loop,usrquota /var/tmp/mock-lfcs-4/quota.img /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo quotacheck -cum /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo quotaon -u /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true

# Q20 user temp-auditor clean
sudo userdel -r temp-auditor 2>/dev/null || true""",
        "verify": """# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 4 against Linux Foundation Domain Weights...${NC}"

# Q1: Awk columnar calculation (Essential Commands - 20%)
TOTAL_CALC=$(cat /var/tmp/mock-lfcs-4/electronics_total.txt 2>/dev/null | tr -d '[:space:]' || echo "0")
if [ "$TOTAL_CALC" = "600" ]; then
  echo -e "${GREEN}[PASS] Q1: electronics_total.txt awk calculation (600) verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: electronics_total.txt value: '$TOTAL_CALC' (expected 600).${NC}"
fi

# Q2: Bulk file permission hardening (Essential Commands - 20%)
M1=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/old_backup.bak 2>/dev/null || echo "")
M2=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/legacy_data.old 2>/dev/null || echo "")
M3=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/recent.bak 2>/dev/null || echo "")
if [ "$M1" = "600" ] && [ "$M2" = "600" ] && [ "$M3" = "644" ] && [ -s /var/tmp/mock-lfcs-4/vault_audit.txt ]; then
  echo -e "${GREEN}[PASS] Q2: Bulk find -exec chmod 600 and vault_audit.txt verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: Permissions not updated to 0600 on mtime +7 files or audit missing.${NC}"
fi

# Q3: SSL/TLS certificate inspection (Essential Commands - 20%)
if [ -s /var/tmp/mock-lfcs-4/cert-summary.txt ] && grep -qiE "notAfter|notAfter=" /var/tmp/mock-lfcs-4/cert-summary.txt && grep -qi "issuer" /var/tmp/mock-lfcs-4/cert-summary.txt && grep -qi "SHA256 Fingerprint" /var/tmp/mock-lfcs-4/cert-summary.txt; then
  echo -e "${GREEN}[PASS] Q3: cert-summary.txt openssl x509 details verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: cert-summary.txt missing or lacks required certificate fields.${NC}"
fi

# Q4: Git cherry-picking (Essential Commands - 20%)
if git -C /var/tmp/mock-lfcs-4/code-repo log --oneline 2>/dev/null | grep -q "HOTFIX: fix buffer overflow" && [ "$(git -C /var/tmp/mock-lfcs-4/code-repo branch --show-current 2>/dev/null)" = "main" ]; then
  echo -e "${GREEN}[PASS] Q4: Git cherry-pick on branch main verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: Branch main does not contain cherry-picked hotfix commit.${NC}"
fi

# Q5: Custom systemd slice (Operations Deployment - 25%)
SLICE_VAL=$(systemctl show batch-worker.service -p Slice --value 2>/dev/null || echo "")
MEM_VAL=$(systemctl show batch.slice -p MemoryMax --value 2>/dev/null || echo "")
CPU_VAL=$(systemctl show batch.slice -p CPUWeight --value 2>/dev/null || echo "")
if [ "$SLICE_VAL" = "batch.slice" ] && [ "$MEM_VAL" = "134217728" ] && [ "$CPU_VAL" = "150" ]; then
  echo -e "${GREEN}[PASS] Q5: batch.slice resource configuration (128M, CPUWeight 150) verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: batch.slice mismatch (Slice: $SLICE_VAL, Mem: $MEM_VAL, CPUWeight: $CPU_VAL).${NC}"
fi

# Q6: Kernel security sysctl parameters (Operations Deployment - 25%)
V_SRC=$(sysctl -n net.ipv4.conf.all.accept_source_route 2>/dev/null || echo "1")
V_ICMP=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")
V_SYN=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
if [ -f /etc/sysctl.d/99-security.conf ] && [ "$V_SRC" = "0" ] && [ "$V_ICMP" = "1" ] && [ "$V_SYN" = "1" ]; then
  echo -e "${GREEN}[PASS] Q6: Kernel security parameters in /etc/sysctl.d/99-security.conf verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: Kernel security sysctl parameters mismatch or not persistent.${NC}"
fi

# Q7: Automated backup script with rsync (Operations Deployment - 25%)
if [ -x /usr/local/bin/system_backup.sh ] && /usr/local/bin/system_backup.sh 2>/dev/null && [ -f /var/tmp/mock-lfcs-4/backup/file1.txt ] && [ -f /var/log/backup_sync.log ] && grep -q "SUCCESS" /var/log/backup_sync.log; then
  echo -e "${GREEN}[PASS] Q7: system_backup.sh rsync synchronization and logging verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: system_backup.sh execution failed or /var/log/backup_sync.log missing.${NC}"
fi

# Q8: Dynamic linker library path (Operations Deployment - 25%)
if [ -f /etc/ld.so.conf.d/customlib.conf ] && grep -q "/opt/customlib" /etc/ld.so.conf.d/customlib.conf && ldconfig -p 2>/dev/null | grep -q "/opt/customlib"; then
  echo -e "${GREEN}[PASS] Q8: Dynamic linker library cache /opt/customlib verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: ld.so.conf.d/customlib.conf missing or /opt/customlib not in ldconfig -p.${NC}"
fi

# Q9: Podman container with volume and env (Operations Deployment - 25%)
if podman ps --format "{{.Names}}" 2>/dev/null | grep -q "mock-backup-job" && podman inspect mock-backup-job --format '{{json .Config.Env}}' 2>/dev/null | grep -q "BACKUP_INTERVAL=3600" && [ -f /var/tmp/mock-lfcs-4/cdata/status.txt ] && grep -q "active" /var/tmp/mock-lfcs-4/cdata/status.txt; then
  echo -e "${GREEN}[PASS] Q9: Podman container mock-backup-job volume and env verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-backup-job missing or volume mount failed.${NC}"
fi

# Q10: HAProxy layer 7 load balancer (Networking - 25%)
if systemctl is-active haproxy &>/dev/null && ss -tlpn 2>/dev/null | grep -q ":8088 " && grep -q "balance roundrobin" /etc/haproxy/haproxy.cfg 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q10: HAProxy HTTP load balancer on port 8088 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: HAProxy not running on port 8088 or haproxy.cfg incorrect.${NC}"
fi

# Q11: Network bonding bond0 (Networking - 25%)
if ip link show bond0 &>/dev/null && grep -qi "active-backup" /proc/net/bonding/bond0 2>/dev/null && grep -qi "veth-bond1" /proc/net/bonding/bond0 2>/dev/null && ip addr show bond0 2>/dev/null | grep -q "192.168.99.10/24"; then
  echo -e "${GREEN}[PASS] Q11: Network bonding bond0 (active-backup, 192.168.99.10/24) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: bond0 interface missing or slaves not attached.${NC}"
fi

# Q12: Iptables stateful packet filtering & rate limiting (Networking - 25%)
if sudo iptables -L INPUT -n 2>/dev/null | grep -qiE "RELATED.*ESTABLISHED|ESTABLISHED.*RELATED" && sudo iptables -L INPUT -n 2>/dev/null | grep -qiE "limit: avg 2/sec|limit 2/sec" && [ -s /var/tmp/mock-lfcs-4/iptables-input.txt ]; then
  echo -e "${GREEN}[PASS] Q12: Iptables stateful filter and ICMP rate limit verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: Iptables INPUT rules missing or iptables-input.txt empty.${NC}"
fi

# Q13: Network socket states audit with ss (Networking - 25%)
if [ -s /var/tmp/mock-lfcs-4/tcp-established.txt ] && grep -qiE "ESTAB|State|Recv-Q" /var/tmp/mock-lfcs-4/tcp-established.txt && [ -f /var/tmp/mock-lfcs-4/udp-listening.txt ] && grep -qiE "UNCONN|State|Recv-Q" /var/tmp/mock-lfcs-4/udp-listening.txt; then
  echo -e "${GREEN}[PASS] Q13: Socket reports (tcp-established.txt & udp-listening.txt) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: tcp-established.txt or udp-listening.txt missing or empty.${NC}"
fi

# Q14: 802.1Q VLAN interface (Networking - 25%)
if ip -d link show dummy0.50 2>/dev/null | grep -q "id 50" && ip addr show dummy0.50 2>/dev/null | grep -q "10.50.50.1/24"; then
  echo -e "${GREEN}[PASS] Q14: 802.1Q VLAN dummy0.50 (ID 50, 10.50.50.1/24) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: VLAN dummy0.50 missing or IP not assigned.${NC}"
fi

# Q15: Storage I/O monitoring with iotop (Storage - 20%)
if [ -s /var/tmp/mock-lfcs-4/iotop-report.txt ] && grep -qi "Total DISK" /var/tmp/mock-lfcs-4/iotop-report.txt && [ -s /var/tmp/mock-lfcs-4/high-io-proc.txt ] && grep -qiE "dd|io_burn|python" /var/tmp/mock-lfcs-4/high-io-proc.txt; then
  echo -e "${GREEN}[PASS] Q15: iotop-report.txt and high I/O process identification verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: iotop-report.txt or high-io-proc.txt missing or invalid.${NC}"
fi

# Q16: Automounter indirect map autofs (Storage - 20%)
if systemctl is-active autofs &>/dev/null && [ -f /etc/auto.master.d/shares.autofs ] && [ -f /shares/docs/policy.pdf ]; then
  echo -e "${GREEN}[PASS] Q16: autofs indirect automount /shares/docs verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: autofs indirect map failed to mount /shares/docs.${NC}"
fi

# Q17: LVM Striped Logical Volume (Storage - 20%)
STRIPES_NUM=$(sudo lvs mock-vg4/mock-striped --noheadings -o stripes 2>/dev/null | tr -d ' ' || echo "0")
if [ "$STRIPES_NUM" = "2" ] && sudo blkid /dev/mock-vg4/mock-striped 2>/dev/null | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Q17: LVM 2-stripe logical volume mock-striped verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: mock-striped volume missing or not 2-stripe ext4.${NC}"
fi

# Q18: Filesystem disk quotas (Storage - 20%)
QUOTA_OUT=$(sudo quota -v -u tester-quota 2>/dev/null || true)
if echo "$QUOTA_OUT" | grep -q "40960.*61440"; then
  echo -e "${GREEN}[PASS] Q18: Filesystem disk quota (soft 40M, hard 60M) verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: Quota for tester-quota not set to 40960/61440 limits.${NC}"
fi

# Q19: Centralized identity lookup SSSD / NSS (Users and Groups - 10%)
if grep -E "^passwd:.*sss" /etc/nsswitch.conf &>/dev/null && grep -E "^group:.*sss" /etc/nsswitch.conf &>/dev/null && [ -f /etc/sssd/sssd.conf ] && [ "$(stat -c %a /etc/sssd/sssd.conf)" = "600" ] && sudo grep -q "domain/local" /etc/sssd/sssd.conf; then
  echo -e "${GREEN}[PASS] Q19: SSSD and nsswitch.conf centralized identity config verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: nsswitch.conf lacks sss or /etc/sssd/sssd.conf incorrect.${NC}"
fi

# Q20: User account expiration and password reset (Users and Groups - 10%)
CHAGE_INFO=$(sudo chage -l temp-auditor 2>/dev/null || true)
if id temp-auditor &>/dev/null && echo "$CHAGE_INFO" | grep -qi "Account expires.*Dec 31, 2026" && echo "$CHAGE_INFO" | grep -qi "Password must be changed"; then
  echo -e "${GREEN}[PASS] Q20: User temp-auditor expiration and password reset verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: temp-auditor missing or expiration/password reset not configured.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: Awk Columnar Calculation
```bash
awk -F',' '$3 == "Electronics" {sum += $4 * $5} END {print sum}' /var/tmp/mock-lfcs-4/sales.csv > /var/tmp/mock-lfcs-4/electronics_total.txt
```

#### Q2: Bulk File Permission Hardening
```bash
find /var/tmp/mock-lfcs-4/archive_vault -type f \( -name "*.bak" -o -name "*.old" \) -mtime +7 -exec chmod 600 {} +
find /var/tmp/mock-lfcs-4/archive_vault -type f \( -name "*.bak" -o -name "*.old" \) -mtime +7 | sort > /var/tmp/mock-lfcs-4/vault_audit.txt
```

#### Q3: SSL/TLS Certificate Inspection
```bash
openssl x509 -in /var/tmp/mock-lfcs-4/production.crt -noout -enddate -issuer -fingerprint -sha256 > /var/tmp/mock-lfcs-4/cert-summary.txt
```

#### Q4: Git Cherry-pick Commit
```bash
cd /var/tmp/mock-lfcs-4/code-repo
git checkout main
HOTFIX_COMMIT=$(git rev-parse hotfix)
git cherry-pick "$HOTFIX_COMMIT"
```

#### Q5: Custom Systemd Slice
```bash
sudo tee /etc/systemd/system/batch.slice << 'EOF'
[Slice]
MemoryMax=128M
CPUWeight=150
EOF
sudo sed -i '/\[Service\]/a Slice=batch.slice' /etc/systemd/system/batch-worker.service
sudo systemctl daemon-reload
sudo systemctl restart batch-worker.service
```

#### Q6: Kernel Security Sysctl Parameters
```bash
sudo tee /etc/sysctl.d/99-security.conf << 'EOF'
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.tcp_syncookies = 1
EOF
sudo sysctl --system
```

#### Q7: Automated Rsync Backup Script
```bash
sudo tee /usr/local/bin/system_backup.sh << 'EOF'
#!/usr/bin/env bash
set -e
mkdir -p /var/tmp/mock-lfcs-4/backup
if rsync -a --delete /var/tmp/mock-lfcs-4/data/ /var/tmp/mock-lfcs-4/backup/; then
    echo "SUCCESS: $(date)" >> /var/log/backup_sync.log
else
    echo "FAILED: $(date)" >> /var/log/backup_sync.log
    exit 1
fi
EOF
sudo chmod +x /usr/local/bin/system_backup.sh
```

#### Q8: Dynamic Linker Configuration
```bash
echo "/opt/customlib" | sudo tee /etc/ld.so.conf.d/customlib.conf
sudo ldconfig
```

#### Q9: Run Container with Volume and Env
```bash
podman run -d --name mock-backup-job -e BACKUP_INTERVAL=3600 -v /var/tmp/mock-lfcs-4/cdata:/data:Z docker.io/library/alpine sh -c "echo active > /data/status.txt && sleep 3600"
```

#### Q10: HAProxy Load Balancer
```bash
sudo tee -a /etc/haproxy/haproxy.cfg << 'EOF'

frontend mock_front
    bind *:8088
    default_backend mock_back

backend mock_back
    balance roundrobin
    server srv1 127.0.0.1:9001 check
    server srv2 127.0.0.1:9002 check
EOF
sudo systemctl restart haproxy
```

#### Q11: Network Bonding bond0
```bash
sudo ip link add bond0 type bond mode active-backup miimon 100
sudo ip link set veth-bond1 master bond0
sudo ip link set veth-bond2 master bond0
sudo ip addr add 192.168.99.10/24 dev bond0
sudo ip link set veth-bond1 up
sudo ip link set veth-bond2 up
sudo ip link set bond0 up
```

#### Q12: Iptables Stateful Filter & ICMP Rate Limiting
```bash
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT
sudo iptables -S INPUT > /var/tmp/mock-lfcs-4/iptables-input.txt
```

#### Q13: Audit Socket States with ss
```bash
ss -t -a state established -p > /var/tmp/mock-lfcs-4/tcp-established.txt
ss -u -l -n > /var/tmp/mock-lfcs-4/udp-listening.txt
```

#### Q14: 802.1Q VLAN Interface
```bash
sudo ip link add link dummy0 name dummy0.50 type vlan id 50
sudo ip addr add 10.50.50.1/24 dev dummy0.50
sudo ip link set dummy0.50 up
```

#### Q15: Storage I/O Monitoring with iotop
```bash
sudo iotop -b -n 3 -d 1 -o > /var/tmp/mock-lfcs-4/iotop-report.txt
awk '/DISK WRITE/ {next} NF > 9 && $6 ~ /M\/s|K\/s/ {print $NF}' /var/tmp/mock-lfcs-4/iotop-report.txt | head -n 1 > /var/tmp/mock-lfcs-4/high-io-proc.txt || echo "dd" > /var/tmp/mock-lfcs-4/high-io-proc.txt
```

#### Q16: Filesystem Automounter Indirect Map
```bash
echo "/shares /etc/auto.shares --timeout=60" | sudo tee /etc/auto.master.d/shares.autofs
echo "docs -fstype=bind,rw :/var/tmp/mock-lfcs-4/storage_export" | sudo tee /etc/auto.shares
sudo systemctl restart autofs
ls /shares/docs
```

#### Q17: LVM Striped Logical Volume
```bash
sudo lvcreate -i 2 -I 64k -L 50M -n mock-striped mock-vg4
sudo mkfs.ext4 /dev/mock-vg4/mock-striped
```

#### Q18: Filesystem Disk Quotas
```bash
sudo setquota -u tester-quota 40960 61440 0 0 /var/tmp/mock-lfcs-4/quota_mount
```

#### Q19: Centralized Identity SSSD / NSS
```bash
sudo sed -i 's/^passwd:.*/passwd:         files systemd sss/' /etc/nsswitch.conf
sudo sed -i 's/^group:.*/group:          files systemd sss/' /etc/nsswitch.conf
sudo tee /etc/sssd/sssd.conf << 'EOF'
[sssd]
services = nss, pam
domains = local

[domain/local]
id_provider = local
EOF
sudo chmod 0600 /etc/sssd/sssd.conf
sudo chown root:root /etc/sssd/sssd.conf
```

#### Q20: User Account Expiration & Password Reset
```bash
sudo useradd -m -e 2026-12-31 temp-auditor
sudo chage -d 0 temp-auditor
```""",
        "reset": """sudo systemctl stop batch-worker.service 2>/dev/null || true
sudo systemctl disable batch-worker.service 2>/dev/null || true
sudo rm -rf /etc/systemd/system/batch.slice /etc/systemd/system/batch-worker.service /etc/sysctl.d/99-security.conf /usr/local/bin/system_backup.sh /etc/ld.so.conf.d/customlib.conf /opt/customlib /etc/auto.master.d/shares.autofs /etc/auto.shares /etc/sssd/sssd.conf /var/log/backup_sync.log
sudo systemctl daemon-reload
podman stop mock-backup-job 2>/dev/null || true
podman rm -f mock-backup-job 2>/dev/null || true
if [ -f /var/tmp/mock-lfcs-4/io.pid ]; then
    kill -9 $(cat /var/tmp/mock-lfcs-4/io.pid) 2>/dev/null || true
fi
sudo iptables -D INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT 2>/dev/null || true
sudo ip link del bond0 2>/dev/null || true
sudo ip link del veth-bond1 2>/dev/null || true
sudo ip link del veth-bond2 2>/dev/null || true
sudo ip link del dummy0.50 2>/dev/null || true
sudo ip link del dummy0 2>/dev/null || true
sudo systemctl stop autofs 2>/dev/null || true
sudo umount -l /shares/docs 2>/dev/null || true
sudo systemctl start autofs 2>/dev/null || true
sudo quotaoff /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo umount /var/tmp/mock-lfcs-4/quota_mount 2>/dev/null || true
sudo lvremove -f /dev/mock-vg4/mock-striped 2>/dev/null || true
sudo vgremove -f mock-vg4 2>/dev/null || true
for l in $(losetup -a | grep "mock-lfcs-4" | cut -d: -f1); do
    sudo losetup -d "$l" 2>/dev/null || true
done
sudo userdel -r tester-quota 2>/dev/null || true
sudo userdel -r temp-auditor 2>/dev/null || true
sudo rm -rf /var/tmp/mock-lfcs-4""",
    },
]
