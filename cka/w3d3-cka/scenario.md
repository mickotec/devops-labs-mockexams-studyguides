# [CKA W3D3-CKA] Resource Requirements, Limits & LimitRanges

**Date:** 2026-10-14  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure LimitRange
In namespace `w3d3-resources`, create a `LimitRange` named `resource-bounds`:
- Default container request: `CPU: 100m`, `Memory: 64Mi`
- Default container limit: `CPU: 200m`, `Memory: 128Mi`
- Max container limit: `CPU: 500m`, `Memory: 256Mi`

### Task 2: Deploy Bounded Workload
Deploy a pod named `bounded-service` in namespace `w3d3-resources` (image: `nginx:alpine`):
- Explicit requests: `CPU: 150m`, `Memory: 100Mi`
- Explicit limits: `CPU: 300m`, `Memory: 200Mi`
- Verify it is running.

### Task 3: Test Default Limit Injection
Deploy a pod named `unconstrained-pod` in namespace `w3d3-resources` (image: `nginx:alpine`) without any resource specs.
- Verify that the `LimitRange` automatically injected the default requests (100m/64Mi) and limits (200m/128Mi).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d3-cka
```
