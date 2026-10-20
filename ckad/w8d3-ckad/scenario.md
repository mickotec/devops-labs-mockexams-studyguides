# [CKAD W8D3-CKAD] ClusterRoles & ClusterRoleBindings

**Date:** 2026-12-02  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Grant Cluster-Wide Read Permissions
1. Create a ClusterRole named `cluster-inspector`:
   - Resources: `nodes`, `persistentvolumes`, `storageclasses`
   - Verbs: `get`, `list`, `watch`
2. Create a ServiceAccount named `auditor-sa` in namespace `default`.
3. Bind ClusterRole `cluster-inspector` to `auditor-sa` using a ClusterRoleBinding named `bind-cluster-inspector`.
4. Verify with `kubectl auth can-i get nodes --as=system:serviceaccount:default:auditor-sa`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d3-ckad
```
