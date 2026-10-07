# [CKA W6D6-CKA] Security & Storage Lab Triathlon

**Date:** 2026-11-07  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 6)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 6 Triathlon Tasks:
In namespace `w6-milestone`:
1. **ServiceAccount & RBAC**:
   Create a ServiceAccount `vault-operator`.
   Create a Role `secret-reader` granting `get, list` on `secrets`.
   Bind `secret-reader` to `vault-operator` via RoleBinding `bind-secret-reader`.

2. **Persistent Storage**:
   Create a PersistentVolume `m6-pv` (150Mi, hostPath: `/tmp/m6-pv`, storageClassName: `fast-storage`).
   Create a PersistentVolumeClaim `m6-pvc` in `w6-milestone` (requesting 100Mi, storageClassName: `fast-storage`).

3. **Hardened Storage Pod**:
   Deploy Pod `vault-pod` in `w6-milestone` (image: `busybox:1.36`):
   - ServiceAccount: `vault-operator`
   - SecurityContext: `runAsUser: 10001`
   - Mount `m6-pvc` at `/data`
   - Command: `sh -c "echo Milestone6Complete > /data/flag.txt && sleep 3600"`

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d6-cka
```
