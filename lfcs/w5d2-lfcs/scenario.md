# [LFCS W5D2-LFCS] Groups, Sudo Privileges & Visudo

**Date:** 2026-10-27  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Group & Assign Membership
1. Create a system group named `sysaudit` with GID `2800`.
2. Add user `student` to group `sysaudit` as a supplementary group.

### Task 2: Configure Passwordless Sudo for Specific Command
Create a sudoers drop-in file `/etc/sudoers.d/90-sysaudit`:
- Members of group `%sysaudit` must be permitted to execute `/usr/bin/journalctl` without password authentication (`NOPASSWD: /usr/bin/journalctl`).
- Validate syntax with `visudo -cf /etc/sudoers.d/90-sysaudit`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d2-lfcs
```
