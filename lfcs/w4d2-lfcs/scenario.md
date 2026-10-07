# [LFCS W4D2-LFCS] Task Scheduling with Cron and At

**Date:** 2026-10-20  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: System-Wide Crontab
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
2. Ensure `/etc/at.deny` does not exist.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d2-lfcs
```
