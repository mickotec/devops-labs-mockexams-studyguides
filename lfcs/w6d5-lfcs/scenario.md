# [LFCS W6D5-LFCS] Remote Filesystems: NFS & Storage Monitoring

**Date:** 2026-11-06  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Storage Monitoring Audit Script
Create a monitoring script at `/usr/local/bin/check-disk.sh`:
- Script is executable (`chmod 755`).
- Extract all mounted filesystems with their filesystem type and usage percentage into `/var/tmp/disk_audit.txt` (formatted with headers `Filesystem Type Size Used Avail Use% Mounted_on`).

### Task 2: Disk Alert Threshold
Configure the script so that if any filesystem usage exceeds `85%`, it appends `WARNING: High disk utilization detected` to `/var/log/disk_alert.log`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d5-lfcs
```
