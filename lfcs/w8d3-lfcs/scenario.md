# [LFCS W8D3-LFCS] Timed Mock Exam 2 (Strict Exam Conditions)

**Date:** 2026-11-18  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Archive & Compression
1. Find all `.conf` files in `/etc` and package them into a gzip-compressed tar archive at `/var/tmp/etc_configs.tar.gz`.

### Task 2: Swap Space Management
1. Create a 128MB swap file at `/swapfile_mock2`.
2. Secure permissions to `0600`.
3. Format as swap using `mkswap` and enable it immediately with `swapon`.

### Task 3: Process Priority (Niceness)
1. Launch a background sleep command with a nice priority of `+10`:
   `nice -n 10 sleep 7200 &`

### Task 4: Package Log Analysis
1. Count the number of lines in `/var/log/dpkg.log` (or `/var/log/dpkg.log.1`) containing the word `status`.
2. Write the exact integer count into `/var/tmp/auth_summary.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d3-lfcs
```
