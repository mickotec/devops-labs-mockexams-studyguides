# [CKAD W8D5-CKAD] Helm Package Management & Value Overrides

**Date:** 2026-12-04  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure Helm Chart Release
1. In namespace `ckad-w8d5`, verify Helm is installed on `controlplane`.
2. A sample chart directory exists at `/tmp/sample-chart`.
3. Install a release named `frontend-app` from `/tmp/sample-chart` into namespace `ckad-w8d5`:
   - Override `replicaCount`: set to `3` using `--set replicaCount=3`
4. Verify the release status using `helm list -n ckad-w8d5` and ensure 3 pods are running.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d5-ckad
```
