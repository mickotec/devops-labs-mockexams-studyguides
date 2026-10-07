# [CKA W2D5-CKA] Kubectl Explain & Declarative Workflow

**Date:** 2026-10-09  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Offline Schema Exploration
Using `kubectl explain`, determine the exact YAML paths for:
1. Container securityContext capabilities addition (`spec.containers.securityContext.capabilities.add`).
2. Pod termination grace period (`spec.terminationGracePeriodSeconds`).
Save both paths (one per line) to `/opt/k8s/schema-paths.txt`.

### Task 2: Declarative Manifest Validation
Construct a declarative pod manifest at `/opt/k8s/secure-pod.yaml`:
- Name: `secure-nginx`
- Namespace: `security-lab`
- Image: `nginx:alpine`
- Command: `["sleep", "3600"]`
- SecurityContext:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `readOnlyRootFilesystem: false`
Apply the manifest and confirm `secure-nginx` reaches `Running` state.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d5-cka
```
