# [CKAD W6D4-CKAD] NetworkPolicy: Egress Lockdown & DNS Resolution

**Date:** 2026-11-19  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: NetworkPolicy: Egress Lockdown & DNS Resolution
1. Work in namespace `ckad-w6d4` on the cluster.
2. Objective: Default deny egress while allowing CoreDNS port 53.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d4-ckad
```
