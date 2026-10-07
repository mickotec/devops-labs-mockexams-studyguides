# [LFCS W8D5-LFCS] Timed Mock Exam 4 & Final Speed Marathon

**Date:** 2026-11-20  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Custom Systemd Timer
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
2. Validate syntax using `sudo logrotate -d /etc/logrotate.d/mock4_logs`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d5-lfcs
```
