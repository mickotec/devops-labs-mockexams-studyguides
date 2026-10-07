# [LFCS W1D6-LFCS] Week 1 Consolidation & Permission Security Triathlon

**Date:** 2026-09-19  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 1)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 1 Triathlon Tasks:
1. **Collaborative Secure Tree:**
   Create groups `sysadmins` and `contractors`.
   Create directory `/srv/secure_vault` owned by `root:sysadmins` with permissions `2770` (SGID).
   Inside, create `/srv/secure_vault/incoming` owned by `root:contractors` with permissions `1775` (Sticky bit).
2. **SUID / SGID Audit:**
   Locate all SUID and SGID executables under `/opt/binaries` and save their full paths to `/var/tmp/suid_audit.txt`.
3. **Relative Symbolic Link:**
   In `/srv/secure_vault/configs`, create a relative symlink `current.conf` pointing to `../storage/vault.conf`.
4. **Archive & Backup:**
   Create a gzip-compressed archive `/var/backups/vault_initial.tar.gz` of `/srv/secure_vault` preserving file permissions (`-p`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d6-lfcs
```
