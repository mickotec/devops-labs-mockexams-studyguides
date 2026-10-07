# [CKA W8D4-CKA] Timed Mock Exam 1 & Step-by-Step Review

**Date:** 2026-11-19  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: RBAC Role & Binding
In namespace `w8d4-exam`:
1. Create a ServiceAccount named `deploy-bot`.
2. Create a Role named `pod-reader` granting `["get", "list", "watch"]` permissions on `pods`.
3. Create a RoleBinding named `deploy-bot-reader` binding `deploy-bot` to Role `pod-reader`.

### Task 2: Multi-Container Pod with Shared Volume
In namespace `w8d4-exam`:
Create a Pod named `app-logger` sharing volume `shared-logs` (`emptyDir`):
1. Container `producer`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]`, mounting `shared-logs` to `/var/log`.
2. Container `consumer`: image `busybox:1.36`, command `["sh", "-c", "tail -f /var/log/app.log"]`, mounting `shared-logs` to `/var/log`.

### Task 3: Secrets Injected into Environment
In namespace `w8d4-exam`:
1. Create a Secret named `db-credentials` with `DB_USER=dbadmin` and `DB_PASS=SuperSecret101`.
2. Deploy a Pod named `db-client` (image `nginx:alpine`) that sets environment variables `DB_USER` and `DB_PASS` from `db-credentials`.

### Task 4: Sentinel DaemonSet
In namespace `w8d4-exam`:
1. Deploy a DaemonSet named `node-sentinel` using image `busybox:1.36` running `["sleep", "3600"]`.
2. Ensure sentinel pods run on every worker node.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d4-cka
```
