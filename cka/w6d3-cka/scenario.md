# [CKA W6D3-CKA] ServiceAccounts & SecurityContexts

**Date:** 2026-11-04  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create ServiceAccount
In namespace `w6d3-sec`:
Create a ServiceAccount named `restricted-sa` with `automountServiceAccountToken: false`.

### Task 2: Hardened Pod SecurityContext
Deploy a Pod named `hardened-app` in namespace `w6d3-sec` (image: `nginx:alpine`):
- Associate with ServiceAccount `restricted-sa`.
- Pod-level `securityContext`:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `fsGroup: 20000`
- Container-level `securityContext`:
  - `allowPrivilegeEscalation: false`
  - `readOnlyRootFilesystem: true`
  - `capabilities.drop: ["ALL"]`
- Mount an `emptyDir` volume at `/tmp` so nginx has a writable scratch space.
- Verify the pod runs successfully without crashing.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d3-cka
```
