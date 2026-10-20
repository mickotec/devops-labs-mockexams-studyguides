# [CKAD W2D1-CKAD] Container Commands & Arguments Execution

**Date:** 2026-10-19  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Override Container Entrypoint & Arguments
1. In namespace `ckad-w2d1`, create a Pod named `report-worker` running image `busybox:1.36`.
2. Configure the container to override the default command and arguments:
   - `command`: `["/bin/sh"]`
   - `args`: `["-c", "mkdir -p /tmp/reports && while true; do date >> /tmp/reports/output.txt; sleep 3; done"]`
3. Ensure the pod transitions to `Running` state and `/tmp/reports/output.txt` is populated.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d1-ckad
```
