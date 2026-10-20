# [CKAD W7D1-CKAD] Volumes: emptyDir Memory Cache & hostPath

**Date:** 2026-11-23  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure In-Memory emptyDir Volume
1. In namespace `ckad-w7d1`, deploy Pod `cache-node` with image `busybox:1.36`.
2. Configure an `emptyDir` volume named `ram-cache` with `medium: Memory` and `sizeLimit: 64Mi`.
3. Mount `ram-cache` at `/cache` inside the container.
4. Also mount a `hostPath` volume named `host-logs` at `/node-logs` (path: `/var/log`, type: `Directory`, readOnly: true).
5. Verify `cache-node` runs and `df -T /cache` inside the pod reports `tmpfs`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d1-ckad
```
