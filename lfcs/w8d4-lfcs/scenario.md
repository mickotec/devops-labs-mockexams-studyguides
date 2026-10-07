# [LFCS W8D4-LFCS] Timed Mock Exam 3 (Strict Exam Conditions)

**Date:** 2026-11-19  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Access Control Lists (ACLs)
1. Create directory `/var/mock3_shared`.
2. Using `setfacl`, grant user `student` read, write, and execute permissions (`rwx`) on `/var/mock3_shared`.
3. Set the same default ACL permissions on `/var/mock3_shared` for user `student` (`-d -m u:student:rwx`).

### Task 2: SUID Binary Audit
1. Search `/usr/bin` for all regular files having the SUID permission bit set (`-perm -4000`).
2. Sort the list of absolute paths alphabetically and save it to `/var/tmp/suid_binaries.txt`.

### Task 3: Persistent Kernel Module
1. Load the `dummy` network kernel module using `modprobe dummy`.
2. Configure `/etc/modules-load.d/dummy.conf` so that `dummy` is loaded automatically at boot.

### Task 4: Firewall Egress Restriction
1. Using iptables, add a rule to the `OUTPUT` chain to drop all outbound TCP traffic to IP `198.51.100.1` on port `443`:
   `sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d4-lfcs
```
