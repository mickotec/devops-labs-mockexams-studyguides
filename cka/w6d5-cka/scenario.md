# [CKA W6D5-CKA] Helm & Kustomize (2025 Updates)

**Date:** 2026-11-06  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Kustomize Overlay
On `controlplane`, in directory `/opt/k8s/kustomize/base`:
A base deployment and service exist.
1. Create a `kustomization.yaml` file in `/opt/k8s/kustomize/base` defining:
   - `resources: [deployment.yaml, service.yaml]`
   - `namePrefix: prod-`
   - `commonLabels: env=production, tier=core`

### Task 2: Apply Declarative Kustomize Manifest
In namespace `w6d5-kustomize`:
1. Build and apply the overlay using `kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`.
2. Verify that the deployment `prod-web-server` and service `prod-web-service` are created and running with label `env=production`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d5-cka
```
