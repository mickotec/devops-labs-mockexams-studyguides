# [CKA W1D4-CKA] Multi-Container Pod Patterns & Init Containers

**Date:** 2026-09-17  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Namespace `telemetry`
Create a namespace named `telemetry`.

### Task 2: Multi-Container Sidecar Pod (`order-service`)
Create a Pod named `order-service` in namespace `telemetry`:
1. Volume:
   - Name: `log-volume`
   - Type: `emptyDir: {}`
2. Container 1 (`app`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]`
   - Mount: `log-volume` at `/var/log/app`
3. Container 2 (`logger`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]`
   - Mount: `log-volume` at `/var/log/app` (readOnly: true)

### Task 3: Init Container Dependency Gating (`web-portal`)
Create a Pod named `web-portal` in namespace `telemetry`:
1. Init Container (`db-wait`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "until [ -f /opt/data/ready.flag ]; do echo waiting for ready.flag; sleep 2; done"]`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
2. Application Container (`web`):
   - Image: `nginx:1.25-alpine`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
3. Simulate dependency completion by creating `/opt/data/ready.flag` or structuring the pod so it runs smoothly.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d4-cka
```
