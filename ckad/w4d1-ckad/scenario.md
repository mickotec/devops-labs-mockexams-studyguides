# [CKAD W4D1-CKAD] Rolling Updates, Rollout History & Undo/Rollback

**Date:** 2026-11-02  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Rolling Updates, Rollout History & Undo/Rollback
1. Work in namespace `ckad-w4d1` on the cluster.
2. Objective: maxSurge, maxUnavailable, change-cause, and rollback.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d1-ckad
```
