# [CKA W2D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-app
  namespace: finance
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: payment-app
  template:
    metadata:
      labels:
        app: payment-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
```
`kubectl apply -f payment-app.yaml`

2. Upgrade image and annotate:
```bash
kubectl set image deploy/payment-app nginx=nginx:1.25-alpine -n finance
kubectl annotate deploy/payment-app -n finance kubernetes.io/change-cause="version 1.25 upgrade"
```

3. Broken rollout and undo:
```bash
kubectl set image deploy/payment-app nginx=nginx:does-not-exist -n finance
kubectl rollout undo deploy/payment-app -n finance
```
