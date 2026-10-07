# [LFCS W6D6-LFCS] Week 6 Storage Mastery & LVM Drill

**Date:** 2026-11-07  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 6)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 6 Triathlon Tasks:
1. **LVM Storage Creation**:
   Loop device `/dev/loop93` (300MB) has been prepared.
   - Create Volume Group `vg_secure`.
   - Create Logical Volume `lv_audit` (120MB).
   - Format with `ext4` and mount at `/mnt/secure_audit`.

2. **Access Control Lists (ACL)**:
   - Use `setfacl` to grant user `student` read, write, and execute permissions (`rwx`) on `/mnt/secure_audit` (`setfacl -m u:student:rwx /mnt/secure_audit`).
   - Confirm with `getfacl /mnt/secure_audit`.

3. **Online Volume Expansion**:
   Extend `lv_audit` by `60MB` and resize filesystem online (`resize2fs`).
   Verify total mounted size >= 170MB.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d6-lfcs
```
