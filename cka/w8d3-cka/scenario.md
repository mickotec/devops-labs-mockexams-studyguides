# [CKA W8D3-CKA] JSONPath Queries & Lightning Labs 1 & 2

**Date:** 2026-11-18  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Node Names Extraction
1. Use `kubectl get nodes -o jsonpath` to extract the names of all nodes in the cluster.
2. Sort the names alphabetically, one per line, and save them to `/opt/k8s/node_names.txt`.

### Task 2: System Container Images Extraction
1. Extract all unique container image names running across all pods in the `kube-system` namespace.
2. Sort the list uniquely and save to `/opt/k8s/kube_system_images.txt`.

### Task 3: Custom Columns Pod Mapping
1. Query pods in namespace `w8d3-json` using custom columns formatted as `NAME:.metadata.name,NODE:.spec.nodeName`.
2. Save the output to `/opt/k8s/pod_node_mapping.txt`.

### Task 4: Lightning Challenge
In namespace `w8d3-lightning`:
1. Deploy a Pod named `fast-pod` using image `redis:alpine` with label `app=fast-cache`.
2. Expose `fast-pod` with a ClusterIP service named `fast-svc` on port `6379`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d3-cka
```
