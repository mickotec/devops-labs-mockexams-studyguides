# [CKA W4D4-CKA] Autoscaling: HPA, VPA & In-Place Pod Resize

**Date:** 2026-10-22  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Deploy Workload with Resource Requests
In namespace `w4d4-scale`, create a Deployment named `order-backend`:
- Replicas: `2`
- Image: `nginx:alpine`
- Container resource requests: `cpu: 50m`, `memory: 64Mi`
- Container resource limits: `cpu: 200m`, `memory: 128Mi`

### Task 2: Configure HorizontalPodAutoscaler (HPA)
Create an HPA named `order-backend-hpa` in namespace `w4d4-scale` targeting `deployment/order-backend`:
- Min replicas: `2`
- Max replicas: `6`
- Target CPU utilization percentage: `50%`
- Verify that `kubectl get hpa -n w4d4-scale` shows the target and minimum/maximum replicas.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d4-cka
```
