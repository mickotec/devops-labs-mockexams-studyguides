# [CKAD W3D2-CKAD] Multi-Container Pods: Adapter Pattern

**Date:** 2026-10-27  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Normalize Metrics via Adapter
1. In namespace `ckad-w3d2`, create Pod `metric-adapter-pod`.
2. Main container named `app`:
   - Image: `busybox:1.36`
   - Writes raw metrics `cpu_usage: 42` to `/var/metrics/system.raw` every 2 seconds.
   - Mount volume `metrics-vol` at `/var/metrics`.
3. Adapter container named `adapter`:
   - Image: `busybox:1.36`
   - Mounts `metrics-vol` at `/var/metrics`.
   - Reads `/var/metrics/system.raw` and formats it into Prometheus format `node_cpu_usage 42` written to `/var/metrics/metrics.prom`.
4. Verify both containers run and `/var/metrics/metrics.prom` contains `node_cpu_usage`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d2-ckad
```
