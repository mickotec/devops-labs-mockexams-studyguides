# [CKA W2D1-CKA] ReplicaSets & Self-Healing Controllers

**Date:** 2026-10-05  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Repair Broken ReplicaSet
A ReplicaSet named `web-replicas` in namespace `core` is failing to manage pods because its selector labels (`app=web-app`) do not match its pod template labels (`app=frontend`).
1. Inspect the manifest `/opt/k8s/replicaset-broken.yaml`.
2. Correct the selector/template label mismatch so selector matches template labels `app=web-app,tier=frontend`.
3. Set the desired replicas to `4`.
4. Apply and verify that exactly 4 pods are running.

### Task 2: Test Self-Healing Mechanism
1. Delete two of the running pods belonging to `web-replicas` using `kubectl delete pod`.
2. Confirm that the ReplicaSet controller immediately recreates replacements and keeps 4 ready replicas.

### Task 3: Scale ReplicaSet
1. Scale the `web-replicas` ReplicaSet to `6` replicas using `kubectl scale`.
2. Confirm that 6 pods are running and ready.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d1-cka
```
