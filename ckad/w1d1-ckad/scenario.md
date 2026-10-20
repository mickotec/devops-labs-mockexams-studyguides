# [CKAD W1D1-CKAD] Pod Architecture & Multi-Container Pod Creation

**Date:** 2026-10-12  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Repair Broken Pod Manifest & Configure Multi-Container Pod
1. On node `controlplane`, a junior developer left a broken YAML manifest at `/tmp/webapp-core.yaml` intended to run in namespace `ckad-w1d1`.
2. Inspect and repair the syntax errors in `/tmp/webapp-core.yaml`:
   - Pod Name: `webapp-core`
   - Namespace: `ckad-w1d1`
   - Primary Container: named `web-app`, running image `nginx:1.24-alpine`, listening on containerPort `80`.
   - Sidecar Container: named `log-shipper`, running image `busybox:1.36`, executing the command:
     `sh -c "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"`
   - Storage: Mount a shared `emptyDir` volume named `shared-logs` at `/var/log/app` in **both** containers.
3. Apply the repaired manifest and verify that pod `webapp-core` enters `Running` status with both containers ready (`2/2`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d1-ckad
```
