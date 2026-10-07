# [CKA W7D4-CKA] Gateway API (2025 Updates)

**Date:** 2026-11-12  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Verify GatewayClass
A GatewayClass named `cluster-gateway-class` is available in the cluster.
- Inspect it with `kubectl get gatewayclasses cluster-gateway-class`.

### Task 2: Create Gateway
In namespace `w7d4-gw`:
1. Create a Gateway resource named `prod-gateway`:
   - `gatewayClassName`: `cluster-gateway-class`
   - Listeners:
     - `name`: `http`
     - `port`: `80`
     - `protocol`: `HTTP`
     - `allowedRoutes`: `{ "namespaces": { "from": "Same" } }`

### Task 3: Create HTTPRoute
In namespace `w7d4-gw`:
1. Create an `HTTPRoute` resource named `api-route`:
   - Parent reference to `prod-gateway` (sectionName: `http`)
   - Hostname: `api.example.com`
   - Rules:
     - Match path prefix `/v1`
     - Route to backend service `api-service` on port `8080`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d4-cka
```
