# [CKA W2D3-CKA] Services: ClusterIP, NodePort & LoadBalancer

**Date:** 2026-10-07  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Multi-port ClusterIP Service
Deploy a pod `backend-api` in namespace `prod` (image: `nginx:alpine`, label `app=api`).
Expose it with a ClusterIP service `api-internal` in namespace `prod`:
- Port 80 -> TargetPort 80 (name: `http`)
- Port 443 -> TargetPort 443 (name: `https`)

### Task 2: NodePort Service Exposure
Create a NodePort service `web-public` in namespace `prod` targeting pod `backend-api`:
- Port: 80, TargetPort: 80, NodePort: `31200`
- Selector: `app=api`

### Task 3: Endpoints Verification
Confirm that endpoints object `api-internal` in namespace `prod` actively lists the IP address of pod `backend-api`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d3-cka
```
