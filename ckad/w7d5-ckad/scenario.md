# [CKAD W7D5-CKAD] StorageClasses & Delayed Volume Binding

**Date:** 2026-11-27  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create StorageClass with WaitForFirstConsumer
1. Create a StorageClass named `delayed-storage`:
   - `provisioner`: `kubernetes.io/no-provisioner`
   - `volumeBindingMode`: `WaitForFirstConsumer`
2. In namespace `ckad-w7d5`, create PVC `delayed-pvc`:
   - `storageClassName`: `delayed-storage`
   - Requests: `1Gi`
   - `accessModes`: `ReadWriteOnce`
3. Verify that `delayed-pvc` remains in status `Pending` (because no consuming pod has been scheduled).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d5-ckad
```
