# [CKAD W5D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Blue-Green Deployment
```bash
ssh controlplane '
# 1. Deploy portal-green:
cat << "EOF_GREEN" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: portal-green
  namespace: ckad-w5d4
spec:
  replicas: 3
  selector:
    matchLabels:
      app: portal
      version: v2
  template:
    metadata:
      labels:
        app: portal
        version: v2
    spec:
      containers:
      - name: web
        image: nginx:1.25-alpine
EOF_GREEN

kubectl rollout status deployment/portal-green -n ckad-w5d4

# 2. Patch service selector to v2:
kubectl patch svc web-portal -n ckad-w5d4 -p "{"spec":{"selector":{"version":"v2"}}}"
'
```
