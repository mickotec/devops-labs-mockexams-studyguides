# [CKAD W5D1-CKAD] Labels, Set-Based Selectors & Annotations

**Date:** 2026-11-09  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Filter Pods & Apply Metadata
1. In namespace `ckad-w5d1`, there are several pods with various labels.
2. Filter the pods using set-based selector syntax for:
   `tier in (backend, cache), env!=dev`
3. Save the names of all matching pods to `/tmp/matched-pods.txt` on node `controlplane`.
4. Add the annotation `release.version=v3.2` to all matching pods in namespace `ckad-w5d1`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d1-ckad
```
