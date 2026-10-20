# [CKAD W4D2-CKAD] Blue-Green Deployment Cutover Pattern

**Date:** 2026-11-03  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Blue-Green Deployment Cutover Pattern
1. Work in namespace `ckad-w4d2` on the cluster.
2. Objective: Switching traffic between v1 and v2 via service selector.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d2-ckad
```
