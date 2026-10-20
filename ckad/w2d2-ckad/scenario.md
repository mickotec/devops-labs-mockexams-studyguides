# [CKAD W2D2-CKAD] ConfigMaps & Environment Variable Injections

**Date:** 2026-10-20  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create ConfigMap & Inject via envFrom
1. In namespace `ckad-w2d2`, create a ConfigMap named `backend-config` with keys:
   - `DB_HOST=postgres.internal`
   - `DB_PORT=5432`
   - `CACHE_TTL=3600`
2. Deploy Pod `app-server` using image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Inject ALL keys from `backend-config` into the container using `envFrom.configMapRef`.
4. Also define an individual environment variable named `APP_ENV` with literal value `"production"` directly in `spec.containers[0].env`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d2-ckad
```
