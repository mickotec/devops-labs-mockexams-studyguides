# [CKA W5D5-CKA] TLS Basics & PKI in Kubernetes

**Date:** 2026-10-30  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Check Certificate Expiration
On `controlplane`:
1. Check expiration dates of all control plane certificates using `kubeadm certs check-expiration`.
2. Save the output table to `/opt/k8s/certs_expiration.txt`.

### Task 2: Extract API Server SANs
Inspect `/etc/kubernetes/pki/apiserver.crt` using `openssl x509`:
- Extract all Subject Alternative Names (DNS names and IP addresses).
- Save the names to `/opt/k8s/apiserver_sans.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d5-cka
```
