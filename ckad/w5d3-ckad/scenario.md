# [CKAD W5D3-CKAD] Rollback Strategies & Historical Revisions

**Date:** 2026-11-11  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Roll Back Faulty Deployment Revision
1. In namespace `ckad-w5d3`, deployment `checkout-api` is broken in revision 2 because an invalid image (`nginx:bad-tag-xyz`) was deployed.
2. Inspect rollout history using `kubectl rollout history deployment checkout-api -n ckad-w5d3`.
3. Roll back the deployment to healthy revision 1 using `kubectl rollout undo`.
4. Verify that the deployment restores running pods with image `nginx:1.24-alpine` and all 3 replicas become ready.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d3-ckad
```
