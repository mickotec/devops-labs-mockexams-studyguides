# [CKAD W5D2-CKAD] Rolling Updates with Zero-Downtime MaxSurge

**Date:** 2026-11-10  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Zero-Downtime Rolling Update
1. In namespace `ckad-w5d2`, inspect existing deployment `payment-gateway`.
2. Configure rolling update strategy parameters:
   - `maxSurge`: `2`
   - `maxUnavailable`: `0`
3. Update the container image to `nginx:1.25-alpine`.
4. Scale deployment to `5` replicas.
5. Track and ensure rollout completes successfully using `kubectl rollout status`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d2-ckad
```
