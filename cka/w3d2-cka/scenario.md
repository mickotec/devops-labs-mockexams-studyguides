# [CKA W3D2-CKA] Taints, Tolerations & Node Affinity

**Date:** 2026-10-13  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Node Tainting
Taint node `node01` with `workload=critical:NoSchedule`.

### Task 2: Tolerations
Deploy a pod named `critical-processor` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Add a toleration matching `workload=critical:NoSchedule`.
- Schedule the pod explicitly to `node01` (using `nodeSelector` or `nodeName`).
- Confirm it achieves `Running` status on `node01`.

### Task 3: Required Node Affinity
Deploy a pod named `data-collector` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Use `affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`.
- Target nodes with label `kubernetes.io/hostname` having value `node02`.
- Confirm the pod runs on `node02`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d2-cka
```
