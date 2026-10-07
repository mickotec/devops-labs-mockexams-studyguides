# [CKA W7D5-CKA] Network Policies Deep Dive

**Date:** 2026-11-13  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Default-Deny Ingress Policy
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `default-deny-ingress` that selects all pods (`podSelector: {}`) and denies all incoming ingress traffic.

### Task 2: Allow Frontend to Backend
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `allow-fe-to-be`:
- `podSelector`: matching pods with label `role: backend`
- Ingress allowed only from pods labeled `role: frontend` on TCP port `80`.

### Task 3: Allow Backend to Database
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `allow-be-to-db`:
- `podSelector`: matching pods with label `role: db`
- Ingress allowed only from pods labeled `role: backend` on TCP port `5432`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d5-cka
```
