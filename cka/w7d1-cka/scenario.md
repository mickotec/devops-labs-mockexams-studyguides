# [CKA W7D1-CKA] Cluster & Pod Networking Prerequisites

**Date:** 2026-11-09  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Inspect Active CNI Plugin
1. On `controlplane`, inspect the CNI network configuration directory `/etc/cni/net.d/`.
2. Find the active CNI configuration file (e.g. `10-flannel.conflist` or similar).
3. Extract the primary plugin type (e.g. `flannel`, `calico`, or `bridge`) and write it into `/opt/k8s/cni-plugin-type.txt`.

### Task 2: Extract Node PodCIDR Allocations
1. Retrieve the assigned `podCIDR` for worker nodes `node01` and `node02` using `kubectl get nodes -o jsonpath`.
2. Write each node and its podCIDR formatted as `<nodeName>=<podCIDR>` on separate lines into `/opt/k8s/node-podcidrs.txt`.
   Example format:
   ```
   node01=10.244.1.0/24
   node02=10.244.2.0/24
   ```

### Task 3: Deploy Cross-Node Pod Mesh
In namespace `w7d1-net`:
1. Create a DaemonSet named `net-mesh` with container image `busybox:1.36` running command `["sleep", "3600"]`.
2. Verify that a pod is scheduled and running on each worker node (`node01` and `node02`) and each has acquired a valid pod IP.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d1-cka
```
