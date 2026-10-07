# [LFCS W1D2-LFCS] Files, Directories, Hard & Soft Links

**Date:** 2026-09-15  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Relative Symbolic Link Migration & Repair
1. The directory `/opt/link-lab/configs` contains a broken symbolic link `active.conf` pointing to a deleted absolute path.
2. The real configuration file has been relocated to `/opt/link-lab/storage/v2/app-v2.conf`.
3. Re-create the symlink `/opt/link-lab/configs/active.conf` pointing to `../storage/v2/app-v2.conf` using a **relative path** (not an absolute path starting with `/`).

### Task 2: Critical Config Hard Linking
1. Create a hard link from `/opt/link-lab/storage/v2/app-v2.conf` to `/opt/link-lab/backup/app-v2.conf.hl`.
2. Append the line `BACKUP_ENABLED=true` to `/opt/link-lab/backup/app-v2.conf.hl`.
3. Verify that the original `/opt/link-lab/storage/v2/app-v2.conf` also displays `BACKUP_ENABLED=true` and shares the exact same inode.

### Task 3: Clean Dangling Symlinks
1. In directory `/opt/link-lab/orphan_links/`, find and remove all broken (dangling) symbolic links.
2. Save the names of the removed links to `/var/tmp/removed_links.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d2-lfcs
```
