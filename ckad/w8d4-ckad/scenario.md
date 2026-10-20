# [CKAD W8D4-CKAD] API Versions & Deprecations Migration

**Date:** 2026-12-03  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Migrate Deprecated Ingress Manifest
1. On node `controlplane`, an outdated manifest exists at `/tmp/deprecated-ingress.yaml` written against `extensions/v1beta1`.
2. Convert the manifest to the current stable API version `networking.k8s.io/v1`:
   - Change `apiVersion` to `networking.k8s.io/v1`
   - Update path syntax to include `pathType: Prefix`
   - Update backend specification to `service: {name: web-svc, port: {number: 80}}`
3. Apply the updated manifest into namespace `ckad-w8d4` and verify it creates successfully.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d4-ckad
```
