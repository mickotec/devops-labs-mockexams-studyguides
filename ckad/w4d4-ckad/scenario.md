# [CKAD W4D4-CKAD] Multi-Container Logging & Crash Log Extraction

**Date:** 2026-11-05  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Extract Previous Crash Logs
1. In namespace `ckad-w4d4`, inspect multi-container pod `microservice-pod`.
2. Container `database-sync` crashed and restarted.
3. Extract the crash logs of the previous terminated instance of container `database-sync` using `kubectl logs ... --previous`.
4. Filter out lines containing `"FATAL"` and save them to `/tmp/fatal-sync.log` on node `controlplane`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d4-ckad
```
