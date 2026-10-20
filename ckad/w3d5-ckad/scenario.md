# [CKAD W3D5-CKAD] Node Taints, Effects & Pod Tolerations

**Date:** 2026-10-30  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Schedule Pod on Tainted Worker Node
1. Worker node `node01` has been tainted with:
   `dedicated=analytics:NoSchedule`
2. In namespace `ckad-w3d5`, create a Pod named `analytics-engine` using image `nginx:alpine`.
3. Add the required toleration so that `analytics-engine` can schedule onto `node01`.
4. Also add `spec.nodeName: node01` or `spec.nodeSelector` to guarantee it lands on `node01`.
5. Verify that `analytics-engine` is `Running` on `node01`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d5-ckad
```
