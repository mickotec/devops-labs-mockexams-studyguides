# [LFCS W5D6-LFCS] Security Audit, User Quarantine & Recovery

**Date:** 2026-10-31  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 5)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 5 Triathlon Tasks:
1. **Quarantine Compromised User Account**:
   A compromised user account `hacked_service` exists on the system.
   - Lock the password using `passwd -l`.
   - Change the login shell to `/usr/sbin/nologin` or `/bin/false`.
   - Expire the account immediately with `chage -E 0 hacked_service`.

2. **Sudoers Audit & Drop-In Hardening**:
   Ensure `/etc/sudoers.d/99-quarantine` allows user `student` full sudo with `NOPASSWD: ALL` and contains no insecure wildcard directives for quarantined users.

3. **Sysctl Kernel Protection**:
   Ensure `/etc/sysctl.d/99-security.conf` enforces `net.ipv4.tcp_syncookies = 1` and `net.ipv4.conf.all.rp_filter = 1`. Apply with `sysctl -p`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d6-lfcs
```
