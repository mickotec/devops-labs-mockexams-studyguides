# [CKAD W3D4-CKAD] Taints & Tolerations: Dedicated Workload Isolation

**Date:** 2026-10-29  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Taints & Tolerations: Dedicated Workload Isolation
1. Work in namespace `ckad-w3d4` on the cluster.
2. Objective: Tainting worker nodes with NoSchedule and tolerations.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d4-ckad
```
