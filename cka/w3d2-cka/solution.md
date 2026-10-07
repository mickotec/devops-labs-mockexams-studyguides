# [CKA W3D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Taint node01:
`kubectl taint node node01 workload=critical:NoSchedule`

2. Deploy `critical-processor`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-processor
  namespace: w3d2-affinity
spec:
  nodeName: node01
  tolerations:
  - key: "workload"
    operator: "Equal"
    value: "critical"
    effect: "NoSchedule"
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f critical-processor.yaml`

3. Deploy `data-collector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-collector
  namespace: w3d2-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f data-collector.yaml`
