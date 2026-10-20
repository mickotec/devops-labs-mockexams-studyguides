# [CKAD W1D2-CKAD] Init Containers & Service Dependency Blocking

**Date:** 2026-10-13  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Init Containers & Service Dependency Blocking
1. Work in namespace `ckad-w1d2` on the cluster.
2. Objective: Sequential init containers blocking until db is ready.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d2-ckad
```
