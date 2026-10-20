# [CKAD W6D1-CKAD] Services: ClusterIP, NodePort & Port Mapping

**Date:** 2026-11-16  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Expose Deployments with ClusterIP & NodePort
1. In namespace `ckad-w6d1`, deploy `backend-deploy` (image `redis:alpine`, 2 replicas) and `frontend-deploy` (image `nginx:alpine`, 2 replicas).
2. Create a ClusterIP Service named `backend-svc` exposing `backend-deploy` on port `6379` mapping to targetPort `6379`.
3. Create a NodePort Service named `frontend-svc` exposing `frontend-deploy` on port `80`, mapping to targetPort `80`, with `nodePort: 30080`.
4. Verify both services are registered with active endpoints.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d1-ckad
```
