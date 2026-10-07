# [CKA W1D6-CKA] Week 1 Integration & Milestone Triathlon

**Date:** 2026-09-19  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 1)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 1 Triathlon Tasks:
1. **Control-Plane Recovery:**
   On `controlplane`, static pod manifests were moved to `/etc/kubernetes/manifests_broken`. Restore them back to `/etc/kubernetes/manifests` and restart kubelet so control-plane static pods recover.
2. **Multi-Tier Workload Pipeline:**
   In namespace `triathlon-w1`:
   - Deploy `web-ui` with 2 replicas, image `nginx:1.25-alpine`, container port 80, CPU limit `150m`, memory limit `128Mi`.
   - Expose via ClusterIP service `web-ui-svc` on port `80`.
3. **ETCD Disaster Recovery Backup:**
   Create an etcd point-in-time snapshot saved to `/opt/backup/triathlon-etcd.db` using TLS credentials.
4. **Worker Static Pod:**
   Deploy a static pod on `node01` named `w1-worker-agent` (image: `busybox:1.36`, command `["sh", "-c", "sleep 3600"]`). Verify it appears in `kubectl get pods -A` as `w1-worker-agent-node01`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d6-cka
```
