# [CKAD W2D5-CKAD] SecurityContexts, Non-Root & Linux Capabilities

**Date:** 2026-10-23  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Secure Container Execution Context
1. In namespace `ckad-w2d5`, create a secure Pod named `locked-container` using image `nginx:alpine`.
2. Configure Pod and Container SecurityContexts to enforce:
   - Pod level: `runAsUser: 2000`, `runAsGroup: 2000`, `runAsNonRoot: true`
   - Container level: `readOnlyRootFilesystem: true`
   - Container capabilities: drop `ALL`, add `NET_BIND_SERVICE`
3. Because the root filesystem is read-only, mount an `emptyDir` volume at `/var/cache/nginx`, `/var/run`, and `/tmp` so Nginx can write runtime PID and cache files.
4. Verify that `locked-container` achieves `Running` status (1/1 Ready).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d5-ckad
```
