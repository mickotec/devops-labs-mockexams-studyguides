# [CKAD W2D2-CKAD] ConfigMaps from Literals, Files & Env Injection

**Date:** 2026-10-20  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: ConfigMaps from Literals, Files & Env Injection
1. Work in namespace `ckad-w2d2` on the cluster.
2. Objective: Injecting configuration as env and volume mounts.
3. Deploy or configure workload named `ckad-app` using image `alpine:3.19`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d2-ckad
```
