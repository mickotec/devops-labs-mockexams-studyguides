# [CKA W3D4-CKA] DaemonSets & Static Pods Architecture

**Date:** 2026-10-15  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create DaemonSet
In namespace `w3d4-ds`, create a DaemonSet named `log-collector`:
- Image: `fluent/fluent-bit:2.1.8` (or `nginx:alpine` if offline)
- Labels: `app=log-collector, tier=monitoring`
- Ensure a pod runs on all available worker nodes.

### Task 2: Create Static Pod on Worker Node
Create a Static Pod named `node02-telemetry` on node `node02`:
- Image: `nginx:alpine`
- Path: place manifest in the kubelet static pod directory (`/etc/kubernetes/manifests/node02-telemetry.yaml`)
- Verify from `controlplane` that `node02-telemetry-node02` is registered and running.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d4-cka
```
