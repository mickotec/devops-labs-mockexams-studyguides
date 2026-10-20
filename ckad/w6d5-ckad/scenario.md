# [CKAD W6D5-CKAD] Ingress Networking: Host & Path Routing

**Date:** 2026-11-20  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure Multi-Path Ingress Resource
1. In namespace `ckad-w6d5`, deploy services `orders-svc` (port 8080) and `catalog-svc` (port 8080).
2. Create an Ingress named `ecommerce-ingress`:
   - Host: `store.internal`
   - Path `/orders` (Prefix) routing to service `orders-svc:8080`
   - Path `/catalog` (Prefix) routing to service `catalog-svc:8080`
3. Verify the Ingress routes both paths to the corresponding services.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d5-ckad
```
