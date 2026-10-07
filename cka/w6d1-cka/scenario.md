# [CKA W6D1-CKA] Certificates API & KubeConfig Management

**Date:** 2026-11-02  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: CertificateSigningRequest (CSR)
On `controlplane`, a certificate request file has been prepared at `/opt/k8s/developer-bob.csr`.
1. Create a Kubernetes `CertificateSigningRequest` named `developer-bob-csr`:
   - `signerName`: `kubernetes.io/kube-apiserver-client`
   - `request`: base64-encoded contents of `/opt/k8s/developer-bob.csr`
   - `usages`: `client auth`

### Task 2: Approve CSR & Export Certificate
1. Approve the request using `kubectl certificate approve developer-bob-csr`.
2. Extract the approved certificate to `/opt/k8s/developer-bob.crt`.

### Task 3: Kubeconfig Configuration
Configure a new user in `/opt/k8s/bob.kubeconfig`:
- Set credentials for `developer-bob` using client certificate `/opt/k8s/developer-bob.crt` and client key `/opt/k8s/developer-bob.key`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w6d1-cka
```
