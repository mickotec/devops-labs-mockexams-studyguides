# [CKA W8D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. PV and PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-marathon-data
spec:
  capacity:
    storage: 2Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data/pv-marathon
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-marathon
  namespace: w8d5-marathon
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
```

2. Label node01 and deploy with NodeAffinity:
`kubectl label node node01 zone=production-a`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zone-app
  namespace: w8d5-marathon
spec:
  replicas: 2
  selector:
    matchLabels:
      app: zone-app
  template:
    metadata:
      labels:
        app: zone-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: zone
                operator: In
                values:
                - production-a
      containers:
      - name: nginx
        image: nginx:alpine
```

3. Taint node02 and deploy special-worker:
`kubectl taint node node02 dedicated=special:NoSchedule`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: special-worker
  namespace: w8d5-marathon
spec:
  nodeName: node02
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special"
    effect: "NoSchedule"
  containers:
  - name: busybox
    image: busybox:1.36
    command: ["sleep", "3600"]
```

4. Rollout and rollback:
```bash
kubectl set image deployment/zone-app nginx=nginx:1.25.5-alpine -n w8d5-marathon
kubectl rollout status deployment/zone-app -n w8d5-marathon
kubectl rollout undo deployment/zone-app -n w8d5-marathon
```
