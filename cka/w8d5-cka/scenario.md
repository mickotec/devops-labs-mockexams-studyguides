# [CKA W8D5-CKA] Timed Mock Exam 2 & 3 Marathon

**Date:** 2026-11-20  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: PersistentVolume & Claim
1. Create a PersistentVolume named `pv-marathon-data`:
   - Capacity: `2Gi`
   - AccessModes: `ReadWriteOnce`
   - HostPath: `/data/pv-marathon`
2. In namespace `w8d5-marathon`, create a PersistentVolumeClaim named `pvc-marathon` requesting `2Gi` (accessModes: `ReadWriteOnce`).
3. Verify that the PVC reaches `Bound` status.

### Task 2: NodeAffinity Scheduling
1. Add label `zone=production-a` to node `node01`.
2. In namespace `w8d5-marathon`, deploy a Deployment named `zone-app` (image `nginx:alpine`, 2 replicas):
   - Configure `nodeAffinity` (`requiredDuringSchedulingIgnoredDuringExecution`) targeting nodes with key `zone` and value `production-a`.
3. Verify all pods run strictly on `node01`.

### Task 3: Taints & Tolerations
1. Taint node `node02` with `dedicated=special:NoSchedule`.
2. In namespace `w8d5-marathon`, deploy a Pod named `special-worker` (image `busybox:1.36`, command `["sleep", "3600"]`):
   - Add a toleration matching key `dedicated`, operator `Equal`, value `special`, effect `NoSchedule`.
   - Explicitly schedule it to `node02` (`nodeName: node02`).
3. Verify `special-worker` is `Running` on `node02`.

### Task 4: Deployment Rollout & Rollback
1. Update deployment `zone-app` image to `nginx:1.25.5-alpine`.
2. Verify the rollout completes.
3. Perform a rollout undo (`kubectl rollout undo deployment zone-app -n w8d5-marathon`) to roll back to the initial image `nginx:alpine`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d5-cka
```
