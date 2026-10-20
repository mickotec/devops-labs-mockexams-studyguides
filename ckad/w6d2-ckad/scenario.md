# [CKAD W6D2-CKAD] Headless Services & StatefulSets Architecture

**Date:** 2026-11-17  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Headless Services & StatefulSets Architecture
1. Work in namespace `ckad-w6d2` on the cluster.
2. Objective: clusterIP None with stable network identities.
3. Deploy or configure workload named `ckad-app` using image `redis:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d2-ckad
```
