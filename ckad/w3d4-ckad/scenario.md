# [CKAD W3D4-CKAD] Init Containers & Service Dependency Gating

**Date:** 2026-10-29  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Unblock Pod Stuck in Init:0/1
1. In namespace `ckad-w3d4`, there is an existing pod named `webapp-gated` currently stuck in `Init:0/1`.
2. Inspect the pod specifications and init container logs to determine what dependency it is waiting for.
3. You will discover the init container is waiting for service `mysql-backend` on port `3306`.
4. Deploy a Pod `mysql-dummy` running `busybox:1.36` (listening on port 3306 with `nc -lk -p 3306`) and expose it as a ClusterIP service named `mysql-backend` on port `3306`.
5. Verify that `webapp-gated` completes its init step and transitions to `Running` (1/1 Ready).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d4-ckad
```
