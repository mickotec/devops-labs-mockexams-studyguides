# [LFCS W5D4-LFCS] Kernel Runtime Tuning with Sysctl

**Date:** 2026-10-29  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Network Parameter Hardening
Configure persistent network parameters in `/etc/sysctl.d/60-hardening.conf`:
- `net.ipv4.ip_forward = 1`
- `net.ipv4.icmp_echo_ignore_broadcasts = 1`

### Task 2: Apply and Verify Parameters
1. Apply the configuration immediately using `sysctl -p /etc/sysctl.d/60-hardening.conf`.
2. Save the active values of `net.ipv4.ip_forward` and `net.ipv4.icmp_echo_ignore_broadcasts` into `/var/tmp/kernel_params.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d4-lfcs
```
