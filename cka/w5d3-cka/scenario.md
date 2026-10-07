# [CKA W5D3-CKA] Cluster Upgrade: Worker Nodes

**Date:** 2026-10-28  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Prepare Worker Node for Upgrade
Prepare worker node `node01` for upgrade:
1. Drain `node01` safely (`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force`) and save the output to `/opt/k8s/node01_drain.txt`.
2. Verify node01 is `SchedulingDisabled`.

### Task 2: Verify Kubelet Service Health
SSH to `node01` and verify that the `kubelet` service is active and running (`systemctl is-active kubelet`).

### Task 3: Restore Worker Node
Uncordon `node01` and verify it is `Ready` and schedulable.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d3-cka
```
