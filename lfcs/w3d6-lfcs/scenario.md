# [LFCS W3D6-LFCS] Week 3 Systemd & Process Orchestration

**Date:** 2026-10-17  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 3)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 3 Triathlon Tasks:
1. **Automated Cleaning Service & Timer**:
   Create a systemd service `/etc/systemd/system/cache-cleaner.service` that removes files older than 7 days from `/var/tmp/cache` (`find /var/tmp/cache -type f -mtime +7 -delete`).
   Create a companion timer `/etc/systemd/system/cache-cleaner.timer` scheduled to trigger every hour (`OnCalendar=hourly`, `Persistent=true`).
   Enable and start `cache-cleaner.timer`.

2. **Fix Broken Systemd Service**:
   A service `payment-bridge.service` has a faulty unit file (`ExecStart` binary points to `/nonexistent/bridge`).
   Fix it to point to `/usr/local/bin/payment-bridge.sh`.
   Reload systemd and start the service so it is `active (running)`.

3. **Process Priority & Limit Hardening**:
   Configure `/etc/security/limits.d/50-worker.conf` to set a hard limit of `4096` open files (`nofile`) and max processes (`nproc`) of `2048` for user `student`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d6-lfcs
```
