# [CKAD W1D2-CKAD] Editing Pods & Command / Args Overrides

**Date:** 2026-10-13  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Reconfigure Immutable Pod Command
1. In namespace `ckad-w1d2`, there is an existing running pod named `data-worker`.
2. Inspect the pod. Currently, it was started with a command that sleeps indefinitely.
3. Modify `data-worker` so that its container executes:
   - `command`: `["/bin/sh"]`
   - `args`: `["-c", "while true; do date >> /tmp/processed.log; sleep 2; done"]`
4. Since `spec.containers[*].command` is immutable, export the pod to YAML, delete/replace the pod, and ensure the updated pod runs with the new arguments and writes to `/tmp/processed.log`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d2-ckad
```
