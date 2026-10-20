# [CKAD W6D4-CKAD] NetworkPolicies: Pod & Port Specific Ingress Rules

**Date:** 2026-11-19  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Allow Ingress Only From Authorized Pod
1. In namespace `ckad-w6d4`, target pod `api-backend` has label `tier=backend`.
2. Create a NetworkPolicy named `allow-frontend-only`:
   - Apply policy to pods matching `tier=backend`.
   - `policyTypes`: `[Ingress]`.
   - Allow ingress traffic ONLY from pods in the same namespace matching label `tier=frontend`.
   - Restrict allowed port strictly to TCP port `8080`.
3. Verify that all other pods are blocked from accessing `api-backend` on port `8080`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d4-ckad
```
