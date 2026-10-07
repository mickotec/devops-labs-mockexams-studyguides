# [LFCS W8D2-LFCS] Timed Mock Exam 1 (Strict Exam Conditions)

**Date:** 2026-11-17  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: User & Group Administration
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
3. Enable and start the service, verifying `/var/log/heartbeat.log` contains an entry.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d2-lfcs
```
