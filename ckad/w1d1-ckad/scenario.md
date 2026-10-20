# [CKAD W1D1-CKAD] Multi-Container Pods & Sidecar Logging

**Date:** 2026-10-12  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Multi-Container Pods & Sidecar Logging
1. Work in namespace `ckad-w1d1` on the cluster.
2. Objective: emptyDir shared volume and log shipping.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d1-ckad
```
