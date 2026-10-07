# [LFCS W5D1-LFCS] Local User Management & /etc/passwd

**Date:** 2026-10-26  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Dedicated User
Create a user named `devops_user`:
- UID: `1600`
- Primary group: `devops_user`
- Shell: `/bin/bash`
- Home directory: `/home/devops_user`
- Comment: `DevOps Service Account`

### Task 2: Account Password Aging & Expiry
Using `chage`:
- Set account expiration date to `2027-12-31`.
- Set maximum password age to `90` days.
- Set password warning to `7` days.

### Task 3: Account Locking
Lock the user account `test_lock_user` using `passwd -l` so login is disabled.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d1-lfcs
```
