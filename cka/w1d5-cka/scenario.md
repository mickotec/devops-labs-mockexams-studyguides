# [CKA W1D5-CKA] Fast Imperative CLI Mastery with Kubectl

**Date:** 2026-09-18  
**Time Limit:** 25m  
**Difficulty:** Medium (Speed Drill)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Terminal Supercharger Configuration
On `controlplane`, configure the environment in `~/.bashrc`:
1. Alias `k=kubectl` with completion: `alias k=kubectl` and `complete -o default -F __start_kubectl k`
2. Shorthand export variables:
   - `export do="--dry-run=client -o yaml"`
   - `export now="--force --grace-period=0"`
3. Configure `~/.vimrc` with:
   - `set tabstop=2`
   - `set shiftwidth=2`
   - `set expandtab`

### Task 2: High-Speed Imperative Resource Creation
Without writing YAML files from scratch, imperatively deploy in namespace `speed-drill`:
1. Deployment `cache-redis`: 3 replicas, image `redis:7-alpine`.
2. ClusterIP service `cache-service`: exposing deployment `cache-redis` on port `6379`.
3. Secret `redis-secret`: with key `auth=supersecret`.

### Task 3: Declarative Clean Export
Export the `cache-redis` deployment manifest to `/opt/k8s/clean-cache.yaml` stripped of cluster runtime fields (`status`, `managedFields`, `creationTimestamp`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d5-cka
```
