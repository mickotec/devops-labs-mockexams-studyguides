# [LFCS W4D5-LFCS] Bash Automation & Maintenance Scripting

**Date:** 2026-10-23  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Robust Maintenance Script
Create an automated log cleanup and audit script at `/usr/local/bin/daily-maint.sh`:
- Script must be executable (`chmod 755`).
- Ensure `set -euo pipefail` is used.
- Script accepts a target directory as argument `$1`. If `$1` is not provided, exit with code `1` and error message `Usage: daily-maint.sh <dir>`.
- Count all `.log` files in `$1` and append `[$(date)] Processed logs in $1: <count> files` to `/var/log/daily-maint.log`.
- Emit a syslog message with tag `daily-maint`: `Maintenance completed for $1`.

### Task 2: Test Execution
Run `/usr/local/bin/daily-maint.sh /var/log` and verify `/var/log/daily-maint.log` receives the log summary.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d5-lfcs
```
