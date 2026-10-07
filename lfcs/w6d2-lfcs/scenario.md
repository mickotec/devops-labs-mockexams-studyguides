# [LFCS W6D2-LFCS] Filesystems & Boot Mounting (/etc/fstab)

**Date:** 2026-11-03  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Loop Device Filesystem Formatting
A 150MB loop disk image `/var/tmp/data_store.img` has been initialized and associated with `/dev/loop90`.
- Format `/dev/loop90` with the `ext4` filesystem with filesystem label `DATA_STORE`.

### Task 2: Mount Point & Persistent /etc/fstab Entry
1. Create mount directory `/mnt/data_store`.
2. Extract the filesystem UUID of `/dev/loop90` using `blkid`.
3. Add an `/etc/fstab` entry:
   `UUID=<extracted-uuid> /mnt/data_store ext4 defaults,noatime 0 2`
4. Mount all filesystems with `sudo mount -a`.
5. Verify `/mnt/data_store` is mounted and writable.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d2-lfcs
```
