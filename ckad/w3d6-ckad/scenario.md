# [CKAD W3D6-CKAD] Node Selectors & Required NodeAffinity

**Date:** 2026-10-31  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Attract Pods Using Required NodeAffinity
1. Label worker node `node02` with label `storage-tier=nvme`.
2. In namespace `ckad-w3d6`, create a Pod named `fast-io-worker` with image `redis:alpine`.
3. Configure `spec.affinity.nodeAffinity` using `requiredDuringSchedulingIgnoredDuringExecution` requiring that `storage-tier` is `In` values `["nvme"]`.
4. Verify that `fast-io-worker` schedules exclusively onto `node02` and enters `Running` state.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d6-ckad
```
