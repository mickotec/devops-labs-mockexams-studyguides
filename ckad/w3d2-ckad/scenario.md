# [CKAD W3D2-CKAD] Manual Node Scheduling & NodeSelector

**Date:** 2026-10-27  
**Time Limit:** 20m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Manual Node Scheduling & NodeSelector
1. Work in namespace `ckad-w3d2` on the cluster.
2. Objective: Targeting specific nodes using nodeSelector and labels.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d2-ckad
```
