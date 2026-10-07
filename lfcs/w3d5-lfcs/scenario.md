# [LFCS W3D5-LFCS] System Integrity, Resource Monitoring & Top

**Date:** 2026-10-16  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Hardware & Memory Profiling
Create an automated hardware summary at `/var/tmp/system_specs.txt`:
1. Total installed RAM in Megabytes (extracted from `/proc/meminfo` or `free -m`).
2. Number of CPU cores (from `/proc/cpuinfo` or `lscpu`).
3. Current system load average over 1, 5, 15 minutes (from `/proc/loadavg` or `uptime`).

### Task 2: VM Swappiness Tuning
Check the current `vm.swappiness` value and permanently tune it:
1. Append `vm.swappiness = 15` to `/etc/sysctl.d/99-swappiness.conf`.
2. Apply the change immediately with `sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d5-lfcs
```
