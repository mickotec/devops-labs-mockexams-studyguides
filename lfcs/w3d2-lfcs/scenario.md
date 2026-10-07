# [LFCS W3D2-LFCS] Systemd Targets & Runlevel Management

**Date:** 2026-10-13  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Inspect and Set Default Target
1. Verify the current default systemd target.
2. Set the default system target to `multi-user.target` using `systemctl set-default`.

### Task 2: Create Custom Target
Create a custom systemd target unit file at `/etc/systemd/system/maintenance.target`:
- Description: `Maintenance Mode Target`
- Requires: `multi-user.target`
- Reload systemd manager configuration (`systemctl daemon-reload`).

### Task 3: Target Isolation Verification
Verify that `multi-user.target` is the active default target and record output of `systemctl get-default` into `/var/tmp/default_target.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d2-lfcs
```
