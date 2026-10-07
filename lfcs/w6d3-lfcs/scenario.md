# [LFCS W6D3-LFCS] Logical Volume Management (LVM) Architecture

**Date:** 2026-11-04  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create LVM Storage Hierarchy
Loop device `/dev/loop91` (250MB) has been prepared.
1. Initialize `/dev/loop91` as an LVM Physical Volume using `pvcreate`.
2. Create a Volume Group named `vg_database` containing `/dev/loop91`.
3. Create a Logical Volume named `lv_orders` with size `120MB` inside `vg_database`.

### Task 2: Format and Mount Logical Volume
1. Format `/dev/vg_database/lv_orders` with the `ext4` filesystem.
2. Mount it at `/mnt/orders_data`.
3. Confirm with `lvs` and `df -h /mnt/orders_data`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d3-lfcs
```
