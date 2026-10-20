# [CKAD W8D2-CKAD] RBAC: Roles & RoleBindings

**Date:** 2026-12-01  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Role & RoleBinding
1. In namespace `ckad-w8d2`, create a ServiceAccount named `app-operator`.
2. Create a Role named `pod-admin` in namespace `ckad-w8d2`:
   - Resources: `pods`, `pods/log`
   - Verbs: `get`, `list`, `watch`, `create`, `delete`
3. Bind Role `pod-admin` to ServiceAccount `app-operator` using a RoleBinding named `bind-pod-admin`.
4. Verify permissions using:
   `kubectl auth can-i create pods -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d2-ckad
```
