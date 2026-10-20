# [CKAD W7D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: StatefulSets
```bash
ssh controlplane 'cat << "EOF_STS" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: ckad-w7d6
spec:
  clusterIP: None
  selector:
    app: redis-node
  ports:
  - port: 6379
    targetPort: 6379
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis-cluster
  namespace: ckad-w7d6
spec:
  serviceName: redis-service
  replicas: 2
  selector:
    matchLabels:
      app: redis-node
  template:
    metadata:
      labels:
        app: redis-node
    spec:
      containers:
      - name: redis
        image: redis:alpine
        ports:
        - containerPort: 6379
        volumeMounts:
        - name: redis-data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: redis-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: redis-sc
      resources:
        requests:
          storage: 200Mi
EOF_STS

kubectl rollout status statefulset/redis-cluster -n ckad-w7d6 --timeout=60s 2>/dev/null || true
'
```
