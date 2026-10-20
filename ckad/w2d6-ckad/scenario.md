# [CKAD W2D6-CKAD] Week 2 Milestone: Hardened Workload Configuration

**Date:** 2026-10-24  
**Time Limit:** 40m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Week 2 Milestone: Hardened Workload Configuration
1. Work in namespace `ckad-w2d6` on the cluster.
2. Objective: Secure Pod with SA, Secret env, and readOnly root.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d6-ckad
```
