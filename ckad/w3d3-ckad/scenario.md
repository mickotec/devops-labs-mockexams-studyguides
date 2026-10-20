# [CKAD W3D3-CKAD] Multi-Container Pods: Ambassador Pattern

**Date:** 2026-10-28  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Ambassador Local Proxy Routing
1. In namespace `ckad-w3d3-infra`, deploy a Redis pod named `redis-backend` exposed via ClusterIP service `redis-svc` on port 6379.
2. In namespace `ckad-w3d3-apps`, deploy Pod `client-ambassador`.
3. The pod has 2 containers:
   - `ambassador`: runs `alpine/socat:latest` or `busybox` listening on `localhost:6379` and proxying to `redis-svc.ckad-w3d3-infra.svc.cluster.local:6379`.
   - `client`: connects to `localhost:6379` using `nc -z localhost 6379` and writes `"AMBASSADOR_CONNECTED"` to `/tmp/proxy.log`.
4. Verify `/tmp/proxy.log` contains `"AMBASSADOR_CONNECTED"`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d3-ckad
```
