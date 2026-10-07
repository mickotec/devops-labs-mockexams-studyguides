# [CKA W4D3-CKA] Secrets Management & Encryption at Rest

**Date:** 2026-10-21  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Generic Secret
In namespace `w4d3-secrets`, create a generic Secret named `db-credentials`:
- Key `username`: `dbadmin`
- Key `password`: `S3cur3P@ssw0rd!`

### Task 2: Mount Secret as Read-Only File Volume
Deploy a Pod named `vault-agent` in namespace `w4d3-secrets` (image: `nginx:alpine`):
- Mount the Secret `db-credentials` as a volume at `/etc/vault/secrets`
- Set `defaultMode: 256` (octal `0400` read-only for owner)
- Verify the pod runs and `/etc/vault/secrets/password` exists with the decrypted content.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d3-cka
```
