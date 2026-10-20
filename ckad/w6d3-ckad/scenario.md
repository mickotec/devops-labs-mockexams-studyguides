# [CKAD W6D3-CKAD] NetworkPolicies: Default Ingress Denial

**Date:** 2026-11-18  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Isolate Namespace with Default-Deny
1. In namespace `ckad-w6d3`, deploy Pod `secure-db` running `redis:alpine` exposed by service `db-svc:6379`.
2. Create a NetworkPolicy named `default-deny-ingress`:
   - Match all pods in namespace `ckad-w6d3` (`podSelector: {}`).
   - `policyTypes`: `[Ingress]`.
   - Leave `ingress` rules empty to deny all incoming connections.
3. Verify policy is created and inspect policy types using `kubectl describe netpol`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d3-ckad
```
