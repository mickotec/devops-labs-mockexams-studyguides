# [CKAD W4D5-CKAD] Workload Monitoring with Metrics Server (kubectl top)

**Date:** 2026-11-06  
**Time Limit:** 20m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Identify Highest Resource Consumer
1. In namespace `kube-system`, several core cluster workloads are running.
2. Using `kubectl top pod -n kube-system --sort-by=cpu`, identify the pod currently consuming the highest CPU.
3. Save the name of that highest CPU pod into `/tmp/top-cpu-pod.txt` on node `controlplane`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d5-ckad
```
