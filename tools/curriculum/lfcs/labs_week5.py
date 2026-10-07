"""
Dedicated LFCS Lab Definitions for Week 5 (Days 1 to 6).
"""

WEEK_5_LABS = [
    {
        "day": 1,
        "date": '2026-10-26',
        "title": 'Local User Management & /etc/passwd',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Create Dedicated User
Create a user named `devops_user`:
- UID: `1600`
- Primary group: `devops_user`
- Shell: `/bin/bash`
- Home directory: `/home/devops_user`
- Comment: `DevOps Service Account`

### Task 2: Account Password Aging & Expiry
Using `chage`:
- Set account expiration date to `2027-12-31`.
- Set maximum password age to `90` days.
- Set password warning to `7` days.

### Task 3: Account Locking
Lock the user account `test_lock_user` using `passwd -l` so login is disabled.""",
        "setup": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true
sudo useradd -m -s /bin/bash test_lock_user
echo "test_lock_user:P@ssword123" | sudo chpasswd""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: devops_user UID and shell
USER_INFO=$(getent passwd devops_user 2>/dev/null || true)
if echo "$USER_INFO" | grep -q ":1600:" && echo "$USER_INFO" | grep -q "/bin/bash"; then
  echo -e "${GREEN}[PASS] Task 1: devops_user created with UID 1600 and /bin/bash shell.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: devops_user missing or UID/shell incorrect: $USER_INFO.${NC}"
fi

# Task 2: chage settings
CHAGE_INFO=$(chage -l devops_user 2>/dev/null || true)
if echo "$CHAGE_INFO" | grep -qi "Dec 31, 2027" && echo "$CHAGE_INFO" | grep -q "90"; then
  echo -e "${GREEN}[PASS] Task 2: Password aging and expiry configured for devops_user.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: chage settings missing or incorrect.${NC}"
fi

# Task 3: test_lock_user locked
SHADOW_STAT=$(sudo passwd -S test_lock_user 2>/dev/null || true)
if echo "$SHADOW_STAT" | grep -qiE " L |locked"; then
  echo -e "${GREEN}[PASS] Task 3: test_lock_user account is locked.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: test_lock_user is not locked: $SHADOW_STAT.${NC}"
fi""",
        "solution": """1. Create user:
`sudo useradd -u 1600 -m -s /bin/bash -c "DevOps Service Account" devops_user`

2. Set aging:
`sudo chage -E 2027-12-31 -M 90 -W 7 devops_user`

3. Lock account:
`sudo passwd -l test_lock_user`""",
        "reset": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true""",
        "lfcs_title": 'Local User Management & /etc/passwd',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Create Dedicated User
Create a user named `devops_user`:
- UID: `1600`
- Primary group: `devops_user`
- Shell: `/bin/bash`
- Home directory: `/home/devops_user`
- Comment: `DevOps Service Account`

### Task 2: Account Password Aging & Expiry
Using `chage`:
- Set account expiration date to `2027-12-31`.
- Set maximum password age to `90` days.
- Set password warning to `7` days.

### Task 3: Account Locking
Lock the user account `test_lock_user` using `passwd -l` so login is disabled.""",
        "lfcs_setup": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true
sudo useradd -m -s /bin/bash test_lock_user
echo "test_lock_user:P@ssword123" | sudo chpasswd""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: devops_user UID and shell
USER_INFO=$(getent passwd devops_user 2>/dev/null || true)
if echo "$USER_INFO" | grep -q ":1600:" && echo "$USER_INFO" | grep -q "/bin/bash"; then
  echo -e "${GREEN}[PASS] Task 1: devops_user created with UID 1600 and /bin/bash shell.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: devops_user missing or UID/shell incorrect: $USER_INFO.${NC}"
fi

# Task 2: chage settings
CHAGE_INFO=$(chage -l devops_user 2>/dev/null || true)
if echo "$CHAGE_INFO" | grep -qi "Dec 31, 2027" && echo "$CHAGE_INFO" | grep -q "90"; then
  echo -e "${GREEN}[PASS] Task 2: Password aging and expiry configured for devops_user.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: chage settings missing or incorrect.${NC}"
fi

# Task 3: test_lock_user locked
SHADOW_STAT=$(sudo passwd -S test_lock_user 2>/dev/null || true)
if echo "$SHADOW_STAT" | grep -qiE " L |locked"; then
  echo -e "${GREEN}[PASS] Task 3: test_lock_user account is locked.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: test_lock_user is not locked: $SHADOW_STAT.${NC}"
fi""",
        "lfcs_solution": """1. Create user:
`sudo useradd -u 1600 -m -s /bin/bash -c "DevOps Service Account" devops_user`

2. Set aging:
`sudo chage -E 2027-12-31 -M 90 -W 7 devops_user`

3. Lock account:
`sudo passwd -l test_lock_user`""",
        "lfcs_reset": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true""",
    },
    {
        "day": 2,
        "date": '2026-10-27',
        "title": 'Groups, Sudo Privileges & Visudo',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Create Group & Assign Membership
1. Create a system group named `sysaudit` with GID `2800`.
2. Add user `student` to group `sysaudit` as a supplementary group.

### Task 2: Configure Passwordless Sudo for Specific Command
Create a sudoers drop-in file `/etc/sudoers.d/90-sysaudit`:
- Members of group `%sysaudit` must be permitted to execute `/usr/bin/journalctl` without password authentication (`NOPASSWD: /usr/bin/journalctl`).
- Validate syntax with `visudo -cf /etc/sudoers.d/90-sysaudit`.""",
        "setup": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: sysaudit group and student member
GRP_GID=$(getent group sysaudit | cut -d: -f3 || echo "0")
if [ "$GRP_GID" == "2800" ] && id -Gn student | grep -q "sysaudit"; then
  echo -e "${GREEN}[PASS] Task 1: Group sysaudit (GID 2800) created and student is member.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Group sysaudit missing or student not member.${NC}"
fi

# Task 2: sudoers drop-in validation
if [ -f /etc/sudoers.d/90-sysaudit ] && sudo visudo -cf /etc/sudoers.d/90-sysaudit >/dev/null 2>&1; then
  if grep -q "%sysaudit.*NOPASSWD.*journalctl" /etc/sudoers.d/90-sysaudit; then
    echo -e "${GREEN}[PASS] Task 2: Sudoers rule validated for %sysaudit with NOPASSWD for journalctl.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 2: Rule content does not grant NOPASSWD for journalctl to %sysaudit.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 2: /etc/sudoers.d/90-sysaudit missing or syntax error.${NC}"
fi""",
        "solution": """1. Group & user:
`sudo groupadd -g 2800 sysaudit`
`sudo usermod -aG sysaudit student`

2. Sudoers file:
`echo "%sysaudit ALL=(ALL) NOPASSWD: /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-sysaudit`
`sudo chmod 0440 /etc/sudoers.d/90-sysaudit`
`sudo visudo -cf /etc/sudoers.d/90-sysaudit`""",
        "reset": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true""",
        "lfcs_title": 'Groups, Sudo Privileges & Visudo',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Create Group & Assign Membership
1. Create a system group named `sysaudit` with GID `2800`.
2. Add user `student` to group `sysaudit` as a supplementary group.

### Task 2: Configure Passwordless Sudo for Specific Command
Create a sudoers drop-in file `/etc/sudoers.d/90-sysaudit`:
- Members of group `%sysaudit` must be permitted to execute `/usr/bin/journalctl` without password authentication (`NOPASSWD: /usr/bin/journalctl`).
- Validate syntax with `visudo -cf /etc/sudoers.d/90-sysaudit`.""",
        "lfcs_setup": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: sysaudit group and student member
GRP_GID=$(getent group sysaudit | cut -d: -f3 || echo "0")
if [ "$GRP_GID" == "2800" ] && id -Gn student | grep -q "sysaudit"; then
  echo -e "${GREEN}[PASS] Task 1: Group sysaudit (GID 2800) created and student is member.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Group sysaudit missing or student not member.${NC}"
fi

# Task 2: sudoers drop-in validation
if [ -f /etc/sudoers.d/90-sysaudit ] && sudo visudo -cf /etc/sudoers.d/90-sysaudit >/dev/null 2>&1; then
  if grep -q "%sysaudit.*NOPASSWD.*journalctl" /etc/sudoers.d/90-sysaudit; then
    echo -e "${GREEN}[PASS] Task 2: Sudoers rule validated for %sysaudit with NOPASSWD for journalctl.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 2: Rule content does not grant NOPASSWD for journalctl to %sysaudit.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 2: /etc/sudoers.d/90-sysaudit missing or syntax error.${NC}"
fi""",
        "lfcs_solution": """1. Group & user:
`sudo groupadd -g 2800 sysaudit`
`sudo usermod -aG sysaudit student`

2. Sudoers file:
`echo "%sysaudit ALL=(ALL) NOPASSWD: /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-sysaudit`
`sudo chmod 0440 /etc/sudoers.d/90-sysaudit`
`sudo visudo -cf /etc/sudoers.d/90-sysaudit`""",
        "lfcs_reset": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true""",
    },
    {
        "day": 3,
        "date": '2026-10-28',
        "title": 'Profiles, Template Environments & User Limits',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Template Environment (/etc/skel)
Place a default welcome document in `/etc/skel/WELCOME.txt`:
- Contents: `Corporate System Policy: All activity is monitored.`
- Ensure default permissions (`644`).

### Task 2: Global Profile Environment Variable
Create `/etc/profile.d/corp_vars.sh`:
- Export `CORPORATE_ENV="production"`
- Make it readable by all users.

### Task 3: Security Limits Configuration
In `/etc/security/limits.d/80-nofile.conf`, set:
- User `student` soft limit for open files (`nofile`) to `2048`.
- User `student` hard limit for open files (`nofile`) to `4096`.""",
        "setup": 'sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf',
        "verify": """SCORE=0; TOTAL=3
# Task 1: /etc/skel/WELCOME.txt
if [ -f /etc/skel/WELCOME.txt ] && grep -qi "All activity is monitored" /etc/skel/WELCOME.txt; then
  echo -e "${GREEN}[PASS] Task 1: /etc/skel/WELCOME.txt created and verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/skel/WELCOME.txt missing or text mismatch.${NC}"
fi

# Task 2: /etc/profile.d/corp_vars.sh
if [ -f /etc/profile.d/corp_vars.sh ] && grep -q 'CORPORATE_ENV="production"' /etc/profile.d/corp_vars.sh; then
  echo -e "${GREEN}[PASS] Task 2: /etc/profile.d/corp_vars.sh exports CORPORATE_ENV.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/profile.d/corp_vars.sh missing or variable missing.${NC}"
fi

# Task 3: limits.d
if [ -f /etc/security/limits.d/80-nofile.conf ] && grep -q "student.*soft.*nofile.*2048" /etc/security/limits.d/80-nofile.conf && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/80-nofile.conf; then
  echo -e "${GREEN}[PASS] Task 3: File limits for student configured in limits.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/80-nofile.conf missing or values incorrect.${NC}"
fi""",
        "solution": """1. Welcome template:
`echo "Corporate System Policy: All activity is monitored." | sudo tee /etc/skel/WELCOME.txt`
`sudo chmod 644 /etc/skel/WELCOME.txt`

2. Profile variable:
`echo 'export CORPORATE_ENV="production"' | sudo tee /etc/profile.d/corp_vars.sh`
`sudo chmod 644 /etc/profile.d/corp_vars.sh`

3. Limits:
`echo -e "student soft nofile 2048
student hard nofile 4096" | sudo tee /etc/security/limits.d/80-nofile.conf`""",
        "reset": 'sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf',
        "lfcs_title": 'Profiles, Template Environments & User Limits',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Template Environment (/etc/skel)
Place a default welcome document in `/etc/skel/WELCOME.txt`:
- Contents: `Corporate System Policy: All activity is monitored.`
- Ensure default permissions (`644`).

### Task 2: Global Profile Environment Variable
Create `/etc/profile.d/corp_vars.sh`:
- Export `CORPORATE_ENV="production"`
- Make it readable by all users.

### Task 3: Security Limits Configuration
In `/etc/security/limits.d/80-nofile.conf`, set:
- User `student` soft limit for open files (`nofile`) to `2048`.
- User `student` hard limit for open files (`nofile`) to `4096`.""",
        "lfcs_setup": 'sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf',
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: /etc/skel/WELCOME.txt
if [ -f /etc/skel/WELCOME.txt ] && grep -qi "All activity is monitored" /etc/skel/WELCOME.txt; then
  echo -e "${GREEN}[PASS] Task 1: /etc/skel/WELCOME.txt created and verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/skel/WELCOME.txt missing or text mismatch.${NC}"
fi

# Task 2: /etc/profile.d/corp_vars.sh
if [ -f /etc/profile.d/corp_vars.sh ] && grep -q 'CORPORATE_ENV="production"' /etc/profile.d/corp_vars.sh; then
  echo -e "${GREEN}[PASS] Task 2: /etc/profile.d/corp_vars.sh exports CORPORATE_ENV.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/profile.d/corp_vars.sh missing or variable missing.${NC}"
fi

# Task 3: limits.d
if [ -f /etc/security/limits.d/80-nofile.conf ] && grep -q "student.*soft.*nofile.*2048" /etc/security/limits.d/80-nofile.conf && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/80-nofile.conf; then
  echo -e "${GREEN}[PASS] Task 3: File limits for student configured in limits.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/80-nofile.conf missing or values incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Welcome template:
`echo "Corporate System Policy: All activity is monitored." | sudo tee /etc/skel/WELCOME.txt`
`sudo chmod 644 /etc/skel/WELCOME.txt`

2. Profile variable:
`echo 'export CORPORATE_ENV="production"' | sudo tee /etc/profile.d/corp_vars.sh`
`sudo chmod 644 /etc/profile.d/corp_vars.sh`

3. Limits:
`echo -e "student soft nofile 2048
student hard nofile 4096" | sudo tee /etc/security/limits.d/80-nofile.conf`""",
        "lfcs_reset": 'sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf',
    },
    {
        "day": 4,
        "date": '2026-10-29',
        "title": 'Kernel Runtime Tuning with Sysctl',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Network Parameter Hardening
Configure persistent network parameters in `/etc/sysctl.d/60-hardening.conf`:
- `net.ipv4.ip_forward = 1`
- `net.ipv4.icmp_echo_ignore_broadcasts = 1`

### Task 2: Apply and Verify Parameters
1. Apply the configuration immediately using `sysctl -p /etc/sysctl.d/60-hardening.conf`.
2. Save the active values of `net.ipv4.ip_forward` and `net.ipv4.icmp_echo_ignore_broadcasts` into `/var/tmp/kernel_params.txt`.""",
        "setup": 'sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt',
        "verify": """SCORE=0; TOTAL=2
# Task 1 & 2: sysctl settings active
IP_FWD=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
ICMP_IGN=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")

if [ "$IP_FWD" == "1" ] && [ "$ICMP_IGN" == "1" ] && [ -f /etc/sysctl.d/60-hardening.conf ]; then
  echo -e "${GREEN}[PASS] Task 1: Kernel parameters active and configured in /etc/sysctl.d/60-hardening.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Parameters not active (ip_forward=$IP_FWD, icmp_ignore=$ICMP_IGN).${NC}"
fi

if [ -f /var/tmp/kernel_params.txt ] && grep -q "net.ipv4.ip_forward = 1" /var/tmp/kernel_params.txt; then
  echo -e "${GREEN}[PASS] Task 2: Active parameters recorded in /var/tmp/kernel_params.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/kernel_params.txt missing or incomplete.${NC}"
fi""",
        "solution": """1. Create sysctl configuration:
```ini
net.ipv4.ip_forward = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
```
`sudo tee /etc/sysctl.d/60-hardening.conf`
`sudo sysctl -p /etc/sysctl.d/60-hardening.conf`

2. Record:
`sysctl net.ipv4.ip_forward net.ipv4.icmp_echo_ignore_broadcasts > /var/tmp/kernel_params.txt`""",
        "reset": 'sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt',
        "lfcs_title": 'Kernel Runtime Tuning with Sysctl',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Network Parameter Hardening
Configure persistent network parameters in `/etc/sysctl.d/60-hardening.conf`:
- `net.ipv4.ip_forward = 1`
- `net.ipv4.icmp_echo_ignore_broadcasts = 1`

### Task 2: Apply and Verify Parameters
1. Apply the configuration immediately using `sysctl -p /etc/sysctl.d/60-hardening.conf`.
2. Save the active values of `net.ipv4.ip_forward` and `net.ipv4.icmp_echo_ignore_broadcasts` into `/var/tmp/kernel_params.txt`.""",
        "lfcs_setup": 'sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt',
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: sysctl settings active
IP_FWD=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
ICMP_IGN=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")

if [ "$IP_FWD" == "1" ] && [ "$ICMP_IGN" == "1" ] && [ -f /etc/sysctl.d/60-hardening.conf ]; then
  echo -e "${GREEN}[PASS] Task 1: Kernel parameters active and configured in /etc/sysctl.d/60-hardening.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Parameters not active (ip_forward=$IP_FWD, icmp_ignore=$ICMP_IGN).${NC}"
fi

if [ -f /var/tmp/kernel_params.txt ] && grep -q "net.ipv4.ip_forward = 1" /var/tmp/kernel_params.txt; then
  echo -e "${GREEN}[PASS] Task 2: Active parameters recorded in /var/tmp/kernel_params.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/kernel_params.txt missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Create sysctl configuration:
```ini
net.ipv4.ip_forward = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
```
`sudo tee /etc/sysctl.d/60-hardening.conf`
`sudo sysctl -p /etc/sysctl.d/60-hardening.conf`

2. Record:
`sysctl net.ipv4.ip_forward net.ipv4.icmp_echo_ignore_broadcasts > /var/tmp/kernel_params.txt`""",
        "lfcs_reset": 'sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt',
    },
    {
        "day": 5,
        "date": '2026-10-30',
        "title": 'Mandatory Access Control: SELinux & AppArmor',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Audit AppArmor Status
Check the status of AppArmor on Ubuntu:
1. Run `aa-status` to evaluate active profiles.
2. Save the summary of loaded and enforcing profiles to `/var/tmp/apparmor_summary.txt`.

### Task 2: Inspect Profile Directory
List all profiles located in `/etc/apparmor.d/` and output their names to `/var/tmp/apparmor_profiles.txt`.""",
        "setup": 'sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt',
        "verify": """SCORE=0; TOTAL=2
# Task 1: apparmor_summary.txt
if [ -f /var/tmp/apparmor_summary.txt ] && grep -qiE "profiles are in enforce mode|profiles are loaded" /var/tmp/apparmor_summary.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/apparmor_summary.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/apparmor_summary.txt missing or invalid.${NC}"
fi

# Task 2: apparmor_profiles.txt
if [ -f /var/tmp/apparmor_profiles.txt ] && [ $(wc -l < /var/tmp/apparmor_profiles.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/apparmor_profiles.txt contains profile listings.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/apparmor_profiles.txt missing or has fewer than 5 entries.${NC}"
fi""",
        "solution": """1. AppArmor status:
`sudo aa-status > /var/tmp/apparmor_summary.txt`

2. Profiles list:
`ls /etc/apparmor.d > /var/tmp/apparmor_profiles.txt`""",
        "reset": 'sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt',
        "lfcs_title": 'Mandatory Access Control: SELinux & AppArmor',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Audit AppArmor Status
Check the status of AppArmor on Ubuntu:
1. Run `aa-status` to evaluate active profiles.
2. Save the summary of loaded and enforcing profiles to `/var/tmp/apparmor_summary.txt`.

### Task 2: Inspect Profile Directory
List all profiles located in `/etc/apparmor.d/` and output their names to `/var/tmp/apparmor_profiles.txt`.""",
        "lfcs_setup": 'sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt',
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: apparmor_summary.txt
if [ -f /var/tmp/apparmor_summary.txt ] && grep -qiE "profiles are in enforce mode|profiles are loaded" /var/tmp/apparmor_summary.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/apparmor_summary.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/apparmor_summary.txt missing or invalid.${NC}"
fi

# Task 2: apparmor_profiles.txt
if [ -f /var/tmp/apparmor_profiles.txt ] && [ $(wc -l < /var/tmp/apparmor_profiles.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/apparmor_profiles.txt contains profile listings.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/apparmor_profiles.txt missing or has fewer than 5 entries.${NC}"
fi""",
        "lfcs_solution": """1. AppArmor status:
`sudo aa-status > /var/tmp/apparmor_summary.txt`

2. Profiles list:
`ls /etc/apparmor.d > /var/tmp/apparmor_profiles.txt`""",
        "lfcs_reset": 'sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt',
    },
    {
        "day": 6,
        "date": '2026-10-31',
        "title": 'Security Audit, User Quarantine & Recovery',
        "diff": 'Hard (Milestone Assessment 5)',
        "time": '45m',
        "tasks": """### Milestone 5 Triathlon Tasks:
1. **Quarantine Compromised User Account**:
   A compromised user account `hacked_service` exists on the system.
   - Lock the password using `passwd -l`.
   - Change the login shell to `/usr/sbin/nologin` or `/bin/false`.
   - Expire the account immediately with `chage -E 0 hacked_service`.

2. **Sudoers Audit & Drop-In Hardening**:
   Ensure `/etc/sudoers.d/99-quarantine` allows user `student` full sudo with `NOPASSWD: ALL` and contains no insecure wildcard directives for quarantined users.

3. **Sysctl Kernel Protection**:
   Ensure `/etc/sysctl.d/99-security.conf` enforces `net.ipv4.tcp_syncookies = 1` and `net.ipv4.conf.all.rp_filter = 1`. Apply with `sysctl -p`.""",
        "setup": """sudo userdel -r hacked_service 2>/dev/null || true
sudo useradd -m -s /bin/bash hacked_service
echo "hacked_service:P@ss123" | sudo chpasswd
sudo rm -f /etc/sysctl.d/99-security.conf""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: hacked_service quarantined
SHELL_HS=$(getent passwd hacked_service | cut -d: -f7 || echo "")
CHAGE_EXP=$(chage -l hacked_service | grep "Account expires" | awk -F: '{print $2}' | tr -d ' ' || echo "")
if [[ "$SHELL_HS" =~ (nologin|false) ]] && [ "$CHAGE_EXP" != "never" ]; then
  echo -e "${GREEN}[PASS] Task 1: hacked_service account is quarantined (shell=$SHELL_HS, expired).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: hacked_service still has shell $SHELL_HS or not expired ($CHAGE_EXP).${NC}"
fi

# Task 2: sudoers valid
if sudo visudo -c >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Sudoers configuration syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Sudoers configuration syntax error.${NC}"
fi

# Task 3: sysctl
SYNC=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
RPF=$(sysctl -n net.ipv4.conf.all.rp_filter 2>/dev/null || echo "0")
if [ "$SYNC" == "1" ] && [ "$RPF" == "1" ]; then
  echo -e "${GREEN}[PASS] Task 3: Kernel security parameters active (syncookies=1, rp_filter=1).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Parameters not set (syncookies=$SYNC, rp_filter=$RPF).${NC}"
fi""",
        "solution": """1. Quarantine:
`sudo passwd -l hacked_service`
`sudo usermod -s /usr/sbin/nologin hacked_service`
`sudo chage -E 0 hacked_service`

2. Sudoers:
`sudo visudo -c`

3. Sysctl:
`echo -e "net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1" | sudo tee /etc/sysctl.d/99-security.conf`
`sudo sysctl -p /etc/sysctl.d/99-security.conf`""",
        "reset": """sudo userdel -r hacked_service 2>/dev/null || true
sudo rm -f /etc/sysctl.d/99-security.conf""",
        "lfcs_title": 'Security Audit, User Quarantine & Recovery',
        "lfcs_diff": 'Hard (Milestone Assessment 5)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 5 Triathlon Tasks:
1. **Quarantine Compromised User Account**:
   A compromised user account `hacked_service` exists on the system.
   - Lock the password using `passwd -l`.
   - Change the login shell to `/usr/sbin/nologin` or `/bin/false`.
   - Expire the account immediately with `chage -E 0 hacked_service`.

2. **Sudoers Audit & Drop-In Hardening**:
   Ensure `/etc/sudoers.d/99-quarantine` allows user `student` full sudo with `NOPASSWD: ALL` and contains no insecure wildcard directives for quarantined users.

3. **Sysctl Kernel Protection**:
   Ensure `/etc/sysctl.d/99-security.conf` enforces `net.ipv4.tcp_syncookies = 1` and `net.ipv4.conf.all.rp_filter = 1`. Apply with `sysctl -p`.""",
        "lfcs_setup": """sudo userdel -r hacked_service 2>/dev/null || true
sudo useradd -m -s /bin/bash hacked_service
echo "hacked_service:P@ss123" | sudo chpasswd
sudo rm -f /etc/sysctl.d/99-security.conf""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: hacked_service quarantined
SHELL_HS=$(getent passwd hacked_service | cut -d: -f7 || echo "")
CHAGE_EXP=$(chage -l hacked_service | grep "Account expires" | awk -F: '{print $2}' | tr -d ' ' || echo "")
if [[ "$SHELL_HS" =~ (nologin|false) ]] && [ "$CHAGE_EXP" != "never" ]; then
  echo -e "${GREEN}[PASS] Task 1: hacked_service account is quarantined (shell=$SHELL_HS, expired).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: hacked_service still has shell $SHELL_HS or not expired ($CHAGE_EXP).${NC}"
fi

# Task 2: sudoers valid
if sudo visudo -c >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Sudoers configuration syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Sudoers configuration syntax error.${NC}"
fi

# Task 3: sysctl
SYNC=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
RPF=$(sysctl -n net.ipv4.conf.all.rp_filter 2>/dev/null || echo "0")
if [ "$SYNC" == "1" ] && [ "$RPF" == "1" ]; then
  echo -e "${GREEN}[PASS] Task 3: Kernel security parameters active (syncookies=1, rp_filter=1).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Parameters not set (syncookies=$SYNC, rp_filter=$RPF).${NC}"
fi""",
        "lfcs_solution": """1. Quarantine:
`sudo passwd -l hacked_service`
`sudo usermod -s /usr/sbin/nologin hacked_service`
`sudo chage -E 0 hacked_service`

2. Sudoers:
`sudo visudo -c`

3. Sysctl:
`echo -e "net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1" | sudo tee /etc/sysctl.d/99-security.conf`
`sudo sysctl -p /etc/sysctl.d/99-security.conf`""",
        "lfcs_reset": """sudo userdel -r hacked_service 2>/dev/null || true
sudo rm -f /etc/sysctl.d/99-security.conf""",
    },
]
