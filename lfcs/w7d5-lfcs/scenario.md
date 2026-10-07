# [LFCS W7D5-LFCS] SSH Hardening, Key Auth & Time Sync

**Date:** 2026-11-13  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Generate & Authorize RSA SSH Key Pair
1. For user `student`, generate a 4096-bit RSA SSH key pair at `/home/student/.ssh/id_admin_rsa` without a passphrase:
   `ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa`
2. Append the public key to `/home/student/.ssh/authorized_keys`.
3. Ensure file permissions are `0600` on `authorized_keys` and `0700` on `~/.ssh`.

### Task 2: SSH Server Configuration Hardening
1. Create a drop-in configuration file `/etc/ssh/sshd_config.d/99-hardening.conf` containing:
   ```
   PermitRootLogin no
   MaxAuthTries 3
   ClientAliveInterval 300
   ClientAliveCountMax 2
   ```
2. Test configuration syntax using `sudo sshd -t`.

### Task 3: Time Synchronization Verification
1. Ensure system NTP synchronization is active using `timedatectl`:
   `sudo timedatectl set-ntp true`
2. Confirm system clock synchronization state using `timedatectl status`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d5-lfcs
```
