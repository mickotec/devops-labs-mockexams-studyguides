# [CKA W2D2-CKA] Deployments, Rollouts & Revisions

**Date:** 2026-10-06  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Rolling Update Deployment
Create a deployment named `payment-app` in namespace `finance`:
- Replicas: `3`
- Image: `nginx:1.24-alpine`
- Strategy: RollingUpdate with `maxSurge: 1`, `maxUnavailable: 0`

### Task 2: Upgrade with Revision History Annotation
Update the image of `payment-app` to `nginx:1.25-alpine` and record the change cause annotation: `version 1.25 upgrade`.

### Task 3: Simulating Broken Rollout & Rollback
1. Update the image to `nginx:does-not-exist` (triggering ImagePullBackOff).
2. Check rollout status with `kubectl rollout status`.
3. Undo the rollout back to the previous stable revision using `kubectl rollout undo`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d2-cka
```
