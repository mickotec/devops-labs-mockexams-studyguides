# [CKA W7D6-CKA] Week 7 Network Mastery Triathlon

**Date:** 2026-11-14  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Multi-Service Architecture
In namespace `w7d6-triathlon`:
1. Deploy `web-frontend` (image `nginx:alpine`, 2 replicas, port 80, label `app=web-frontend`) and expose with ClusterIP service `frontend-svc` on port 80.
2. Deploy `api-backend` (image `nginx:alpine`, 2 replicas, port 80, label `app=api-backend`) and expose with ClusterIP service `backend-svc` on port 80.

### Task 2: TLS Secret & Ingress Routing
In namespace `w7d6-triathlon`:
1. Generate a self-signed TLS cert and private key for domain `triathlon.k8s.local` and create Secret `triathlon-tls`.
2. Create an Ingress named `triathlon-ingress` with `ingressClassName: nginx`:
   - Host: `triathlon.k8s.local`
   - TLS enabled using Secret `triathlon-tls`
   - Path `/api` (Prefix) -> `backend-svc:80`
   - Path `/` (Prefix) -> `frontend-svc:80`
   - Annotation `nginx.ingress.kubernetes.io/rewrite-target: /`

### Task 3: Network Isolation Policy
In namespace `w7d6-triathlon`:
1. Create a NetworkPolicy named `backend-isolation` targeting pods with `app: api-backend`.
2. Allow incoming traffic ONLY from pods with label `app: web-frontend` on TCP port `80`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d6-cka
```
