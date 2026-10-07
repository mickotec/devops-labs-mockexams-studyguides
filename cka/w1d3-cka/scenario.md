# [CKA W1D3-CKA] Pod Internals & YAML Architecture

**Date:** 2026-09-16  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Namespace `fintech`
Create a namespace named `fintech`.

### Task 2: Fix the Broken Manifest & Deploy
1. Inspect `/opt/k8s-manifests/broken-app.yaml` on `controlplane`.
2. Fix all syntax, schema, and indentation errors:
   - Pod Name: `transaction-processor`
   - Namespace: `fintech`
   - Container Name: `processor`
   - Image: `nginx:1.25-alpine`
   - Environment variables: `MAX_WORKERS=8` and `CACHE_DIR=/tmp/cache`
   - Container Ports: `8080` (name: `http`) and `9090` (name: `metrics`)
   - Resource limits: memory `128Mi`, CPU `200m`
   - Readiness probe: HTTP GET `/` on port `80` (nginx default) with `initialDelaySeconds: 5`
3. Apply the fixed manifest and ensure `transaction-processor` is in `Running` (1/1 Ready) state.

### Task 3: Imperative Pod with Command Override
1. Imperatively generate a pod named `event-streamer` in namespace `fintech`.
2. The pod must use image `busybox:1.36`.
3. Override its command so it executes:
   `["sh", "-c", "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"]`
4. Verify that `event-streamer` is `Running` and actively appending to `/tmp/stream.log`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d3-cka
```
