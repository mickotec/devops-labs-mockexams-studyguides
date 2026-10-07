# [LFCS W4D1-LFCS] Journald & System Log File Analysis

**Date:** 2026-10-19  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Error-Level Journal Extraction
Query `journalctl` to extract all system log messages with priority `err` or higher (`err`, `crit`, `alert`, `emerg`) recorded since boot (`-b`).
- Output the entries to `/var/tmp/system_errors.log`.

### Task 2: Service Unit Log Extraction
Extract the 20 most recent journal lines for the `ssh` service unit (`-u ssh`).
- Save the output to `/var/tmp/ssh_service.log`.

### Task 3: Journal Disk Space Audit
Check the current disk usage consumed by systemd journal files using `journalctl --disk-usage`.
- Save the exact output line to `/var/tmp/journal_usage.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d1-lfcs
```
