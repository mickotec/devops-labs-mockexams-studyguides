# [LFCS W1D4-LFCS] Special Permissions: SUID, SGID & Sticky Bit

**Date:** 2026-09-17  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Collaborative Shared Directory with SGID
1. Create a group named `marketing`.
2. Create directory `/opt/campaigns`.
3. Set ownership of `/opt/campaigns` to user `root` and group `marketing`.
4. Enforce permissions such that:
   - Group members have full read, write, and execute permissions (`rwx`).
   - Others have zero permissions (`---`).
   - Any new file or directory created inside automatically inherits the group `marketing` (SetGID bit).

### Task 2: Secure Public Drop Directory with Sticky Bit
1. Inside `/opt/campaigns`, create a directory `incoming`.
2. Configure permissions on `/opt/campaigns/incoming` with the Sticky bit (`1777` or `1770`):
   - Only the file owner or root can delete or rename files inside `incoming`.

### Task 3: World-Writable File Security Audit
1. Search `/var/log` for any world-writable files (`-perm -002`).
2. Save the list of matched paths to `/var/tmp/world_writable_audit.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d4-lfcs
```
