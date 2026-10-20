# [CKAD W3D1-CKAD] Multi-Container Pods: Sidecar Log Streaming

**Date:** 2026-10-26  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Sidecar Container Log Shipper
1. In namespace `ckad-w3d1`, deploy a multi-container Pod named `app-logger`.
2. Main container named `app`:
   - Image: `busybox:1.36`
   - Command: `sh -c "while true; do echo 'TRANSACTION_ID='$(date +%s%N) >> /var/log/app/tx.log; sleep 2; done"`
   - Mount volume `log-storage` at `/var/log/app`.
3. Sidecar container named `sidecar`:
   - Image: `busybox:1.36`
   - Command: `sh -c "tail -n+1 -F /var/log/app/tx.log"`
   - Mount same volume `log-storage` at `/var/log/app`.
4. Define volume `log-storage` as `emptyDir: {}`.
5. Verify both containers are 2/2 Ready and `kubectl logs app-logger -c sidecar` outputs the transaction logs.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d1-ckad
```
