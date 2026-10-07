# [LFCS W6D1-LFCS] Storage Partitions (MBR vs GPT) & Swap

**Date:** 2026-11-02  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Dedicated Swap File Creation
1. Create a `128MB` swap file at `/var/tmp/swapfile_extra` (use `dd` or `fallocate`).
2. Set permissions strictly to `0600` (`chmod 600`).
3. Format it as swap space with `mkswap`.

### Task 2: Swap Space Activation & Persistence
1. Activate the swap file with `swapon /var/tmp/swapfile_extra`.
2. Append a persistent entry to `/etc/fstab` so it activates on boot:
   `/var/tmp/swapfile_extra none swap sw 0 0`
3. Verify that `swapon --show` displays `/var/tmp/swapfile_extra`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d1-lfcs
```
