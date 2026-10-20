# [CKAD W5D1-CKAD] Liveness Probes: HTTP, Command & TCP Checks

**Date:** 2026-11-09  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Liveness Probes: HTTP, Command & TCP Checks
1. Work in namespace `ckad-w5d1` on the cluster.
2. Objective: Detecting deadlock and restarting failed containers.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d1-ckad
```
