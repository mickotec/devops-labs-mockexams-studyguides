# [LFCS W6D4-LFCS] Dynamic LVM Volume Expansion

**Date:** 2026-11-05  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Extend Logical Volume
A Volume Group `vg_expand` (size 350MB) and mounted Logical Volume `lv_store` (initial size 100MB mounted at `/mnt/expand_store`) are active.
1. Extend `lv_store` by `100MB` (to total size 200MB) using `lvextend`.

### Task 2: Online Filesystem Resize
Resize the `ext4` filesystem online without unmounting using `resize2fs /dev/vg_expand/lv_store`.
- Confirm with `df -h /mnt/expand_store` that the filesystem reflects ~200MB.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d4-lfcs
```
