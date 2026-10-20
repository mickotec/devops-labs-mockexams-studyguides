# [CKAD W4D3-CKAD] Startup Probes for Slow Initialization Workloads

**Date:** 2026-11-04  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Shield Slow Boot with Startup Probe
1. In namespace `ckad-w4d3`, deploy Pod `slow-boot-app` with image `busybox:1.36`.
2. The container takes 20 seconds to initialize before creating `/tmp/initialized`:
   `command: ["sh", "-c", "sleep 20 && touch /tmp/initialized && sleep 3600"]`
3. Configure a Startup Probe:
   - Exec command: `cat /tmp/initialized`
   - `failureThreshold`: `15`
   - `periodSeconds`: `3`
4. Configure a Liveness Probe:
   - Exec command: `cat /tmp/initialized`
   - `periodSeconds`: `5`
5. Verify that the startup probe prevents premature liveness kills and the pod enters `Running` state cleanly.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d3-ckad
```
