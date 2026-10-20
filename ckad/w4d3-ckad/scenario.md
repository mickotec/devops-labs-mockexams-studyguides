# [CKAD W4D3-CKAD] Canary Deployment Strategy with Weighted Traffic

**Date:** 2026-11-04  
**Time Limit:** 25m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Canary Deployment Strategy with Weighted Traffic
1. Work in namespace `ckad-w4d3` on the cluster.
2. Objective: Splitting traffic 80/20 across stable and canary deployments.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d3-ckad
```
