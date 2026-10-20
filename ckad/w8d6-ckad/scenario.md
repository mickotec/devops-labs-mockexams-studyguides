# [CKAD W8D6-CKAD] Kustomize: Overlays, Transformers & Patches

**Date:** 2026-12-05  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Build Multi-Environment Kustomize Overlay
1. On node `controlplane`, construct a Kustomize structure under `/tmp/kustomize-store`:
   - `base/deployment.yaml`: Deployment of `nginx:1.24-alpine` (replicas: 1)
   - `base/kustomization.yaml`: referencing `deployment.yaml`
   - `overlays/prod/kustomization.yaml`:
     - `resources`: referencing `../../base`
     - `namePrefix`: `prod-`
     - `commonLabels`: `env: production, tier: web`
     - Patch: increase replicas to `3`
2. Apply the overlay into namespace `ckad-w8d6` using `kubectl apply -k /tmp/kustomize-store/overlays/prod`.
3. Verify that deployment `prod-web-app` runs with 3 replicas and label `env=production`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d6-ckad
```
