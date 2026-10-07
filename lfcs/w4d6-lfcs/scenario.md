# [LFCS W4D6-LFCS] Week 4 System Automation & Maintenance Triathlon

**Date:** 2026-10-24  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 4)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 4 Triathlon Tasks:
1. **Automated Audit Pipeline**:
   Create `/usr/local/bin/log-auditor.sh`:
   - Extracts all journal entries with priority `err` from the last 2 hours.
   - Saves them to `/var/log/audit/recent_errors.log` (create directory if missing).
   - Counts the error lines and appends `[$(date)] Found <count> errors` to `/var/log/audit/summary.log`.

2. **Crontab Automation**:
   Add a root crontab entry in `/etc/cron.d/log-audit` running `/usr/local/bin/log-auditor.sh` every 30 minutes (`*/30 * * * * root /usr/local/bin/log-auditor.sh`).

3. **Package Hold and Source Build**:
   Verify `tar` is held with `apt-mark hold tar`.
   Verify `/usr/local/bin/log-auditor.sh` is executable by root.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d6-lfcs
```
