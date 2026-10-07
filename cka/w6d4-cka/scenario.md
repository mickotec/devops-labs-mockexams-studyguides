# [CKA W6D4-CKA] Storage: Volumes, PV, PVC & StorageClasses

**Date:** 2026-11-05  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create PersistentVolume
Create a PersistentVolume named `app-data-pv`:
- Capacity: `200Mi`
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- HostPath: `/tmp/app-data-pv` (on `node01`)

### Task 2: Create PersistentVolumeClaim
In namespace `w6d4-storage`, create a PVC named `app-data-pvc`:
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- Storage request: `100Mi`

### Task 3: Deploy Storage Workload
Deploy a Pod named `storage-writer` in namespace `w6d4-storage` (image: `busybox:1.36`):
- Mount `app-data-pvc` at `/mnt/data`
- Command: `sh -c "echo StorageVerified > /mnt/data/success.txt && sleep 3600"`
- Confirm the PVC is `Bound` and the Pod runs.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d4-cka
```
