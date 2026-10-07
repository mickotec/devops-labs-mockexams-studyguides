# [CKA W4D5-CKA] Admission Controllers & Validating Webhooks

**Date:** 2026-10-23  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Audit Enabled Admission Plugins
Query the `kube-apiserver` static pod manifest on `controlplane` to inspect active admission plugins:
1. Extract the `--enable-admission-plugins` configuration flag.
2. Save the comma-separated list of enabled admission plugins to `/opt/k8s/enabled_admission_plugins.txt`.

### Task 2: Test NamespaceLifecycle Admission Controller
Verify that the `NamespaceLifecycle` admission controller actively rejects pod creation in a non-existent namespace:
- Run a test command attempting to create pod `ghost-pod` in non-existent namespace `void-ns` and save stderr output to `/opt/k8s/admission_rejection.log`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d5-cka
```
