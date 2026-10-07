# [CKA W3D1-CKA] Manual Scheduling, Labels & Selectors

**Date:** 2026-10-12  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Node Labeling
1. Add the label `disktype=ssd` to `node01`.
2. Add the label `environment=production` to `node02`.

### Task 2: Constraint-based Scheduling with nodeSelector
Create a Pod named `storage-worker` in namespace `w3d1-sched` using image `nginx:alpine`:
- It must specify a `nodeSelector` requiring `disktype: ssd`.
- Verify it is scheduled and running on `node01`.

### Task 3: Manual Scheduling via nodeName
A manifest at `/opt/k8s/orphan-pod.yaml` on `controlplane` defines a Pod named `orphan-task` in namespace `w3d1-sched` (image: `busybox:1.36`, command: `sh -c "sleep 3600"`).
- Modify the manifest to directly assign it to `node02` using `spec.nodeName: node02` (bypassing `kube-scheduler`).
- Apply the manifest and verify the pod runs on `node02`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d1-cka
```
