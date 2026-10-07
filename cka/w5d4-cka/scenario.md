# [CKA W5D4-CKA] ETCD Snapshot Backup & Disaster Recovery

**Date:** 2026-10-29  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Validated ETCD Snapshot
On `controlplane`, save an etcd snapshot to `/opt/backup/etcd-snapshot-w5.db`:
- Endpoints: `https://127.0.0.1:2379`
- CACert: `/etc/kubernetes/pki/etcd/ca.crt`
- Cert: `/etc/kubernetes/pki/etcd/server.crt`
- Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 2: Verify Snapshot Integrity
Verify the saved snapshot status using `etcdctl snapshot status`:
- Write the status table output to `/opt/backup/etcd_snapshot_status.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d4-cka
```
