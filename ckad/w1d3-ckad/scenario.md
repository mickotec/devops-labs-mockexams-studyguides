# [CKAD W1D3-CKAD] ReplicaSets, Label Selectors & Pod Adoption

**Date:** 2026-10-14  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create ReplicaSet & Adopt Orphaned Pod
1. In namespace `ckad-w1d3`, there is an unmanaged pod named `orphan-web` with label `app=frontend`.
2. Create a ReplicaSet named `frontend-rs` in namespace `ckad-w1d3`:
   - `spec.replicas`: `3`
   - `spec.selector.matchLabels`: `app=frontend,tier=web`
   - Pod Template Image: `nginx:1.24-alpine`
   - Template Labels: `app=frontend,tier=web`
3. Modify the labels of `orphan-web` to add `tier=web` so that `frontend-rs` acquires it.
4. Verify that total pods matching `app=frontend,tier=web` in namespace `ckad-w1d3` equals exactly 3.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d3-ckad
```
