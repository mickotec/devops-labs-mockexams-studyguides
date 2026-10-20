# [CKAD W1D6-CKAD] Imperative Commands & JSONPath Output Mastery

**Date:** 2026-10-17  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Fast Imperative CLI & Data Extraction
1. In namespace `ckad-w1d6`, imperatively create a pod named `imperative-pod` with image `redis:7-alpine`, label `tier=cache`, and containerPort `6379`.
2. Extract the internal IP address of pod `target-alpha` in namespace `ckad-w1d6` using `kubectl ... -o jsonpath` and save ONLY the IP to `/tmp/alpha-ip.txt` on node `controlplane`.
3. Use `kubectl explain` to check the field name for pod's `terminationGracePeriodSeconds` and append the explanation title to `/tmp/explain.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d6-ckad
```
