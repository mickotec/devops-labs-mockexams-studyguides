# [CKAD W7D2-CKAD] PersistentVolumes & PersistentVolumeClaims

**Date:** 2026-11-24  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: PersistentVolumes & PersistentVolumeClaims
1. Work in namespace `ckad-w7d2` on the cluster.
2. Objective: Static volume provisioning and ReadWriteOnce binding.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d2-ckad
```
