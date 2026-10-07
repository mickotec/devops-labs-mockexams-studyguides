# [CKA W5D6-CKA] Full Disaster Recovery & Upgrade Drill

**Date:** 2026-10-31  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 5)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 5 Triathlon Tasks:
1. **ETCD Cluster Snapshot**:
   Take an etcd snapshot and store it in `/opt/backup/milestone5-etcd.db`.
   Verify the snapshot status with `etcdctl snapshot status`.

2. **Drain and Upgrade Preparation for `node02`**:
   Drain `node02` ignoring daemonsets and deleting emptydir data.
   Confirm that `node02` has `SchedulingDisabled`.

3. **Certificate Auditing**:
   Export all expired or impending certificate warnings to `/opt/k8s/m5_certs_audit.txt` using `kubeadm certs check-expiration`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d6-cka
```
