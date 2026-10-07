# [LFCS W7D3-LFCS] Packet Filtering with Firewalld & Iptables

**Date:** 2026-11-11  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Block Port with Iptables
1. Append a rule to the `INPUT` chain that drops all incoming TCP packets destined for port `8088`:
   `sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

### Task 2: Allow Subnet ICMP Traffic
1. Insert a rule at position 1 in the `INPUT` chain that explicitly allows incoming ICMP echo-requests (ping) originating from `192.168.0.0/16`:
   `sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

### Task 3: Backup Active Iptables Rules
1. Export the active IPv4 iptables ruleset to `/var/tmp/iptables_backup.rules` using `iptables-save`:
   `sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d3-lfcs
```
