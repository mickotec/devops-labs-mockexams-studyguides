# [CKAD W6D2-CKAD] Headless Services & Direct Pod Discovery

**Date:** 2026-11-17  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Headless Service for Clustered Pods
1. In namespace `ckad-w6d2`, deploy two pods named `db-node-0` and `db-node-1` with labels `app=database` using image `redis:alpine`.
2. Create a Headless Service named `db-headless` (`clusterIP: None`):
   - Selector: `app=database`
   - Port: `6379`
   - TargetPort: `6379`
3. Verify `clusterIP` is set to `None` and running `nslookup db-headless.ckad-w6d2.svc.cluster.local` returns both pod IPs.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d2-ckad
```
