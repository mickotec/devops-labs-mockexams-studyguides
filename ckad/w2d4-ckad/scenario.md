# [CKAD W2D4-CKAD] Secrets Management & Restricted File Modes

**Date:** 2026-10-22  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Mount Secret Volume with 0400 Permissions
1. In namespace `ckad-w2d4`, create an Opaque Secret named `api-credentials` containing keys:
   - `api-key`: `secret-alpha-9988`
   - `api-token`: `token-beta-7766`
2. Deploy Pod `auth-consumer` with image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Mount the Secret as a volume at `/etc/api-keys` with file permission mode `0400` (`r--------`).
4. Ensure the file `/etc/api-keys/api-key` is readable and its permission mode is verified.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d4-ckad
```
