# [LFCS W2D2-LFCS] Text Processing: Grep & Regular Expressions

**Date:** 2026-10-06  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Extract IPv4 Addresses
From `/var/tmp/auth_sample.log`, extract all distinct IPv4 addresses that attempted connection. Save them sorted uniquely to `/var/tmp/auth_ips.txt`.

### Task 2: Case-Insensitive Pattern Filtering
In `/etc/security/`, find all configuration lines that contain `pam` or `login` ignoring case, excluding commented lines starting with `#`. Save to `/var/tmp/pam_rules.txt`.

### Task 3: Log Error Frequency Count
In `/var/tmp/auth_sample.log`, count how many lines contain `Failed password` or `authentication failure`. Output the integer count to `/var/tmp/error_count.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d2-lfcs
```
