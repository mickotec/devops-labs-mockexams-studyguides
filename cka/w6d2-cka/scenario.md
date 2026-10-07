# [CKA W6D2-CKA] RBAC (Roles, RoleBindings & ClusterRoles)

**Date:** 2026-11-03  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Namespace Role & RoleBinding
In namespace `w6d2-rbac`:
1. Create a `Role` named `pod-operator` granting `get, list, watch, create, delete` permissions on `pods`.
2. Create a `RoleBinding` named `bind-pod-operator` binding `pod-operator` to ServiceAccount `dev-sa`.

### Task 2: ClusterRole & ClusterRoleBinding
1. Create a `ClusterRole` named `node-observer` granting `get, list, watch` permissions on `nodes`.
2. Create a `ClusterRoleBinding` named `bind-node-observer` binding `node-observer` to ServiceAccount `dev-sa` in namespace `w6d2-rbac`.

### Task 3: RBAC Authorization Verification
Verify authorization using `kubectl auth can-i`:
- Check if `dev-sa` in `w6d2-rbac` can list pods in `w6d2-rbac` (must be `yes`).
- Check if `dev-sa` in `w6d2-rbac` can list nodes cluster-wide (must be `yes`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d2-cka
```
