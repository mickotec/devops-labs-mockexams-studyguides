# [LFCS W5D3-LFCS] Profiles, Template Environments & User Limits

**Date:** 2026-10-28  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Template Environment (/etc/skel)
Place a default welcome document in `/etc/skel/WELCOME.txt`:
- Contents: `Corporate System Policy: All activity is monitored.`
- Ensure default permissions (`644`).

### Task 2: Global Profile Environment Variable
Create `/etc/profile.d/corp_vars.sh`:
- Export `CORPORATE_ENV="production"`
- Make it readable by all users.

### Task 3: Security Limits Configuration
In `/etc/security/limits.d/80-nofile.conf`, set:
- User `student` soft limit for open files (`nofile`) to `2048`.
- User `student` hard limit for open files (`nofile`) to `4096`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d3-lfcs
```
