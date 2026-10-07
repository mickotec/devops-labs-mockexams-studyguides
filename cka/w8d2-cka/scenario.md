# [CKA W8D2-CKA] Troubleshooting: Worker Nodes & Network Failure

**Date:** 2026-11-17  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Restore NotReady Worker Node
Worker node `node02` is currently reporting `NotReady` or has a stopped kubelet service.
1. SSH to `node02` (`ssh node02`).
2. Inspect `kubelet` service status using `systemctl status kubelet`.
3. Start and enable `kubelet` using `sudo systemctl enable --now kubelet`.
4. Verify on `controlplane` that `node02` returns to `Ready` status.

### Task 2: Remove Degraded Taint
Worker node `node02` has been tainted with `trouble=unreachable:NoSchedule`.
1. Remove this taint from `node02` using `kubectl taint`.

### Task 3: Verify Workload Scheduling on node02
In namespace `w8d2-trouble`:
1. Create a Pod named `worker-canary` using image `nginx:alpine`.
2. Schedule it to `node02` (using `nodeName: node02` or `nodeSelector`).
3. Verify the pod is in `Running` state on `node02`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d2-cka
```
