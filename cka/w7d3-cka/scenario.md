# [CKA W7D3-CKA] Ingress Controllers & Routing Rules

**Date:** 2026-11-11  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Deploy Backend Microservices
In namespace `w7d3-ingress`:
1. Deploy `catalog` (image: `nginx:alpine`, port 80, 1 replica) and expose it via ClusterIP Service `catalog-svc` on port 80.
2. Deploy `orders` (image: `httpd:alpine`, port 80, 1 replica) and expose it via ClusterIP Service `orders-svc` on port 80.

### Task 2: Ingress Resource with Path-Based Routing
Create an Ingress resource named `store-ingress` in namespace `w7d3-ingress`:
- `ingressClassName: nginx`
- Host: `store.internal.example.com`
- Paths:
  - Path `/catalog` with pathType `Prefix` routed to backend service `catalog-svc` port `80`.
  - Path `/orders` with pathType `Prefix` routed to backend service `orders-svc` port `80`.

### Task 3: Rewrite Annotation
Add the rewrite target annotation to `store-ingress`:
`nginx.ingress.kubernetes.io/rewrite-target: /`

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d3-cka
```
