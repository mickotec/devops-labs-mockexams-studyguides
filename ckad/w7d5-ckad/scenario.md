# [CKAD W7D5-CKAD] Kustomize Basics: Overlays, Patches & Transformers

**Date:** 2026-11-27  
**Time Limit:** 30m  
**Difficulty:** Easy  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Kustomize Basics: Overlays, Patches & Transformers
1. Work in namespace `ckad-w7d5` on the cluster.
2. Objective: base and overlays (dev/prod) with commonLabels and patches.
3. Deploy or configure workload named `ckad-app` using image `kustomize`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d5-ckad
```
