# [CKAD W6D6-CKAD] Ingress Rewrite-Target & Path Regex

**Date:** 2026-11-21  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure URL Rewrite Annotation
1. In namespace `ckad-w6d6`, deploy backend service `service-api:80`.
2. Create Ingress `api-rewrite-ingress`:
   - Annotation: `nginx.ingress.kubernetes.io/rewrite-target: /$2`
   - Path: `/api(/|$)(.*)` with `pathType: ImplementationSpecific`
   - Backend: `service-api` on port `80`
3. Verify the rewrite-target annotation is active on the Ingress resource.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d6-ckad
```
