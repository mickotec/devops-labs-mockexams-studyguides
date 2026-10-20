# [CKAD W4D1-CKAD] Readiness Probes & Service Endpoint Gating

**Date:** 2026-11-02  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure HTTP Readiness Probe
1. In namespace `ckad-w4d1`, create a Pod named `order-processor` running image `nginx:alpine`.
2. Configure an HTTP GET readiness probe on path `/ready` port `80`:
   - `initialDelaySeconds`: `5`
   - `periodSeconds`: `3`
   - `failureThreshold`: `2`
3. Expose `order-processor` with a ClusterIP service named `order-service` on port `80`.
4. Ensure the probe passes by creating `/usr/share/nginx/html/ready` inside the container.
5. Verify that `order-service` registers the pod IP as a healthy endpoint.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d1-ckad
```
