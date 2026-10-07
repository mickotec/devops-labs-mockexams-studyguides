# [LFCS W1D3-LFCS] Standard Linux File Permissions

**Date:** 2026-09-16  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Groups and Users
Ensure the following group and users exist:
1. Group: `devops_eng` (system assigned GID)
2. User `alice` belonging to primary group `devops_eng`.
3. User `bob` belonging to primary group `devops_eng`.

### Task 2: Selective Permission Enforcement
In directory `/srv/data/engineering`:
1. Change group ownership of `/srv/data/engineering` and all its contents recursively to `devops_eng`.
2. Enforce standard permissions:
   - All files must have permissions `664` (`-rw-rw-r--`).
   - All directories must have permissions `775` (`drwxrwxr-x`).

### Task 3: Enforce Default DevOps Umask
Create an environment script `/etc/profile.d/devops_umask.sh`:
- When users belonging to group `devops_eng` log in, set their default umask to `002`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d3-lfcs
```
