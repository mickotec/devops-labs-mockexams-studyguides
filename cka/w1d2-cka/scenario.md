# [CKA W1D2-CKA] ETCD Fundamentals & Cluster State Store

**Date:** 2026-09-15  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: ETCD Endpoint Health & Member Inspection
1. SSH into `controlplane`.
2. Inspect the static pod manifest `/etc/kubernetes/manifests/etcd.yaml` to identify the client port, CA certificate, cert file, and key file.
3. Using `etcdctl` (with `ETCDCTL_API=3`), query the endpoint health using TLS certificates.
4. Export the endpoint health report to `/opt/backup/etcd-health.txt`.

### Task 2: Create a Validated ETCD Snapshot
1. Create directory `/opt/backup/` on `controlplane` if it does not already exist.
2. Using `etcdctl snapshot save`, save a point-in-time snapshot to `/opt/backup/etcd-snapshot-w1d2.db`.
3. Verify the snapshot using `etcdctl snapshot status --write-out=table`.
4. Ensure the snapshot status output is saved to `/opt/backup/snapshot-status.txt`.

### Task 3: Key Prefix Counting
1. Using `etcdctl get`, query the keys with prefix `/registry/namespaces` to count how many namespaces currently exist in the raw etcd store.
2. Save the count (number only) to `/opt/backup/namespace-count.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d2-cka
```
