# [CKA W4D6-CKA] Week 4 App Lifecycle & Secret Security Drill

**Date:** 2026-10-24  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 4)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 4 Triathlon Tasks:
In namespace `w4-milestone`:
1. **ConfigMap & Secret Injection**:
   Create a ConfigMap `app-settings` with `APP_MODE=production`.
   Create a Secret `app-auth` with `API_KEY=Alpha99SecretToken`.
   Deploy a deployment `secure-frontend` (2 replicas, image `nginx:alpine`):
   - Inject `APP_MODE` as an env var from ConfigMap `app-settings`.
   - Inject `API_KEY` as an env var from Secret `app-auth`.
   - Set container resource requests: `cpu: 30m`, `memory: 64Mi`.

2. **Horizontal Pod Autoscaling**:
   Configure an HPA named `secure-frontend-hpa` targeting `secure-frontend`:
   - Min replicas: `2`, Max replicas: `5`, Target CPU: `60%`.

3. **Secret File Volume**:
   Mount Secret `app-auth` inside the container as a file at `/etc/auth/token` (read-only, defaultMode: `0400`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d6-cka
```
