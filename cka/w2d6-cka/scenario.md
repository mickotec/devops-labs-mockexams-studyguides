# [CKA W2D6-CKA] Week 2 Speed Drills & Controller Triathlon

**Date:** 2026-10-10  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 2)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 2 Triathlon Tasks:
1. Create a Deployment `order-processor` with 5 replicas (image: `nginx:1.24-alpine`) in namespace `triathlon-w2`.
2. Expose it via NodePort service `order-service` on port `30500` (targetPort: 80).
3. Perform an in-place image update to `nginx:1.25-alpine`, record change-cause annotation, then rollback to revision 1.
4. Export the deployment configuration without cluster-specific fields (`uid`, `status`, `resourceVersion`) to `/opt/k8s/clean-export.yaml`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d6-cka
```
