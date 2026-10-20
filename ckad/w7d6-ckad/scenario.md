# [CKAD W7D6-CKAD] StatefulSets & VolumeClaimTemplates

**Date:** 2026-11-28  
**Time Limit:** 30m  
**Difficulty:** Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Deploy Clustered StatefulSet
1. In namespace `ckad-w7d6`, create a Headless Service named `redis-service` (`clusterIP: None`) on port `6379`.
2. Deploy a StatefulSet named `redis-cluster`:
   - `serviceName`: `redis-service`
   - Replicas: `2`
   - Image: `redis:alpine`
   - Container port: `6379`
   - `volumeClaimTemplates`: name `redis-data`, accessModes `ReadWriteOnce`, requests `200Mi`, mounted at `/data`.
3. Verify both replicas `redis-cluster-0` and `redis-cluster-1` are `Running` and both generate their own PVC.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d6-ckad
```
