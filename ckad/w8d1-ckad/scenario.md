# [CKAD W8D1-CKAD] Kubeconfig Files & Context Management

**Date:** 2026-11-30  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Custom Context & Set Default Namespace
1. On node `controlplane`, create a working kubeconfig copy at `/tmp/custom-kubeconfig`.
2. Configure a new context named `developer-ctx` in `/tmp/custom-kubeconfig`:
   - `cluster`: `kubernetes`
   - `user`: `kubernetes-admin`
   - `namespace`: `ckad-dev-ns`
3. Set the current-context of `/tmp/custom-kubeconfig` to `developer-ctx`.
4. Verify that running `kubectl --kubeconfig=/tmp/custom-kubeconfig config current-context` outputs `developer-ctx`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d1-ckad
```
