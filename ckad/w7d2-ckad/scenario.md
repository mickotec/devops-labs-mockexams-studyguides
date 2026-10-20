# [CKAD W7D2-CKAD] PersistentVolumes: AccessModes & Reclaim Policies

**Date:** 2026-11-24  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create PersistentVolume
1. Create a PersistentVolume named `app-storage-pv`:
   - Capacity: `2Gi`
   - `accessModes`: `ReadWriteOnce`
   - `persistentVolumeReclaimPolicy`: `Retain`
   - `storageClassName`: `manual-storage`
   - `hostPath`: `/mnt/k8s-pv-data` (type: `DirectoryOrCreate`)
2. Verify that `app-storage-pv` reports status `Available`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d2-ckad
```
