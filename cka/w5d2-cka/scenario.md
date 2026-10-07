# [CKA W5D2-CKA] Cluster Upgrade: Kubeadm Control Plane

**Date:** 2026-10-27  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Kubeadm Upgrade Plan Audit
On `controlplane`:
1. Run `kubeadm upgrade plan` using `sudo`.
2. Extract the current component versions table and save the output to `/opt/k8s/upgrade_plan.txt`.

### Task 2: Inspect Static Pod Manifests
Verify that all control plane static pod manifests in `/etc/kubernetes/manifests` (`kube-apiserver.yaml`, `kube-controller-manager.yaml`, `kube-scheduler.yaml`, `etcd.yaml`) are present, valid, and owned by `root:root`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d2-cka
```
