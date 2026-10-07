# [CKA W3D6-CKA] Week 3 Scheduling Troubleshooting Matrix

**Date:** 2026-10-17  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 3)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 3 Triathlon Tasks:
A set of broken scheduling scenarios has been injected into namespace `w3-milestone`:

1. **Fix Pending Pod `stuck-selector`**:
   It is stuck in `Pending` because its `nodeSelector` requires `hardware=gpu`, which no node has. Label `node02` with `hardware=gpu` to allow it to schedule.

2. **Fix Taint Mismatch on `stuck-taint`**:
   `node01` has been tainted with `dedicated=web:NoSchedule`. Update `stuck-taint` pod manifest or recreate it with a toleration for `dedicated=web:NoSchedule` so it runs on `node01`.

3. **Control Plane DaemonSet `infra-agent`**:
   DaemonSet `infra-agent` is only running on worker nodes because control plane nodes have the default `node-role.kubernetes.io/control-plane:NoSchedule` taint. Update the DaemonSet with a toleration so it schedules an agent on `controlplane` as well.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d6-cka
```
