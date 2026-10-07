# [CKA W4D2-CKA] ConfigMaps & Application Configuration

**Date:** 2026-10-20  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create ConfigMaps
In namespace `w4d2-config`:
1. Create a ConfigMap named `backend-config` from literals:
   - `DB_HOST=postgres.internal`
   - `DB_PORT=5432`
2. Create a ConfigMap named `ui-settings` from file `/opt/k8s/settings.json`.

### Task 2: Consume ConfigMaps via envFrom and Volume Mount
Deploy a Pod named `portal-app` in namespace `w4d2-config` (image: `nginx:alpine`):
- Inject all keys from `backend-config` as environment variables using `envFrom`.
- Mount `ui-settings` as a volume at `/etc/portal/config/` (read-only).
- Verify the pod runs and the configuration file is present at `/etc/portal/config/settings.json`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d2-cka
```
