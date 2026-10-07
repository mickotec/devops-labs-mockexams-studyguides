# [CKA W1D1-CKA] Kubernetes Architecture & Container Runtimes

**Date:** 2026-09-14  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Troubleshoot Control Plane Static Pod
1. Inspect the control plane static pod manifests located in `/etc/kubernetes/manifests/` on node `controlplane`.
2. Determine why `kube-scheduler` is failing to start. (Check `/var/log/pods` or kubelet journal on `controlplane`).
3. Correct the error in `/etc/kubernetes/manifests/kube-scheduler.yaml` without breaking other parameters.
4. Verify that the static pod `kube-scheduler-controlplane` is in `Running` state (1/1 Ready) and that the test pod `w1d1-pending-test` in namespace `default` transitions from `Pending` to `Running`.

### Task 2: CRI Runtime Inspection & Rogue Container Termination
1. SSH into worker node `node01`.
2. Using the CRI CLI utility (`crictl`), inspect the running containers managed by runtime `containerd`.
3. Locate the rogue container named `rogue-crypto-miner` that was started directly on the node bypassing the API server.
4. Stop and remove the rogue container using `crictl`.

### Task 3: Create a Worker Static Pod
1. On worker node `node01`, configure a static pod manifest named `node01-monitor.yaml` in kubelet's static pod manifest directory (`/etc/kubernetes/manifests/`).
2. The pod specification must satisfy:
   - Pod Name: `node01-monitor`
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]`
   - Volume: Mount host directory `/var/log` into container directory `/var/log`.
3. Verify from `controlplane` that `node01-monitor-node01` appears in `kubectl get pods -A` and is in `Running` state.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d1-cka
```
