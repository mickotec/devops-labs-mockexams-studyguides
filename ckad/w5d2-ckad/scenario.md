# [CKAD W5D2-CKAD] Readiness Probes & Service Traffic Gating

**Date:** 2026-11-10  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Readiness Probes & Service Traffic Gating
1. Work in namespace `ckad-w5d2` on the cluster.
2. Objective: Preventing traffic to unready containers until warmup.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d2-ckad
```
