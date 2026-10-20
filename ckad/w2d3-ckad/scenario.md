# [CKAD W2D3-CKAD] Secrets Creation, Base64 & Safe Mounting

**Date:** 2026-10-21  
**Time Limit:** 25m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Secrets Creation, Base64 & Safe Mounting
1. Work in namespace `ckad-w2d3` on the cluster.
2. Objective: Opaque secrets, TLS secrets, and read-only mounts.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d3-ckad
```
