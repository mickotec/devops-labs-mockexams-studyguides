# [CKAD W2D6-CKAD] ServiceAccounts & API Token Security

**Date:** 2026-10-24  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Workload Identity & Token Mounting Control
1. In namespace `ckad-w2d6`, create a ServiceAccount named `build-deployer`.
2. Deploy a Pod named `isolated-agent` using image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Configure the pod to use ServiceAccount `build-deployer`.
4. Explicitly disable mounting the API token credential into the container by configuring:
   `automountServiceAccountToken: false` in the pod spec.
5. Verify that `/var/run/secrets/kubernetes.io/serviceaccount` does NOT exist inside the container.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d6-ckad
```
