# [CKA W7D2-CKA] Service Networking & CoreDNS Deep Dive

**Date:** 2026-11-10  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: ClusterIP Service Deployment
In namespace `w7d2-dns`:
1. Deploy a Deployment named `backend-app` with 2 replicas using image `nginx:alpine` (port 80, labels `app=backend-app`).
2. Create a ClusterIP Service named `backend-svc` exposing port `8080` targeting pod port `80`.

### Task 2: NodePort Service Deployment
In namespace `w7d2-dns`:
1. Deploy a Deployment named `frontend-app` with 1 replica using image `nginx:alpine` (port 80, labels `app=frontend-app`).
2. Create a Service named `frontend-nodeport` of type `NodePort` mapping port `80` (targetPort 80) to static `nodePort: 30080`.

### Task 3: CoreDNS Name Resolution Test
1. Run a one-off diagnostic pod `dns-tester` (image `busybox:1.36`, restart policy `Never`) in namespace `w7d2-dns`.
2. Inside the pod, run `nslookup backend-svc.w7d2-dns.svc.cluster.local`.
3. Save the DNS resolution output to `/opt/k8s/dns_resolution.txt` on `controlplane`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d2-cka
```
