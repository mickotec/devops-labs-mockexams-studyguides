# [CKA W5D1-CKA] Node Maintenance: Cordon, Drain & Uncordon

**Date:** 2026-10-26  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Cordon Node
Mark worker node `node02` as unschedulable using `kubectl cordon node02`.
- Verify that `kubectl get nodes` displays `SchedulingDisabled` for `node02`.

### Task 2: Drain Node
Safely evict all running workloads from `node02` using `kubectl drain node02`:
- Ignore DaemonSets (`--ignore-daemonsets`)
- Delete emptyDir data (`--delete-emptydir-data`)
- Force eviction if needed (`--force`)
- Verify no user pods remain running on `node02`.

### Task 3: Return Node to Service
Uncordon `node02` using `kubectl uncordon node02` and verify it returns to `Ready` status without `SchedulingDisabled`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d1-cka
```
