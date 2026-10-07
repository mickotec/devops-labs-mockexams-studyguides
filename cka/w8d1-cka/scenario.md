# [CKA W8D1-CKA] Troubleshooting: Control Plane & Applications

**Date:** 2026-11-16  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Repair Broken Static Pod
A static pod manifest on `controlplane` at `/etc/kubernetes/manifests/broken-watchdog.yaml` is failing to run due to an invalid image tag.
1. Inspect `/etc/kubernetes/manifests/broken-watchdog.yaml`.
2. Change the image to `busybox:1.36` and ensure its command is `["sh", "-c", "sleep 3600"]`.
3. Wait for the kubelet to reconcile and verify that static pod `broken-watchdog-controlplane` enters `Running` status.

### Task 2: Fix CrashLoopBackOff Application Pod
In namespace `w8d1-trouble`:
Pod `db-connector` is failing in a CrashLoopBackOff state because a required environment variable `DB_HOST` is missing and its exit code is non-zero.
1. Inspect logs using `kubectl logs db-connector -n w8d1-trouble`.
2. Edit or recreate the pod with:
   - Environment variable: `DB_HOST=10.0.0.1`
   - Command: `["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]`
3. Verify that `db-connector` reaches `Running` status.

### Task 3: Export Control Plane Diagnostics
1. Capture the last 20 lines of the `kube-apiserver` static pod log on `controlplane` and save them to `/opt/k8s/apiserver_log_sample.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d1-cka
```
