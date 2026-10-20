# [CKAD W7D4-CKAD] Consuming PVCs in Pods & Data Persistence

**Date:** 2026-11-26  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Verify Storage Persistence Across Pod Lifecycle
1. In namespace `ckad-w7d4`, PVC `data-claim` is bound to a PersistentVolume.
2. Deploy a Pod named `state-writer`:
   - Image: `busybox:1.36`
   - Mount `data-claim` at `/var/storage`.
   - Command: `sh -c "echo 'PERSISTED_STATE_OK' > /var/storage/state.txt && sleep 3600"`
3. Verify `/var/storage/state.txt` is written.
4. Delete `state-writer`.
5. Deploy a second Pod named `state-reader`:
   - Image: `busybox:1.36`
   - Mount same `data-claim` at `/var/storage`.
   - Command: `sleep 3600`
6. Verify `state-reader` successfully reads `"PERSISTED_STATE_OK"` from `/var/storage/state.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d4-ckad
```
