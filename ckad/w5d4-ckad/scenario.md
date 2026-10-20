# [CKAD W5D4-CKAD] Blue-Green Deployment Cutover

**Date:** 2026-11-12  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Atomic Cutover to Green Release
1. In namespace `ckad-w5d4`, service `web-portal` currently routes to Blue release (`version=v1`).
2. Deploy the Green release:
   - Deployment Name: `portal-green`
   - Replicas: `3`
   - Labels: `app=portal,version=v2`
   - Image: `nginx:1.25-alpine`
3. Verify `portal-green` achieves 3/3 Ready status.
4. Atomically update Service `web-portal` selector to route 100% of incoming traffic to `version: v2`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d4-ckad
```
