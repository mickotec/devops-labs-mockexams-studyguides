# [CKAD W5D3-CKAD] Startup Probes for Slow-Initializing Applications

**Date:** 2026-11-11  
**Time Limit:** 25m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Startup Probes for Slow-Initializing Applications
1. Work in namespace `ckad-w5d3` on the cluster.
2. Objective: failureThreshold and periodSeconds for slow containers.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d3-ckad
```
