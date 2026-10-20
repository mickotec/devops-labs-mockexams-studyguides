# [CKAD W4D2-CKAD] Liveness Probes & Automated Container Healing

**Date:** 2026-11-03  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Configure Exec Liveness Probe
1. In namespace `ckad-w4d2`, deploy Pod `health-monitor` running image `busybox:1.36`.
2. The container must touch `/tmp/healthy` at startup and sleep indefinitely:
   `command: ["sh", "-c", "touch /tmp/healthy && sleep 3600"]`
3. Configure an Exec liveness probe checking `cat /tmp/healthy`:
   - `initialDelaySeconds`: `5`
   - `periodSeconds`: `5`
4. Verify that `health-monitor` runs continuously without restarting.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d2-ckad
```
