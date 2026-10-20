# [CKAD W2D4-CKAD] SecurityContexts: UID, GID & Linux Capabilities

**Date:** 2026-10-22  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: SecurityContexts: UID, GID & Linux Capabilities
1. Work in namespace `ckad-w2d4` on the cluster.
2. Objective: runAsUser, runAsGroup, fsGroup, drop ALL, add NET_ADMIN.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d4-ckad
```
