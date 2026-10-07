# [LFCS W8D6-LFCS] Certification Gate Review & Readiness Audit

**Date:** 2026-11-21  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Storage & Filesystem Health Audit
1. Execute a command to inspect filesystem type, mount point, and space for `/` (e.g. `df -hT /`).
2. Save the output to `/var/log/storage_audit.log`.

### Task 2: Service Security Audit
1. Check for any failed systemd units on the system using `systemctl --failed --no-legend`.
2. Save the list of failed services (or string `ALL_SERVICES_OPERATIONAL` if none failed) to `/var/log/security_audit.log`.

### Task 3: Automated System Backup Script
1. Create an executable script `/usr/local/bin/system_backup.sh`.
2. The script must package `/etc/systemd` and `/etc/default` into a gzip-compressed tar archive at `/var/backups/etc_backup_audit.tar.gz`.
3. Set executable permissions on `/usr/local/bin/system_backup.sh` and execute it once to create the backup archive.

### Task 4: Student User Security Validation
1. Verify permissions on `/home/student/.ssh`:
   - Directory permissions must be `0700`.
   - File permissions on `/home/student/.ssh/authorized_keys` must be `0600`.
   - Ownership of `/home/student/.ssh` must be `student:student`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d6-lfcs
```
