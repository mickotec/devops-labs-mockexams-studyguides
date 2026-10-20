# [CKAD W5D4-CKAD] Container Logging: Multi-Container & Previous Logs

**Date:** 2026-11-12  
**Time Limit:** 20m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Container Logging: Multi-Container & Previous Logs
1. Work in namespace `ckad-w5d4` on the cluster.
2. Objective: Extracting logs from crashing pods with --previous.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d4-ckad
```
