# [CKAD W7D3-CKAD] PersistentVolumeClaims & Volume Binding

**Date:** 2026-11-25  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Bind PersistentVolumeClaim
1. On the cluster, PV `claim-target-pv` (1Gi, `storageClassName: manual-target`) already exists in `Available` status.
2. In namespace `ckad-w7d3`, create a PersistentVolumeClaim named `app-storage-pvc`:
   - `storageClassName`: `manual-target`
   - `accessModes`: `ReadWriteOnce`
   - Requests: `1Gi` storage
3. Verify `app-storage-pvc` transitions from `Pending` to `Bound` to `claim-target-pv`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d3-ckad
```
