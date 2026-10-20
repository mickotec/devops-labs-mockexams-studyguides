# [CKAD W1D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ReplicaSet & Label Selectors
```bash
# 1. Update labels on orphan-web:
ssh controlplane '
kubectl label pod orphan-web -n ckad-w1d3 tier=web

# 2. Create ReplicaSet manifest:
cat << "EOF_RS" | kubectl apply -f -
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend-rs
  namespace: ckad-w1d3
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
      tier: web
  template:
    metadata:
      labels:
        app: frontend
        tier: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
EOF_RS
'
```
