# [CKA W4D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-backend
  namespace: w4d4-scale
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-backend
  template:
    metadata:
      labels:
        app: order-backend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 128Mi
```
`kubectl apply -f order-backend.yaml`

2. Create HPA:
`kubectl autoscale deployment order-backend -n w4d4-scale --cpu-percent=50 --min=2 --max=6 --name=order-backend-hpa`
