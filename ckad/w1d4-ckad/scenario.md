# [CKAD W1D4-CKAD] Deployments, Zero-Downtime Rollouts & Scaling

**Date:** 2026-10-15  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure Rolling Update & Scale Deployment
1. In namespace `ckad-w1d4`, inspect existing deployment `api-gateway`.
2. Reconfigure its update strategy to:
   - `type`: `RollingUpdate`
   - `maxSurge`: `1`
   - `maxUnavailable`: `0`
3. Update the container image of `api-gateway` to `nginx:1.25-alpine`.
4. Scale the deployment to `4` replicas.
5. Wait for the rollout to complete successfully.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d4-ckad
```
