# [CKA W8D6-CKA] Killer.sh Simulator Marathon (Exam Benchmark)

**Date:** 2026-11-21  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Sidecar Logging Architecture
In namespace `w8d6-benchmark`:
Create Pod `audit-counter` sharing an `emptyDir` volume `log-storage`:
1. Container `counter`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]`, mounting `log-storage` at `/var/log`.
2. Container `sidecar`: image `busybox:1.36`, command `["sh", "-c", "tail -n+1 -f /var/log/counter.log"]`, mounting `log-storage` at `/var/log`.

### Task 2: ETCD Snapshot Backup
On `controlplane`:
1. Create a snapshot backup of etcd at `/opt/k8s/etcd-backup.db` using `etcdctl snapshot save`.
2. Use etcd endpoint `https://127.0.0.1:2379` and certificates:
   - CA: `/etc/kubernetes/pki/etcd/ca.crt`
   - Cert: `/etc/kubernetes/pki/etcd/server.crt`
   - Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 3: Ingress with TLS Termination
In namespace `w8d6-benchmark`:
1. Deploy `frontend` (image `nginx:alpine`, port 80) and expose with ClusterIP service `frontend-svc` on port 80.
2. Generate a TLS secret `benchmark-tls` for hostname `benchmark.k8s.local`.
3. Create Ingress `benchmark-ingress` with `ingressClassName: nginx`:
   - Host: `benchmark.k8s.local`
   - TLS referencing `benchmark-tls`
   - Path `/` (Prefix) pointing to service `frontend-svc` port 80.

### Task 4: Database Network Isolation
In namespace `w8d6-benchmark`:
1. Deploy pod `database` with label `role=db` (image `nginx:alpine`).
2. Create NetworkPolicy `strict-db-policy` that isolates `database` allowing ingress ONLY from pods labeled `role=backend` on TCP port `5432`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d6-cka
```
