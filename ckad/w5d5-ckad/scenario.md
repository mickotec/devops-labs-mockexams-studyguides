# [CKAD W5D5-CKAD] Canary Deployment Traffic Splitting

**Date:** 2026-11-13  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Deploy Canary Workload
1. In namespace `ckad-w5d5`, service `catalog-svc` routes traffic to pods with label `app=catalog`.
2. Existing baseline deployment `catalog-stable` has `4` replicas of `nginx:1.24-alpine` with labels `app=catalog,track=stable`.
3. Create Canary deployment named `catalog-canary`:
   - Replicas: `1`
   - Labels: `app=catalog,track=canary`
   - Image: `nginx:1.25-alpine`
4. Verify that total endpoints for service `catalog-svc` equals `5` (4 stable + 1 canary, 20% traffic split).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d5-ckad
```
