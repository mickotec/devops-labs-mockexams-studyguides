# [LFCS W7D2-LFCS] Network Bonding & Bridging

**Date:** 2026-11-10  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Linux Software Bridge
1. Create a software bridge interface named `br0` using `ip link`:
   `sudo ip link add br0 type bridge`
2. Assign IP address `192.168.100.1/24` to `br0`.
3. Bring `br0` interface UP.

### Task 2: Create Virtual Ethernet Pair (veth)
1. Create a virtual ethernet pair named `veth-host` and `veth-guest`:
   `sudo ip link add veth-host type veth peer name veth-guest`

### Task 3: Attach Slave Interface to Bridge
1. Attach `veth-host` to bridge `br0` as a master bridge port:
   `sudo ip link set veth-host master br0`
2. Bring `veth-host` and `veth-guest` interfaces UP:
   `sudo ip link set veth-host up`
   `sudo ip link set veth-guest up`

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d2-lfcs
```
