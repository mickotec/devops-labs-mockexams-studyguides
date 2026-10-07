# [LFCS W5D5-LFCS] Mandatory Access Control: SELinux & AppArmor

**Date:** 2026-10-30  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Audit AppArmor Status
Check the status of AppArmor on Ubuntu:
1. Run `aa-status` to evaluate active profiles.
2. Save the summary of loaded and enforcing profiles to `/var/tmp/apparmor_summary.txt`.

### Task 2: Inspect Profile Directory
List all profiles located in `/etc/apparmor.d/` and output their names to `/var/tmp/apparmor_profiles.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d5-lfcs
```
