# [CKA W3D5-CKA] Priority Classes & Multiple Schedulers

**Date:** 2026-10-16  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Define PriorityClasses
1. Create a `PriorityClass` named `mission-critical` with value `1000000` and `globalDefault: false`.
2. Create a `PriorityClass` named `low-priority` with value `500` and `preemptionPolicy: Never`.

### Task 2: Workload Priority Association
In namespace `w3d5-priority`:
1. Deploy pod `critical-db` (image: `nginx:alpine`) assigned to `priorityClassName: mission-critical`.
2. Deploy pod `batch-worker` (image: `nginx:alpine`) assigned to `priorityClassName: low-priority`.
3. Verify both pods run and reflect their assigned priority values.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d5-cka
```
