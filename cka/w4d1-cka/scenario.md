# [CKA W4D1-CKA] Commands & Arguments (Docker vs Kubernetes)

**Date:** 2026-10-19  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Override Entrypoint with Command
In namespace `w4d1-cmd`, deploy a Pod named `custom-streamer` (image: `busybox:1.36`):
- Override the default entrypoint (`command`): `["/bin/sh", "-c"]`
- Override the arguments (`args`): `["while true; do echo STREAMING_EVENT; sleep 2; done"]`
- Verify the pod runs and streams `STREAMING_EVENT` to its standard output.

### Task 2: Interpolate Environment Variables into Arguments
Deploy a Pod named `env-interpolator` in namespace `w4d1-cmd` (image: `busybox:1.36`):
- Define an environment variable: `CLUSTER_ROLE=processor`
- Set `command`: `["/bin/sh", "-c"]`
- Set `args`: `["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]`
- Confirm that the container stdout shows `Initialized as processor`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d1-cka
```
