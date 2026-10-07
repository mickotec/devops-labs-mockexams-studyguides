# [LFCS W7D1-LFCS] Linux Networking Configuration (IP & Routing)

**Date:** 2026-11-09  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Dummy Network Interface
1. Create a dummy network interface named `dummy0` using `ip link`:
   `sudo ip link add dummy0 type dummy`
2. Bring the interface UP:
   `sudo ip link set dummy0 up`

### Task 2: Assign Static IP Address
1. Assign secondary static IP `10.10.20.50/24` to interface `dummy0`:
   `sudo ip addr add 10.10.20.50/24 dev dummy0`

### Task 3: Static Route Configuration
1. Add a static route for destination subnet `10.200.0.0/16` routed via device `dummy0`:
   `sudo ip route add 10.200.0.0/16 dev dummy0`

### Task 4: Network Diagnostic Audit Script
1. Create an executable bash script `/usr/local/bin/network_audit.sh`.
2. The script must write:
   - The default routing line (`ip route show default`)
   - All active nameserver entries from `/etc/resolv.conf` (`grep nameserver /etc/resolv.conf`)
   into `/var/log/network_audit.log`.
3. Set executable permissions on `/usr/local/bin/network_audit.sh` and run it once to initialize the log.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d1-lfcs
```
