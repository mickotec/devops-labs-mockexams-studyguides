# [CKAD W1D5-CKAD] Namespaces & Cross-Namespace DNS Communication

**Date:** 2026-10-16  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Cross-Namespace Service Discovery
1. In namespace `ckad-w1d5-backend`, there is a service named `db-service` running on port `6379`.
2. In namespace `ckad-w1d5-frontend`, create a client pod named `query-client` using image `busybox:1.36`.
3. The container must run a shell script that resolves and pings the backend service using its fully qualified domain name (FQDN):
   `nc -z -w 3 db-service.ckad-w1d5-backend.svc.cluster.local 6379`
   and logs `"CONNECTION_SUCCESS"` to `/tmp/conn.log`.
4. Ensure `query-client` is running and `/tmp/conn.log` records successful connection.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d5-ckad
```
