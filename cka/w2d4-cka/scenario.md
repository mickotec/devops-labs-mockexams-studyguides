# [CKA W2D4-CKA] Namespaces & DNS Resolution Inside Clusters

**Date:** 2026-10-08  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Multi-Namespace Service Deployment
1. Create namespaces `frontend-ns` and `database-ns`.
2. In `database-ns`, deploy pod `mysql-db` (image: `nginx:alpine` simulating db) with label `app=db`.
3. Expose `mysql-db` as a service named `mysql-svc` in `database-ns` on port `3306` (targetPort: 80).

### Task 2: Cross-Namespace Client Pod
1. In `frontend-ns`, create pod `tester` (image: `busybox:1.36`, command `sleep 3600`).

### Task 3: Cross-Namespace DNS Verification
1. Exec into `tester` and perform an `nslookup` on the fully qualified domain name (FQDN):
   `mysql-svc.database-ns.svc.cluster.local`
2. Save the output of the DNS resolution to `/tmp/dns-record.txt` inside pod `tester`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d4-cka
```
