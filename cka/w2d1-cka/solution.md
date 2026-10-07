# [CKA W2D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Fix `/opt/k8s/replicaset-broken.yaml`:
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
      tier: frontend
  template:
    metadata:
      labels:
        app: web-app
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
```
`kubectl apply -f /opt/k8s/replicaset-broken.yaml`

2. Delete pods to observe self-healing:
`kubectl delete pod -n core -l app=web-app --now`

3. Scale to 6 replicas:
`kubectl scale rs web-replicas -n core --replicas=6`
