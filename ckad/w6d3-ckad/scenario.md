# [CKAD W6D3-CKAD] NetworkPolicy: Ingress Isolation & Pod Selectors

**Date:** 2026-11-18  
**Time Limit:** 30m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: NetworkPolicy: Ingress Isolation & Pod Selectors
1. Work in namespace `ckad-w6d3` on the cluster.
2. Objective: Restricting incoming traffic to database pods.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d3-ckad
```
