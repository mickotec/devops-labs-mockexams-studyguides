# [CKAD W3D3-CKAD] Node Affinity: Required vs Preferred

**Date:** 2026-10-28  
**Time Limit:** 25m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Node Affinity: Required vs Preferred
1. Work in namespace `ckad-w3d3` on the cluster.
2. Objective: requiredDuringScheduling vs preferredDuringScheduling.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d3-ckad
```
