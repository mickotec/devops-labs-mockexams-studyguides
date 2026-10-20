# [CKAD W3D1-CKAD] Resource Requests, Limits & OOM Troubleshooting

**Date:** 2026-10-26  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Resource Requests, Limits & OOM Troubleshooting
1. Work in namespace `ckad-w3d1` on the cluster.
2. Objective: CPU/Memory requests, limits, and OOMKilled resolution.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d1-ckad
```
