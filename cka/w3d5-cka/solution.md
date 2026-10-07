# [CKA W3D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create PriorityClasses:
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: mission-critical
value: 1000000
globalDefault: false
description: "Mission critical applications"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 500
preemptionPolicy: Never
globalDefault: false
```
`kubectl apply -f priorities.yaml`

2. Deploy pods with `priorityClassName`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-db
  namespace: w3d5-priority
spec:
  priorityClassName: mission-critical
  containers:
  - name: nginx
    image: nginx:alpine
---
apiVersion: v1
kind: Pod
metadata:
  name: batch-worker
  namespace: w3d5-priority
spec:
  priorityClassName: low-priority
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f pods.yaml`
