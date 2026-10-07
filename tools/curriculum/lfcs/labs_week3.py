"""
Dedicated LFCS Lab Definitions for Week 3 (Days 1 to 6).
"""

WEEK_3_LABS = [
    {
        "day": 1,
        "date": '2026-10-12',
        "title": 'Linux Boot Architecture & GRUB2',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: GRUB Configuration Tuning
1. In `/etc/default/grub`, modify `GRUB_CMDLINE_LINUX_DEFAULT` to append the kernel boot parameter `consoleblank=600`.
2. Change the default boot timeout (`GRUB_TIMEOUT`) to `8` seconds.
3. Run `sudo update-grub` to regenerate `/boot/grub/grub.cfg`.

### Task 2: System Boot Diagnostic Report
Extract boot diagnostics to `/var/tmp/boot_diagnostic.txt`:
1. Use `dmesg` or `journalctl -b` to find the kernel command-line arguments used during current boot and save the line containing `Command line:` or `Kernel command line:` as the first line of `/var/tmp/boot_diagnostic.txt`.
2. Append the UUID of the root filesystem mounted at `/` (use `findmnt` or `lsblk`).""",
        "setup": """sudo rm -f /var/tmp/boot_diagnostic.txt
if [ ! -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub /etc/default/grub.bak
fi""",
        "verify": """SCORE=0; TOTAL=2
# Check Task 1: GRUB configuration and generated grub.cfg
GRUB_PARAM=$(grep 'consoleblank=600' /etc/default/grub 2>/dev/null || true)
GRUB_TIME=$(grep 'GRUB_TIMEOUT=8' /etc/default/grub 2>/dev/null || true)
GRUB_CFG=$(sudo grep 'consoleblank=600' /boot/grub/grub.cfg 2>/dev/null || true)

if [ -n "$GRUB_PARAM" ] && [ -n "$GRUB_TIME" ] && [ -n "$GRUB_CFG" ]; then
  echo -e "${GREEN}[PASS] Task 1: GRUB default params and regenerated grub.cfg verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GRUB config missing consoleblank=600, TIMEOUT=8, or update-grub not executed.${NC}"
fi

# Check Task 2: boot diagnostic report
if [ -f /var/tmp/boot_diagnostic.txt ] && grep -qiE "BOOT_IMAGE|vmlinuz|Command line" /var/tmp/boot_diagnostic.txt && grep -qiE "UUID=" /var/tmp/boot_diagnostic.txt; then
  echo -e "${GREEN}[PASS] Task 2: Boot diagnostic report verified with kernel cmdline and root UUID.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/boot_diagnostic.txt missing or incomplete.${NC}"
fi""",
        "solution": """1. Edit `/etc/default/grub`:
Set `GRUB_TIMEOUT=8`
Update `GRUB_CMDLINE_LINUX_DEFAULT="... consoleblank=600"`
Run: `sudo update-grub`

2. Generate report:
`journalctl -b -k | grep -m1 -E "Command line|BOOT_IMAGE" > /var/tmp/boot_diagnostic.txt`
`findmnt / -no UUID | awk '{print "UUID="$1}' >> /var/tmp/boot_diagnostic.txt`""",
        "reset": """if [ -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub.bak /etc/default/grub
  sudo update-grub
fi
sudo rm -f /var/tmp/boot_diagnostic.txt""",
        "lfcs_title": 'Linux Boot Architecture & GRUB2',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: GRUB Configuration Tuning
1. In `/etc/default/grub`, modify `GRUB_CMDLINE_LINUX_DEFAULT` to append the kernel boot parameter `consoleblank=600`.
2. Change the default boot timeout (`GRUB_TIMEOUT`) to `8` seconds.
3. Run `sudo update-grub` to regenerate `/boot/grub/grub.cfg`.

### Task 2: System Boot Diagnostic Report
Extract boot diagnostics to `/var/tmp/boot_diagnostic.txt`:
1. Use `dmesg` or `journalctl -b` to find the kernel command-line arguments used during current boot and save the line containing `Command line:` or `Kernel command line:` as the first line of `/var/tmp/boot_diagnostic.txt`.
2. Append the UUID of the root filesystem mounted at `/` (use `findmnt` or `lsblk`).""",
        "lfcs_setup": """sudo rm -f /var/tmp/boot_diagnostic.txt
if [ ! -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub /etc/default/grub.bak
fi""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Check Task 1: GRUB configuration and generated grub.cfg
GRUB_PARAM=$(grep 'consoleblank=600' /etc/default/grub 2>/dev/null || true)
GRUB_TIME=$(grep 'GRUB_TIMEOUT=8' /etc/default/grub 2>/dev/null || true)
GRUB_CFG=$(sudo grep 'consoleblank=600' /boot/grub/grub.cfg 2>/dev/null || true)

if [ -n "$GRUB_PARAM" ] && [ -n "$GRUB_TIME" ] && [ -n "$GRUB_CFG" ]; then
  echo -e "${GREEN}[PASS] Task 1: GRUB default params and regenerated grub.cfg verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GRUB config missing consoleblank=600, TIMEOUT=8, or update-grub not executed.${NC}"
fi

# Check Task 2: boot diagnostic report
if [ -f /var/tmp/boot_diagnostic.txt ] && grep -qiE "BOOT_IMAGE|vmlinuz|Command line" /var/tmp/boot_diagnostic.txt && grep -qiE "UUID=" /var/tmp/boot_diagnostic.txt; then
  echo -e "${GREEN}[PASS] Task 2: Boot diagnostic report verified with kernel cmdline and root UUID.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/boot_diagnostic.txt missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Edit `/etc/default/grub`:
Set `GRUB_TIMEOUT=8`
Update `GRUB_CMDLINE_LINUX_DEFAULT="... consoleblank=600"`
Run: `sudo update-grub`

2. Generate report:
`journalctl -b -k | grep -m1 -E "Command line|BOOT_IMAGE" > /var/tmp/boot_diagnostic.txt`
`findmnt / -no UUID | awk '{print "UUID="$1}' >> /var/tmp/boot_diagnostic.txt`""",
        "lfcs_reset": """if [ -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub.bak /etc/default/grub
  sudo update-grub
fi
sudo rm -f /var/tmp/boot_diagnostic.txt""",
    },
    {
        "day": 2,
        "date": '2026-10-13',
        "title": 'Systemd Targets & Runlevel Management',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Inspect and Set Default Target
1. Verify the current default systemd target.
2. Set the default system target to `multi-user.target` using `systemctl set-default`.

### Task 2: Create Custom Target
Create a custom systemd target unit file at `/etc/systemd/system/maintenance.target`:
- Description: `Maintenance Mode Target`
- Requires: `multi-user.target`
- Reload systemd manager configuration (`systemctl daemon-reload`).

### Task 3: Target Isolation Verification
Verify that `multi-user.target` is the active default target and record output of `systemctl get-default` into `/var/tmp/default_target.txt`.""",
        "setup": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: default target is multi-user.target
DEF_TARGET=$(systemctl get-default 2>/dev/null || true)
if [ "$DEF_TARGET" == "multi-user.target" ]; then
  echo -e "${GREEN}[PASS] Task 1: Default target is multi-user.target.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Default target is '$DEF_TARGET' (expected multi-user.target).${NC}"
fi

# Task 2: maintenance.target unit file
if [ -f /etc/systemd/system/maintenance.target ] && grep -qi "Maintenance Mode" /etc/systemd/system/maintenance.target; then
  echo -e "${GREEN}[PASS] Task 2: /etc/systemd/system/maintenance.target created and validated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: maintenance.target missing or invalid description.${NC}"
fi

# Task 3: /var/tmp/default_target.txt
if [ -f /var/tmp/default_target.txt ] && grep -q "multi-user.target" /var/tmp/default_target.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/default_target.txt recorded accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/default_target.txt missing or empty.${NC}"
fi""",
        "solution": """1. Set default target:
`sudo systemctl set-default multi-user.target`

2. Create `/etc/systemd/system/maintenance.target`:
```ini
[Unit]
Description=Maintenance Mode Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes
```
`sudo systemctl daemon-reload`

3. Save status:
`systemctl get-default > /var/tmp/default_target.txt`""",
        "reset": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload""",
        "lfcs_title": 'Systemd Targets & Runlevel Management',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Inspect and Set Default Target
1. Verify the current default systemd target.
2. Set the default system target to `multi-user.target` using `systemctl set-default`.

### Task 2: Create Custom Target
Create a custom systemd target unit file at `/etc/systemd/system/maintenance.target`:
- Description: `Maintenance Mode Target`
- Requires: `multi-user.target`
- Reload systemd manager configuration (`systemctl daemon-reload`).

### Task 3: Target Isolation Verification
Verify that `multi-user.target` is the active default target and record output of `systemctl get-default` into `/var/tmp/default_target.txt`.""",
        "lfcs_setup": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: default target is multi-user.target
DEF_TARGET=$(systemctl get-default 2>/dev/null || true)
if [ "$DEF_TARGET" == "multi-user.target" ]; then
  echo -e "${GREEN}[PASS] Task 1: Default target is multi-user.target.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Default target is '$DEF_TARGET' (expected multi-user.target).${NC}"
fi

# Task 2: maintenance.target unit file
if [ -f /etc/systemd/system/maintenance.target ] && grep -qi "Maintenance Mode" /etc/systemd/system/maintenance.target; then
  echo -e "${GREEN}[PASS] Task 2: /etc/systemd/system/maintenance.target created and validated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: maintenance.target missing or invalid description.${NC}"
fi

# Task 3: /var/tmp/default_target.txt
if [ -f /var/tmp/default_target.txt ] && grep -q "multi-user.target" /var/tmp/default_target.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/default_target.txt recorded accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/default_target.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Set default target:
`sudo systemctl set-default multi-user.target`

2. Create `/etc/systemd/system/maintenance.target`:
```ini
[Unit]
Description=Maintenance Mode Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes
```
`sudo systemctl daemon-reload`

3. Save status:
`systemctl get-default > /var/tmp/default_target.txt`""",
        "lfcs_reset": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload""",
    },
    {
        "day": 3,
        "date": '2026-10-14',
        "title": 'Creating & Managing Systemd Services',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Worker Script
Create a background script at `/usr/local/bin/worker-daemon.sh`:
- Make it executable (`chmod 755`).
- Contents: An infinite loop that writes `Worker ping: $(date)` to `/var/log/worker-daemon.log` every 3 seconds.

### Task 2: Create Systemd Service Unit
Create `/etc/systemd/system/worker-daemon.service`:
- `Description=Worker Daemon Service`
- `ExecStart=/usr/local/bin/worker-daemon.sh`
- `Restart=always`
- `[Install]` section with `WantedBy=multi-user.target`

### Task 3: Service Activation
1. Reload systemd (`systemctl daemon-reload`).
2. Enable and start `worker-daemon.service`.
3. Verify the service is active and the log file `/var/log/worker-daemon.log` is receiving entries.""",
        "setup": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: script exists and executable
if [ -x /usr/local/bin/worker-daemon.sh ]; then
  echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/worker-daemon.sh executable verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/worker-daemon.sh missing or not executable.${NC}"
fi

# Task 2: service file
if [ -f /etc/systemd/system/worker-daemon.service ] && grep -qi "Restart=always" /etc/systemd/system/worker-daemon.service; then
  echo -e "${GREEN}[PASS] Task 2: worker-daemon.service unit file configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Service unit file missing or Restart directive absent.${NC}"
fi

# Task 3: service is running and logging
IS_ACTIVE=$(systemctl is-active worker-daemon.service 2>/dev/null || echo "inactive")
if [ "$IS_ACTIVE" == "active" ] && [ -f /var/log/worker-daemon.log ] && [ -s /var/log/worker-daemon.log ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-daemon.service is active and writing to /var/log/worker-daemon.log.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Service is $IS_ACTIVE or /var/log/worker-daemon.log empty.${NC}"
fi""",
        "solution": """1. Create script `/usr/local/bin/worker-daemon.sh`:
```bash
#!/usr/bin/env bash
while true; do
  echo "Worker ping: $(date)" >> /var/log/worker-daemon.log
  sleep 3
done
```
`sudo chmod 755 /usr/local/bin/worker-daemon.sh`

2. Create `/etc/systemd/system/worker-daemon.service`:
```ini
[Unit]
Description=Worker Daemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/worker-daemon.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
`sudo systemctl daemon-reload`
`sudo systemctl enable --now worker-daemon.service`""",
        "reset": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload""",
        "lfcs_title": 'Creating & Managing Systemd Services',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Create Worker Script
Create a background script at `/usr/local/bin/worker-daemon.sh`:
- Make it executable (`chmod 755`).
- Contents: An infinite loop that writes `Worker ping: $(date)` to `/var/log/worker-daemon.log` every 3 seconds.

### Task 2: Create Systemd Service Unit
Create `/etc/systemd/system/worker-daemon.service`:
- `Description=Worker Daemon Service`
- `ExecStart=/usr/local/bin/worker-daemon.sh`
- `Restart=always`
- `[Install]` section with `WantedBy=multi-user.target`

### Task 3: Service Activation
1. Reload systemd (`systemctl daemon-reload`).
2. Enable and start `worker-daemon.service`.
3. Verify the service is active and the log file `/var/log/worker-daemon.log` is receiving entries.""",
        "lfcs_setup": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: script exists and executable
if [ -x /usr/local/bin/worker-daemon.sh ]; then
  echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/worker-daemon.sh executable verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/worker-daemon.sh missing or not executable.${NC}"
fi

# Task 2: service file
if [ -f /etc/systemd/system/worker-daemon.service ] && grep -qi "Restart=always" /etc/systemd/system/worker-daemon.service; then
  echo -e "${GREEN}[PASS] Task 2: worker-daemon.service unit file configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Service unit file missing or Restart directive absent.${NC}"
fi

# Task 3: service is running and logging
IS_ACTIVE=$(systemctl is-active worker-daemon.service 2>/dev/null || echo "inactive")
if [ "$IS_ACTIVE" == "active" ] && [ -f /var/log/worker-daemon.log ] && [ -s /var/log/worker-daemon.log ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-daemon.service is active and writing to /var/log/worker-daemon.log.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Service is $IS_ACTIVE or /var/log/worker-daemon.log empty.${NC}"
fi""",
        "lfcs_solution": """1. Create script `/usr/local/bin/worker-daemon.sh`:
```bash
#!/usr/bin/env bash
while true; do
  echo "Worker ping: $(date)" >> /var/log/worker-daemon.log
  sleep 3
done
```
`sudo chmod 755 /usr/local/bin/worker-daemon.sh`

2. Create `/etc/systemd/system/worker-daemon.service`:
```ini
[Unit]
Description=Worker Daemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/worker-daemon.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
`sudo systemctl daemon-reload`
`sudo systemctl enable --now worker-daemon.service`""",
        "lfcs_reset": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload""",
    },
    {
        "day": 4,
        "date": '2026-10-15',
        "title": 'Process Diagnostics & Signal Management',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Rogue Process Termination
A rogue process simulating a memory leak (`rogue-sim`) is running in the background.
1. Locate its PID using `pgrep` or `ps`.
2. Terminate it gracefully with `SIGTERM` (15); if it remains, force terminate with `SIGKILL` (9).

### Task 2: Nice Priority Adjustment
A background workload process `batch-calc` is running.
- Use `renice` to lower its scheduling priority to nice value `+12`.

### Task 3: Resource Inventory
Generate `/var/tmp/process_report.txt` containing:
- The top 5 memory-consuming processes formatted with headers: `PID,USER,%MEM,COMMAND`.""",
        "setup": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
# Start rogue process
nohup bash -c 'exec -a rogue-sim sleep 3600' >/dev/null 2>&1 &
# Start batch calc
nohup bash -c 'exec -a batch-calc sleep 3600' >/dev/null 2>&1 &
sudo rm -f /var/tmp/process_report.txt""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: rogue-sim killed
if ! pgrep -f "rogue-sim" >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: Rogue process rogue-sim has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: rogue-sim process is still running.${NC}"
fi

# Task 2: batch-calc reniced to 12
NI=$(ps -eo ni,cmd | grep "batch-calc" | grep -v grep | awk '{print $1}' | head -1 || echo "0")
if [ "$NI" == "12" ]; then
  echo -e "${GREEN}[PASS] Task 2: batch-calc has nice priority 12.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: batch-calc nice value is '$NI' (expected 12).${NC}"
fi

# Task 3: process_report.txt exists with at least 5 entries
if [ -f /var/tmp/process_report.txt ] && [ $(wc -l < /var/tmp/process_report.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/process_report.txt created with memory stats.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/process_report.txt missing or has fewer than 5 lines.${NC}"
fi""",
        "solution": """1. Kill rogue process:
`killall -15 rogue-sim || killall -9 rogue-sim`

2. Renice batch-calc:
`renice -n 12 -p $(pgrep -f batch-calc)`

3. Top 5 memory processes:
`ps -eo pid,user,%mem,command --sort=-%mem | head -n 6 > /var/tmp/process_report.txt`""",
        "reset": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
sudo rm -f /var/tmp/process_report.txt""",
        "lfcs_title": 'Process Diagnostics & Signal Management',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Rogue Process Termination
A rogue process simulating a memory leak (`rogue-sim`) is running in the background.
1. Locate its PID using `pgrep` or `ps`.
2. Terminate it gracefully with `SIGTERM` (15); if it remains, force terminate with `SIGKILL` (9).

### Task 2: Nice Priority Adjustment
A background workload process `batch-calc` is running.
- Use `renice` to lower its scheduling priority to nice value `+12`.

### Task 3: Resource Inventory
Generate `/var/tmp/process_report.txt` containing:
- The top 5 memory-consuming processes formatted with headers: `PID,USER,%MEM,COMMAND`.""",
        "lfcs_setup": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
# Start rogue process
nohup bash -c 'exec -a rogue-sim sleep 3600' >/dev/null 2>&1 &
# Start batch calc
nohup bash -c 'exec -a batch-calc sleep 3600' >/dev/null 2>&1 &
sudo rm -f /var/tmp/process_report.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: rogue-sim killed
if ! pgrep -f "rogue-sim" >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: Rogue process rogue-sim has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: rogue-sim process is still running.${NC}"
fi

# Task 2: batch-calc reniced to 12
NI=$(ps -eo ni,cmd | grep "batch-calc" | grep -v grep | awk '{print $1}' | head -1 || echo "0")
if [ "$NI" == "12" ]; then
  echo -e "${GREEN}[PASS] Task 2: batch-calc has nice priority 12.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: batch-calc nice value is '$NI' (expected 12).${NC}"
fi

# Task 3: process_report.txt exists with at least 5 entries
if [ -f /var/tmp/process_report.txt ] && [ $(wc -l < /var/tmp/process_report.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/process_report.txt created with memory stats.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/process_report.txt missing or has fewer than 5 lines.${NC}"
fi""",
        "lfcs_solution": """1. Kill rogue process:
`killall -15 rogue-sim || killall -9 rogue-sim`

2. Renice batch-calc:
`renice -n 12 -p $(pgrep -f batch-calc)`

3. Top 5 memory processes:
`ps -eo pid,user,%mem,command --sort=-%mem | head -n 6 > /var/tmp/process_report.txt`""",
        "lfcs_reset": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
sudo rm -f /var/tmp/process_report.txt""",
    },
    {
        "day": 5,
        "date": '2026-10-16',
        "title": 'System Integrity, Resource Monitoring & Top',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Hardware & Memory Profiling
Create an automated hardware summary at `/var/tmp/system_specs.txt`:
1. Total installed RAM in Megabytes (extracted from `/proc/meminfo` or `free -m`).
2. Number of CPU cores (from `/proc/cpuinfo` or `lscpu`).
3. Current system load average over 1, 5, 15 minutes (from `/proc/loadavg` or `uptime`).

### Task 2: VM Swappiness Tuning
Check the current `vm.swappiness` value and permanently tune it:
1. Append `vm.swappiness = 15` to `/etc/sysctl.d/99-swappiness.conf`.
2. Apply the change immediately with `sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`.""",
        "setup": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: system_specs.txt
if [ -f /var/tmp/system_specs.txt ] && grep -qiE "RAM|Memory" /var/tmp/system_specs.txt && grep -qiE "CPU|Cores" /var/tmp/system_specs.txt && grep -qiE "Load" /var/tmp/system_specs.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_specs.txt contains RAM, CPU, and Load metrics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_specs.txt missing or incomplete metrics.${NC}"
fi

# Task 2: swappiness runtime and persistent
CURR_SWAP=$(sysctl -n vm.swappiness)
CONF_SWAP=$(grep -oE "vm.swappiness\s*=\s*15" /etc/sysctl.d/99-swappiness.conf 2>/dev/null || true)
if [ "$CURR_SWAP" == "15" ] && [ -n "$CONF_SWAP" ]; then
  echo -e "${GREEN}[PASS] Task 2: vm.swappiness=15 active and configured persistently in sysctl.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Runtime swappiness is $CURR_SWAP (expected 15) or config file missing.${NC}"
fi""",
        "solution": """1. Hardware report:
```bash
MEM=$(free -m | awk '/Mem:/ {print "RAM: "$2"MB"}')
CPU=$(lscpu | awk -F: '/CPU\(s\):/ {print "CPU Cores: "$2}' | head -1)
LOAD=$(awk '{print "Load Average: "$1", "$2", "$3}' /proc/loadavg)
echo "$MEM" > /var/tmp/system_specs.txt
echo "$CPU" >> /var/tmp/system_specs.txt
echo "$LOAD" >> /var/tmp/system_specs.txt
```

2. Tune swappiness:
`echo "vm.swappiness = 15" | sudo tee /etc/sysctl.d/99-swappiness.conf`
`sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`""",
        "reset": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null""",
        "lfcs_title": 'System Integrity, Resource Monitoring & Top',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Hardware & Memory Profiling
Create an automated hardware summary at `/var/tmp/system_specs.txt`:
1. Total installed RAM in Megabytes (extracted from `/proc/meminfo` or `free -m`).
2. Number of CPU cores (from `/proc/cpuinfo` or `lscpu`).
3. Current system load average over 1, 5, 15 minutes (from `/proc/loadavg` or `uptime`).

### Task 2: VM Swappiness Tuning
Check the current `vm.swappiness` value and permanently tune it:
1. Append `vm.swappiness = 15` to `/etc/sysctl.d/99-swappiness.conf`.
2. Apply the change immediately with `sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: system_specs.txt
if [ -f /var/tmp/system_specs.txt ] && grep -qiE "RAM|Memory" /var/tmp/system_specs.txt && grep -qiE "CPU|Cores" /var/tmp/system_specs.txt && grep -qiE "Load" /var/tmp/system_specs.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_specs.txt contains RAM, CPU, and Load metrics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_specs.txt missing or incomplete metrics.${NC}"
fi

# Task 2: swappiness runtime and persistent
CURR_SWAP=$(sysctl -n vm.swappiness)
CONF_SWAP=$(grep -oE "vm.swappiness\s*=\s*15" /etc/sysctl.d/99-swappiness.conf 2>/dev/null || true)
if [ "$CURR_SWAP" == "15" ] && [ -n "$CONF_SWAP" ]; then
  echo -e "${GREEN}[PASS] Task 2: vm.swappiness=15 active and configured persistently in sysctl.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Runtime swappiness is $CURR_SWAP (expected 15) or config file missing.${NC}"
fi""",
        "lfcs_solution": """1. Hardware report:
```bash
MEM=$(free -m | awk '/Mem:/ {print "RAM: "$2"MB"}')
CPU=$(lscpu | awk -F: '/CPU\(s\):/ {print "CPU Cores: "$2}' | head -1)
LOAD=$(awk '{print "Load Average: "$1", "$2", "$3}' /proc/loadavg)
echo "$MEM" > /var/tmp/system_specs.txt
echo "$CPU" >> /var/tmp/system_specs.txt
echo "$LOAD" >> /var/tmp/system_specs.txt
```

2. Tune swappiness:
`echo "vm.swappiness = 15" | sudo tee /etc/sysctl.d/99-swappiness.conf`
`sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`""",
        "lfcs_reset": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null""",
    },
    {
        "day": 6,
        "date": '2026-10-17',
        "title": 'Week 3 Systemd & Process Orchestration',
        "diff": 'Hard (Milestone Assessment 3)',
        "time": '45m',
        "tasks": """### Milestone 3 Triathlon Tasks:
1. **Automated Cleaning Service & Timer**:
   Create a systemd service `/etc/systemd/system/cache-cleaner.service` that removes files older than 7 days from `/var/tmp/cache` (`find /var/tmp/cache -type f -mtime +7 -delete`).
   Create a companion timer `/etc/systemd/system/cache-cleaner.timer` scheduled to trigger every hour (`OnCalendar=hourly`, `Persistent=true`).
   Enable and start `cache-cleaner.timer`.

2. **Fix Broken Systemd Service**:
   A service `payment-bridge.service` has a faulty unit file (`ExecStart` binary points to `/nonexistent/bridge`).
   Fix it to point to `/usr/local/bin/payment-bridge.sh`.
   Reload systemd and start the service so it is `active (running)`.

3. **Process Priority & Limit Hardening**:
   Configure `/etc/security/limits.d/50-worker.conf` to set a hard limit of `4096` open files (`nofile`) and max processes (`nproc`) of `2048` for user `student`.""",
        "setup": """sudo mkdir -p /var/tmp/cache /usr/local/bin
sudo tee /usr/local/bin/payment-bridge.sh << 'EOF' >/dev/null
#!/usr/bin/env bash
while true; do sleep 3600; done
EOF
sudo chmod 755 /usr/local/bin/payment-bridge.sh

sudo tee /etc/systemd/system/payment-bridge.service << 'EOF' >/dev/null
[Unit]
Description=Payment Bridge Service
After=network.target

[Service]
Type=simple
ExecStart=/nonexistent/bridge
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/security/limits.d/50-worker.conf
sudo systemctl daemon-reload""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: Timer active
TIMER_ACTIVE=$(systemctl is-active cache-cleaner.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: cache-cleaner.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: cache-cleaner.timer is $TIMER_ACTIVE.${NC}"
fi

# Task 2: payment-bridge service fixed and running
SVC_ACTIVE=$(systemctl is-active payment-bridge.service 2>/dev/null || echo "inactive")
if [ "$SVC_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 2: payment-bridge.service is active (running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: payment-bridge.service is $SVC_ACTIVE.${NC}"
fi

# Task 3: limits file
if [ -f /etc/security/limits.d/50-worker.conf ] && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/50-worker.conf && grep -q "student.*hard.*nproc.*2048" /etc/security/limits.d/50-worker.conf; then
  echo -e "${GREEN}[PASS] Task 3: Security limits for student configured correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/50-worker.conf missing or values incorrect.${NC}"
fi""",
        "solution": """1. Cache cleaner timer:
`/etc/systemd/system/cache-cleaner.service`:
```ini
[Unit]
Description=Cache Cleaner
[Service]
Type=oneshot
ExecStart=/usr/bin/find /var/tmp/cache -type f -mtime +7 -delete
```
`/etc/systemd/system/cache-cleaner.timer`:
```ini
[Unit]
Description=Hourly Cache Cleaner Timer
[Timer]
OnCalendar=hourly
Persistent=true
[Install]
WantedBy=timers.target
```
`sudo systemctl daemon-reload && sudo systemctl enable --now cache-cleaner.timer`

2. Fix `/etc/systemd/system/payment-bridge.service`:
Change `ExecStart=/usr/local/bin/payment-bridge.sh`
`sudo systemctl daemon-reload && sudo systemctl restart payment-bridge.service`

3. Create `/etc/security/limits.d/50-worker.conf`:
```
student hard nofile 4096
student hard nproc 2048
```""",
        "reset": """sudo systemctl stop cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo systemctl disable cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/systemd/system/payment-bridge.service /usr/local/bin/payment-bridge.sh /etc/security/limits.d/50-worker.conf
sudo rm -rf /var/tmp/cache
sudo systemctl daemon-reload""",
        "lfcs_title": 'Week 3 Systemd & Process Orchestration',
        "lfcs_diff": 'Hard (Milestone Assessment 3)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 3 Triathlon Tasks:
1. **Automated Cleaning Service & Timer**:
   Create a systemd service `/etc/systemd/system/cache-cleaner.service` that removes files older than 7 days from `/var/tmp/cache` (`find /var/tmp/cache -type f -mtime +7 -delete`).
   Create a companion timer `/etc/systemd/system/cache-cleaner.timer` scheduled to trigger every hour (`OnCalendar=hourly`, `Persistent=true`).
   Enable and start `cache-cleaner.timer`.

2. **Fix Broken Systemd Service**:
   A service `payment-bridge.service` has a faulty unit file (`ExecStart` binary points to `/nonexistent/bridge`).
   Fix it to point to `/usr/local/bin/payment-bridge.sh`.
   Reload systemd and start the service so it is `active (running)`.

3. **Process Priority & Limit Hardening**:
   Configure `/etc/security/limits.d/50-worker.conf` to set a hard limit of `4096` open files (`nofile`) and max processes (`nproc`) of `2048` for user `student`.""",
        "lfcs_setup": """sudo mkdir -p /var/tmp/cache /usr/local/bin
sudo tee /usr/local/bin/payment-bridge.sh << 'EOF' >/dev/null
#!/usr/bin/env bash
while true; do sleep 3600; done
EOF
sudo chmod 755 /usr/local/bin/payment-bridge.sh

sudo tee /etc/systemd/system/payment-bridge.service << 'EOF' >/dev/null
[Unit]
Description=Payment Bridge Service
After=network.target

[Service]
Type=simple
ExecStart=/nonexistent/bridge
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/security/limits.d/50-worker.conf
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Timer active
TIMER_ACTIVE=$(systemctl is-active cache-cleaner.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: cache-cleaner.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: cache-cleaner.timer is $TIMER_ACTIVE.${NC}"
fi

# Task 2: payment-bridge service fixed and running
SVC_ACTIVE=$(systemctl is-active payment-bridge.service 2>/dev/null || echo "inactive")
if [ "$SVC_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 2: payment-bridge.service is active (running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: payment-bridge.service is $SVC_ACTIVE.${NC}"
fi

# Task 3: limits file
if [ -f /etc/security/limits.d/50-worker.conf ] && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/50-worker.conf && grep -q "student.*hard.*nproc.*2048" /etc/security/limits.d/50-worker.conf; then
  echo -e "${GREEN}[PASS] Task 3: Security limits for student configured correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/50-worker.conf missing or values incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Cache cleaner timer:
`/etc/systemd/system/cache-cleaner.service`:
```ini
[Unit]
Description=Cache Cleaner
[Service]
Type=oneshot
ExecStart=/usr/bin/find /var/tmp/cache -type f -mtime +7 -delete
```
`/etc/systemd/system/cache-cleaner.timer`:
```ini
[Unit]
Description=Hourly Cache Cleaner Timer
[Timer]
OnCalendar=hourly
Persistent=true
[Install]
WantedBy=timers.target
```
`sudo systemctl daemon-reload && sudo systemctl enable --now cache-cleaner.timer`

2. Fix `/etc/systemd/system/payment-bridge.service`:
Change `ExecStart=/usr/local/bin/payment-bridge.sh`
`sudo systemctl daemon-reload && sudo systemctl restart payment-bridge.service`

3. Create `/etc/security/limits.d/50-worker.conf`:
```
student hard nofile 4096
student hard nproc 2048
```""",
        "lfcs_reset": """sudo systemctl stop cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo systemctl disable cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/systemd/system/payment-bridge.service /usr/local/bin/payment-bridge.sh /etc/security/limits.d/50-worker.conf
sudo rm -rf /var/tmp/cache
sudo systemctl daemon-reload""",
    },
]
