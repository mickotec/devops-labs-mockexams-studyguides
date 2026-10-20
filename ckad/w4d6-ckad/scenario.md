# [CKAD W4D6-CKAD] Debugging Pod Exit Codes: 137 OOMKilled & 127 Command

**Date:** 2026-11-07  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Fix OOMKilled Pod (Exit Code 137)
1. In namespace `ckad-w4d6`, pod `memory-hungry` is failing repeatedly with Exit Code 137 (OOMKilled) because its memory limit is set to `20Mi` while the container requires `64Mi`.
2. Inspect the pod and increase `spec.containers[0].resources.limits.memory` to `128Mi` (and requests to `64Mi`).
3. Recreate the pod so that it enters `Running` state without crash looping.

### Task 2: Fix Command Not Found (Exit Code 127)
1. In namespace `ckad-w4d6`, pod `broken-exec` is failing with Exit Code 127 because its command is set to `/usr/local/bin/nonexistent-binary`.
2. Change the command to `["/bin/sh", "-c", "sleep 3600"]`.
3. Verify both pods are in `Running` (1/1 Ready) state.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d6-ckad
```
