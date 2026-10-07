# [LFCS W2D1-LFCS] File Searching with Find and Locate

**Date:** 2026-10-05  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Find Large Files
Search the `/var/log` directory for all files strictly larger than `500KB` (`+500k`). Save the list of full paths to `/var/tmp/large_logs.txt`.

### Task 2: Find by Modification Time and Permissions
Find all files in `/etc` that were modified within the last `7 days` (`-mtime -7`) and have permissions `644`. Output their paths to `/var/tmp/recent_configs.txt`.

### Task 3: Locate Database Indexing
Update the `mlocate` / `plocate` database (`sudo updatedb`) and use `locate` to find all configuration files ending in `.conf` located inside `/etc/systemd`. Save the results to `/var/tmp/systemd_confs.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d1-lfcs
```
