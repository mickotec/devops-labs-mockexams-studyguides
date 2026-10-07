"""
Dedicated LFCS Lab Definitions for Week 4 (Days 1 to 6).
"""

WEEK_4_LABS = [
    {
        "day": 1,
        "date": '2026-10-19',
        "title": 'Journald & System Log File Analysis',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Error-Level Journal Extraction
Query `journalctl` to extract all system log messages with priority `err` or higher (`err`, `crit`, `alert`, `emerg`) recorded since boot (`-b`).
- Output the entries to `/var/tmp/system_errors.log`.

### Task 2: Service Unit Log Extraction
Extract the 20 most recent journal lines for the `ssh` service unit (`-u ssh`).
- Save the output to `/var/tmp/ssh_service.log`.

### Task 3: Journal Disk Space Audit
Check the current disk usage consumed by systemd journal files using `journalctl --disk-usage`.
- Save the exact output line to `/var/tmp/journal_usage.txt`.""",
        "setup": 'sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt',
        "verify": """SCORE=0; TOTAL=3
# Task 1: system_errors.log
if [ -f /var/tmp/system_errors.log ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_errors.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_errors.log missing.${NC}"
fi

# Task 2: ssh_service.log has entries
if [ -f /var/tmp/ssh_service.log ] && [ -s /var/tmp/ssh_service.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/ssh_service.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/ssh_service.log missing or empty.${NC}"
fi

# Task 3: journal_usage.txt
if [ -f /var/tmp/journal_usage.txt ] && grep -qiE "Archived|Active|take up" /var/tmp/journal_usage.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/journal_usage.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/journal_usage.txt missing or lacks usage metrics.${NC}"
fi""",
        "solution": """1. Query error logs:
`journalctl -b -p err..emerg --no-pager > /var/tmp/system_errors.log`

2. SSH service logs:
`journalctl -u ssh -n 20 --no-pager > /var/tmp/ssh_service.log`

3. Journal disk usage:
`journalctl --disk-usage > /var/tmp/journal_usage.txt`""",
        "reset": 'sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt',
        "lfcs_title": 'Journald & System Log File Analysis',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Error-Level Journal Extraction
Query `journalctl` to extract all system log messages with priority `err` or higher (`err`, `crit`, `alert`, `emerg`) recorded since boot (`-b`).
- Output the entries to `/var/tmp/system_errors.log`.

### Task 2: Service Unit Log Extraction
Extract the 20 most recent journal lines for the `ssh` service unit (`-u ssh`).
- Save the output to `/var/tmp/ssh_service.log`.

### Task 3: Journal Disk Space Audit
Check the current disk usage consumed by systemd journal files using `journalctl --disk-usage`.
- Save the exact output line to `/var/tmp/journal_usage.txt`.""",
        "lfcs_setup": 'sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt',
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: system_errors.log
if [ -f /var/tmp/system_errors.log ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_errors.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_errors.log missing.${NC}"
fi

# Task 2: ssh_service.log has entries
if [ -f /var/tmp/ssh_service.log ] && [ -s /var/tmp/ssh_service.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/ssh_service.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/ssh_service.log missing or empty.${NC}"
fi

# Task 3: journal_usage.txt
if [ -f /var/tmp/journal_usage.txt ] && grep -qiE "Archived|Active|take up" /var/tmp/journal_usage.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/journal_usage.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/journal_usage.txt missing or lacks usage metrics.${NC}"
fi""",
        "lfcs_solution": """1. Query error logs:
`journalctl -b -p err..emerg --no-pager > /var/tmp/system_errors.log`

2. SSH service logs:
`journalctl -u ssh -n 20 --no-pager > /var/tmp/ssh_service.log`

3. Journal disk usage:
`journalctl --disk-usage > /var/tmp/journal_usage.txt`""",
        "lfcs_reset": 'sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt',
    },
    {
        "day": 2,
        "date": '2026-10-20',
        "title": 'Task Scheduling with Cron and At',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: System-Wide Crontab
Create a system crontab file `/etc/cron.d/sync-audit`:
- Schedule: Every 15 minutes (`*/15 * * * *`)
- User: `root`
- Command: `/bin/echo "Sync executed at $(date)" >> /var/log/sync-audit.log`
- Ensure correct permissions (`chmod 644`).

### Task 2: User Crontab Configuration
Configure a crontab entry for user `student`:
- Schedule: Every day at 03:30 AM (`30 3 * * *`)
- Command: `/bin/date >> /var/tmp/daily_timestamp.txt`

### Task 3: Access Control for At Jobs
Ensure only user `student` is permitted to schedule `at` jobs:
1. Create `/etc/at.allow` containing only `student`.
2. Ensure `/etc/at.deny` does not exist.""",
        "setup": """sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: /etc/cron.d/sync-audit
if [ -f /etc/cron.d/sync-audit ] && grep -qiE "\*/15\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/sync-audit; then
  echo -e "${GREEN}[PASS] Task 1: /etc/cron.d/sync-audit configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/cron.d/sync-audit missing or syntax incorrect.${NC}"
fi

# Task 2: student user crontab
STUDENT_CRON=$(crontab -u student -l 2>/dev/null || true)
if echo "$STUDENT_CRON" | grep -qiE "30\s+3\s+\*\s+\*\s+\*"; then
  echo -e "${GREEN}[PASS] Task 2: User student crontab configured for 03:30 AM.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: student crontab missing or schedule incorrect.${NC}"
fi

# Task 3: /etc/at.allow
if [ -f /etc/at.allow ] && grep -q "^student$" /etc/at.allow; then
  echo -e "${GREEN}[PASS] Task 3: /etc/at.allow restricts access to student.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/at.allow missing or does not specify student.${NC}"
fi""",
        "solution": """1. System crontab:
`echo "*/15 * * * * root /bin/echo "Sync executed at \$(date)" >> /var/log/sync-audit.log" | sudo tee /etc/cron.d/sync-audit`
`sudo chmod 644 /etc/cron.d/sync-audit`

2. User crontab:
`(crontab -u student -l 2>/dev/null; echo "30 3 * * * /bin/date >> /var/tmp/daily_timestamp.txt") | crontab -u student -`

3. At allow:
`echo "student" | sudo tee /etc/at.allow`
`sudo rm -f /etc/at.deny`""",
        "reset": """sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true""",
        "lfcs_title": 'Task Scheduling with Cron and At',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: System-Wide Crontab
Create a system crontab file `/etc/cron.d/sync-audit`:
- Schedule: Every 15 minutes (`*/15 * * * *`)
- User: `root`
- Command: `/bin/echo "Sync executed at $(date)" >> /var/log/sync-audit.log`
- Ensure correct permissions (`chmod 644`).

### Task 2: User Crontab Configuration
Configure a crontab entry for user `student`:
- Schedule: Every day at 03:30 AM (`30 3 * * *`)
- Command: `/bin/date >> /var/tmp/daily_timestamp.txt`

### Task 3: Access Control for At Jobs
Ensure only user `student` is permitted to schedule `at` jobs:
1. Create `/etc/at.allow` containing only `student`.
2. Ensure `/etc/at.deny` does not exist.""",
        "lfcs_setup": """sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: /etc/cron.d/sync-audit
if [ -f /etc/cron.d/sync-audit ] && grep -qiE "\*/15\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/sync-audit; then
  echo -e "${GREEN}[PASS] Task 1: /etc/cron.d/sync-audit configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/cron.d/sync-audit missing or syntax incorrect.${NC}"
fi

# Task 2: student user crontab
STUDENT_CRON=$(crontab -u student -l 2>/dev/null || true)
if echo "$STUDENT_CRON" | grep -qiE "30\s+3\s+\*\s+\*\s+\*"; then
  echo -e "${GREEN}[PASS] Task 2: User student crontab configured for 03:30 AM.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: student crontab missing or schedule incorrect.${NC}"
fi

# Task 3: /etc/at.allow
if [ -f /etc/at.allow ] && grep -q "^student$" /etc/at.allow; then
  echo -e "${GREEN}[PASS] Task 3: /etc/at.allow restricts access to student.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/at.allow missing or does not specify student.${NC}"
fi""",
        "lfcs_solution": """1. System crontab:
`echo "*/15 * * * * root /bin/echo "Sync executed at \$(date)" >> /var/log/sync-audit.log" | sudo tee /etc/cron.d/sync-audit`
`sudo chmod 644 /etc/cron.d/sync-audit`

2. User crontab:
`(crontab -u student -l 2>/dev/null; echo "30 3 * * * /bin/date >> /var/tmp/daily_timestamp.txt") | crontab -u student -`

3. At allow:
`echo "student" | sudo tee /etc/at.allow`
`sudo rm -f /etc/at.deny`""",
        "lfcs_reset": """sudo rm -f /etc/cron.d/sync-audit /var/log/sync-audit.log /var/tmp/daily_timestamp.txt /etc/at.allow
sudo crontab -u student -r 2>/dev/null || true""",
    },
    {
        "day": 3,
        "date": '2026-10-21',
        "title": 'Package Managers (APT, DNF/YUM & RPM)',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Package Version & File Query
Find which package owns `/usr/bin/tar` and record the package name and installed version into `/var/tmp/tar_package.txt` (use `dpkg -S` and `dpkg -l` or `apt-cache policy`).

### Task 2: Pin Package Version with apt-mark
Place a package hold on `tar` to prevent it from being upgraded during automated system upgrades.
- Confirm with `apt-mark showhold`.

### Task 3: Download Debian Package Archive Without Installing
Download the `.deb` package file for `tree` into directory `/var/tmp/pkg_cache/` using `apt-get download`.""",
        "setup": """sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache
mkdir -p /var/tmp/pkg_cache""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: tar_package.txt
if [ -f /var/tmp/tar_package.txt ] && grep -qi "tar" /var/tmp/tar_package.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/tar_package.txt created with package ownership details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/tar_package.txt missing or lacks tar info.${NC}"
fi

# Task 2: apt-mark showhold has tar
HOLD=$(apt-mark showhold 2>/dev/null || true)
if echo "$HOLD" | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 2: Package 'tar' is pinned (hold) in apt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Package 'tar' is not held.${NC}"
fi

# Task 3: .deb file in /var/tmp/pkg_cache/
DEB_COUNT=$(ls /var/tmp/pkg_cache/*.deb 2>/dev/null | wc -l)
if [ "$DEB_COUNT" -ge 1 ]; then
  echo -e "${GREEN}[PASS] Task 3: Debian package downloaded to /var/tmp/pkg_cache/.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: No .deb package found in /var/tmp/pkg_cache/.${NC}"
fi""",
        "solution": """1. Query tar:
`dpkg -S /usr/bin/tar > /var/tmp/tar_package.txt`
`dpkg -l tar >> /var/tmp/tar_package.txt`

2. Hold tar:
`sudo apt-mark hold tar`

3. Download deb:
`cd /var/tmp/pkg_cache && apt-get download tree`""",
        "reset": """sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache""",
        "lfcs_title": 'Package Managers (APT, DNF/YUM & RPM)',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Package Version & File Query
Find which package owns `/usr/bin/tar` and record the package name and installed version into `/var/tmp/tar_package.txt` (use `dpkg -S` and `dpkg -l` or `apt-cache policy`).

### Task 2: Pin Package Version with apt-mark
Place a package hold on `tar` to prevent it from being upgraded during automated system upgrades.
- Confirm with `apt-mark showhold`.

### Task 3: Download Debian Package Archive Without Installing
Download the `.deb` package file for `tree` into directory `/var/tmp/pkg_cache/` using `apt-get download`.""",
        "lfcs_setup": """sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache
mkdir -p /var/tmp/pkg_cache""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: tar_package.txt
if [ -f /var/tmp/tar_package.txt ] && grep -qi "tar" /var/tmp/tar_package.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/tar_package.txt created with package ownership details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/tar_package.txt missing or lacks tar info.${NC}"
fi

# Task 2: apt-mark showhold has tar
HOLD=$(apt-mark showhold 2>/dev/null || true)
if echo "$HOLD" | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 2: Package 'tar' is pinned (hold) in apt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Package 'tar' is not held.${NC}"
fi

# Task 3: .deb file in /var/tmp/pkg_cache/
DEB_COUNT=$(ls /var/tmp/pkg_cache/*.deb 2>/dev/null | wc -l)
if [ "$DEB_COUNT" -ge 1 ]; then
  echo -e "${GREEN}[PASS] Task 3: Debian package downloaded to /var/tmp/pkg_cache/.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: No .deb package found in /var/tmp/pkg_cache/.${NC}"
fi""",
        "lfcs_solution": """1. Query tar:
`dpkg -S /usr/bin/tar > /var/tmp/tar_package.txt`
`dpkg -l tar >> /var/tmp/tar_package.txt`

2. Hold tar:
`sudo apt-mark hold tar`

3. Download deb:
`cd /var/tmp/pkg_cache && apt-get download tree`""",
        "lfcs_reset": """sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache""",
    },
    {
        "day": 4,
        "date": '2026-10-22',
        "title": 'Compiling Software from Source Code',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Extract Source Code Archive
A C source code archive `/var/tmp/hello-c.tar.gz` has been prepared.
- Extract it into `/var/tmp/src-build/`.

### Task 2: Compile with GCC
Compile the extracted source code `hello.c` using `gcc` into an optimized binary at `/usr/local/bin/hello-app`:
- Ensure executable permissions (`chmod 755 /usr/local/bin/hello-app`).

### Task 3: Verify Binary Execution
Execute `/usr/local/bin/hello-app` and write its output to `/var/tmp/hello_output.txt`.""",
        "setup": """sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt
mkdir -p /tmp/pkg-source
cat << "EOF" > /tmp/pkg-source/hello.c
#include <stdio.h>
int main() {
    printf("LFCS Source Compilation Successful: v1.0.0\n");
    return 0;
}
EOF
tar -czf /var/tmp/hello-c.tar.gz -C /tmp/pkg-source hello.c
rm -rf /tmp/pkg-source""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: extracted source
if [ -f /var/tmp/src-build/hello.c ]; then
  echo -e "${GREEN}[PASS] Task 1: Source code extracted to /var/tmp/src-build/hello.c.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/src-build/hello.c not found.${NC}"
fi

# Task 2: compiled binary
if [ -x /usr/local/bin/hello-app ]; then
  echo -e "${GREEN}[PASS] Task 2: Compiled binary /usr/local/bin/hello-app exists and is executable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /usr/local/bin/hello-app missing or not executable.${NC}"
fi

# Task 3: execution output
if [ -f /var/tmp/hello_output.txt ] && grep -q "LFCS Source Compilation Successful" /var/tmp/hello_output.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/hello_output.txt verified with correct binary output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/hello_output.txt missing or output incorrect.${NC}"
fi""",
        "solution": """1. Extract:
`mkdir -p /var/tmp/src-build`
`tar -xzf /var/tmp/hello-c.tar.gz -C /var/tmp/src-build`

2. Compile:
`sudo gcc -O2 /var/tmp/src-build/hello.c -o /usr/local/bin/hello-app`
`sudo chmod 755 /usr/local/bin/hello-app`

3. Verify:
`/usr/local/bin/hello-app > /var/tmp/hello_output.txt`""",
        "reset": 'sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt',
        "lfcs_title": 'Compiling Software from Source Code',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Extract Source Code Archive
A C source code archive `/var/tmp/hello-c.tar.gz` has been prepared.
- Extract it into `/var/tmp/src-build/`.

### Task 2: Compile with GCC
Compile the extracted source code `hello.c` using `gcc` into an optimized binary at `/usr/local/bin/hello-app`:
- Ensure executable permissions (`chmod 755 /usr/local/bin/hello-app`).

### Task 3: Verify Binary Execution
Execute `/usr/local/bin/hello-app` and write its output to `/var/tmp/hello_output.txt`.""",
        "lfcs_setup": """sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt
mkdir -p /tmp/pkg-source
cat << "EOF" > /tmp/pkg-source/hello.c
#include <stdio.h>
int main() {
    printf("LFCS Source Compilation Successful: v1.0.0\n");
    return 0;
}
EOF
tar -czf /var/tmp/hello-c.tar.gz -C /tmp/pkg-source hello.c
rm -rf /tmp/pkg-source""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: extracted source
if [ -f /var/tmp/src-build/hello.c ]; then
  echo -e "${GREEN}[PASS] Task 1: Source code extracted to /var/tmp/src-build/hello.c.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/src-build/hello.c not found.${NC}"
fi

# Task 2: compiled binary
if [ -x /usr/local/bin/hello-app ]; then
  echo -e "${GREEN}[PASS] Task 2: Compiled binary /usr/local/bin/hello-app exists and is executable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /usr/local/bin/hello-app missing or not executable.${NC}"
fi

# Task 3: execution output
if [ -f /var/tmp/hello_output.txt ] && grep -q "LFCS Source Compilation Successful" /var/tmp/hello_output.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/hello_output.txt verified with correct binary output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/hello_output.txt missing or output incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Extract:
`mkdir -p /var/tmp/src-build`
`tar -xzf /var/tmp/hello-c.tar.gz -C /var/tmp/src-build`

2. Compile:
`sudo gcc -O2 /var/tmp/src-build/hello.c -o /usr/local/bin/hello-app`
`sudo chmod 755 /usr/local/bin/hello-app`

3. Verify:
`/usr/local/bin/hello-app > /var/tmp/hello_output.txt`""",
        "lfcs_reset": 'sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt',
    },
    {
        "day": 5,
        "date": '2026-10-23',
        "title": 'Bash Automation & Maintenance Scripting',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Robust Maintenance Script
Create an automated log cleanup and audit script at `/usr/local/bin/daily-maint.sh`:
- Script must be executable (`chmod 755`).
- Ensure `set -euo pipefail` is used.
- Script accepts a target directory as argument `$1`. If `$1` is not provided, exit with code `1` and error message `Usage: daily-maint.sh <dir>`.
- Count all `.log` files in `$1` and append `[$(date)] Processed logs in $1: <count> files` to `/var/log/daily-maint.log`.
- Emit a syslog message with tag `daily-maint`: `Maintenance completed for $1`.

### Task 2: Test Execution
Run `/usr/local/bin/daily-maint.sh /var/log` and verify `/var/log/daily-maint.log` receives the log summary.""",
        "setup": 'sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log',
        "verify": """SCORE=0; TOTAL=2
# Task 1: script executable and handles arguments
if [ -x /usr/local/bin/daily-maint.sh ]; then
  ERR_OUT=$(/usr/local/bin/daily-maint.sh 2>&1 || true)
  if echo "$ERR_OUT" | grep -qi "Usage:"; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/daily-maint.sh exists, executable, and validates arguments.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: Script did not exit with Usage message when no argument was passed.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/daily-maint.sh missing or not executable.${NC}"
fi

# Task 2: log file updated
if [ -f /var/log/daily-maint.log ] && grep -qi "Processed logs" /var/log/daily-maint.log; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/daily-maint.log verified with processed logs summary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/daily-maint.log missing or missing log entry.${NC}"
fi""",
        "solution": """1. Create `/usr/local/bin/daily-maint.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: daily-maint.sh <dir>" >&2
  exit 1
fi

TARGET_DIR="$1"
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist" >&2
  exit 2
fi

COUNT=$(find "$TARGET_DIR" -maxdepth 1 -name "*.log" 2>/dev/null | wc -l)
echo "[$(date)] Processed logs in $TARGET_DIR: $COUNT files" >> /var/log/daily-maint.log
logger -t daily-maint "Maintenance completed for $TARGET_DIR"
```
`sudo chmod 755 /usr/local/bin/daily-maint.sh`

2. Run test:
`sudo /usr/local/bin/daily-maint.sh /var/log`""",
        "reset": 'sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log',
        "lfcs_title": 'Bash Automation & Maintenance Scripting',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Robust Maintenance Script
Create an automated log cleanup and audit script at `/usr/local/bin/daily-maint.sh`:
- Script must be executable (`chmod 755`).
- Ensure `set -euo pipefail` is used.
- Script accepts a target directory as argument `$1`. If `$1` is not provided, exit with code `1` and error message `Usage: daily-maint.sh <dir>`.
- Count all `.log` files in `$1` and append `[$(date)] Processed logs in $1: <count> files` to `/var/log/daily-maint.log`.
- Emit a syslog message with tag `daily-maint`: `Maintenance completed for $1`.

### Task 2: Test Execution
Run `/usr/local/bin/daily-maint.sh /var/log` and verify `/var/log/daily-maint.log` receives the log summary.""",
        "lfcs_setup": 'sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log',
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: script executable and handles arguments
if [ -x /usr/local/bin/daily-maint.sh ]; then
  ERR_OUT=$(/usr/local/bin/daily-maint.sh 2>&1 || true)
  if echo "$ERR_OUT" | grep -qi "Usage:"; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/daily-maint.sh exists, executable, and validates arguments.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: Script did not exit with Usage message when no argument was passed.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/daily-maint.sh missing or not executable.${NC}"
fi

# Task 2: log file updated
if [ -f /var/log/daily-maint.log ] && grep -qi "Processed logs" /var/log/daily-maint.log; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/daily-maint.log verified with processed logs summary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/daily-maint.log missing or missing log entry.${NC}"
fi""",
        "lfcs_solution": """1. Create `/usr/local/bin/daily-maint.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: daily-maint.sh <dir>" >&2
  exit 1
fi

TARGET_DIR="$1"
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist" >&2
  exit 2
fi

COUNT=$(find "$TARGET_DIR" -maxdepth 1 -name "*.log" 2>/dev/null | wc -l)
echo "[$(date)] Processed logs in $TARGET_DIR: $COUNT files" >> /var/log/daily-maint.log
logger -t daily-maint "Maintenance completed for $TARGET_DIR"
```
`sudo chmod 755 /usr/local/bin/daily-maint.sh`

2. Run test:
`sudo /usr/local/bin/daily-maint.sh /var/log`""",
        "lfcs_reset": 'sudo rm -f /usr/local/bin/daily-maint.sh /var/log/daily-maint.log',
    },
    {
        "day": 6,
        "date": '2026-10-24',
        "title": 'Week 4 System Automation & Maintenance Triathlon',
        "diff": 'Hard (Milestone Assessment 4)',
        "time": '45m',
        "tasks": """### Milestone 4 Triathlon Tasks:
1. **Automated Audit Pipeline**:
   Create `/usr/local/bin/log-auditor.sh`:
   - Extracts all journal entries with priority `err` from the last 2 hours.
   - Saves them to `/var/log/audit/recent_errors.log` (create directory if missing).
   - Counts the error lines and appends `[$(date)] Found <count> errors` to `/var/log/audit/summary.log`.

2. **Crontab Automation**:
   Add a root crontab entry in `/etc/cron.d/log-audit` running `/usr/local/bin/log-auditor.sh` every 30 minutes (`*/30 * * * * root /usr/local/bin/log-auditor.sh`).

3. **Package Hold and Source Build**:
   Verify `tar` is held with `apt-mark hold tar`.
   Verify `/usr/local/bin/log-auditor.sh` is executable by root.""",
        "setup": """sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: script exists and works
if [ -x /usr/local/bin/log-auditor.sh ]; then
  sudo /usr/local/bin/log-auditor.sh
  if [ -f /var/log/audit/summary.log ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/log-auditor.sh executed and generated summary.log.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/log/audit/summary.log not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/log-auditor.sh missing or not executable.${NC}"
fi

# Task 2: cron.d file
if [ -f /etc/cron.d/log-audit ] && grep -qiE "\*/30\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/log-audit; then
  echo -e "${GREEN}[PASS] Task 2: /etc/cron.d/log-audit cron schedule verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/cron.d/log-audit missing or invalid schedule.${NC}"
fi

# Task 3: package hold
if apt-mark showhold | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 3: Package tar is held.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Package tar is not held.${NC}"
fi""",
        "solution": """1. Script `/usr/local/bin/log-auditor.sh`:
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
`sudo apt-mark hold tar`""",
        "reset": """sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true""",
        "lfcs_title": 'Week 4 System Automation & Maintenance Triathlon',
        "lfcs_diff": 'Hard (Milestone Assessment 4)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 4 Triathlon Tasks:
1. **Automated Audit Pipeline**:
   Create `/usr/local/bin/log-auditor.sh`:
   - Extracts all journal entries with priority `err` from the last 2 hours.
   - Saves them to `/var/log/audit/recent_errors.log` (create directory if missing).
   - Counts the error lines and appends `[$(date)] Found <count> errors` to `/var/log/audit/summary.log`.

2. **Crontab Automation**:
   Add a root crontab entry in `/etc/cron.d/log-audit` running `/usr/local/bin/log-auditor.sh` every 30 minutes (`*/30 * * * * root /usr/local/bin/log-auditor.sh`).

3. **Package Hold and Source Build**:
   Verify `tar` is held with `apt-mark hold tar`.
   Verify `/usr/local/bin/log-auditor.sh` is executable by root.""",
        "lfcs_setup": """sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: script exists and works
if [ -x /usr/local/bin/log-auditor.sh ]; then
  sudo /usr/local/bin/log-auditor.sh
  if [ -f /var/log/audit/summary.log ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/log-auditor.sh executed and generated summary.log.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/log/audit/summary.log not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/log-auditor.sh missing or not executable.${NC}"
fi

# Task 2: cron.d file
if [ -f /etc/cron.d/log-audit ] && grep -qiE "\*/30\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/log-audit; then
  echo -e "${GREEN}[PASS] Task 2: /etc/cron.d/log-audit cron schedule verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/cron.d/log-audit missing or invalid schedule.${NC}"
fi

# Task 3: package hold
if apt-mark showhold | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 3: Package tar is held.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Package tar is not held.${NC}"
fi""",
        "lfcs_solution": """1. Script `/usr/local/bin/log-auditor.sh`:
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
`sudo apt-mark hold tar`""",
        "lfcs_reset": """sudo rm -rf /usr/local/bin/log-auditor.sh /var/log/audit /etc/cron.d/log-audit
sudo apt-mark unhold tar 2>/dev/null || true""",
    },
]
