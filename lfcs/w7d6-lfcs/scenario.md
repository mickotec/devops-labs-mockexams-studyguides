# [LFCS W7D6-LFCS] Week 7 Linux Networking & Firewall Marathon

**Date:** 2026-11-14  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Bridge Network Construction
1. Create a software bridge interface `br-marathon` with IP `172.25.1.1/24` and bring it UP:
   `sudo ip link add br-marathon type bridge`
   `sudo ip addr add 172.25.1.1/24 dev br-marathon`
   `sudo ip link set br-marathon up`

### Task 2: Virtual Interface Attachment
1. Create a veth pair `veth-m1` and `veth-m2`.
2. Attach `veth-m1` to `br-marathon` as a slave port.
3. Bring both `veth-m1` and `veth-m2` interfaces UP.

### Task 3: Firewall Filtering & NAT Redirection
1. Redirect incoming TCP traffic on port `9090` to local port `80` using iptables NAT table PREROUTING chain:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
2. Drop all incoming UDP traffic on port `5353` in the INPUT chain:
   `sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

### Task 4: Network Health Check Script
1. Create an executable script `/usr/local/bin/network_health.sh`.
2. If `br-marathon` is in state UP, write `STATUS=HEALTHY` to `/var/log/net_marathon.status`.
3. Execute the script once to confirm.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d6-lfcs
```
