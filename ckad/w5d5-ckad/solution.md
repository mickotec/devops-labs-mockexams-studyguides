# [CKAD W5D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Canary Deployment
```bash
ssh controlplane 'cat << "EOF_DEPLOY" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: catalog-canary
  namespace: ckad-w5d5
spec:
  replicas: 1
  selector:
    matchLabels:
      app: catalog
      track: canary
  template:
    metadata:
      labels:
        app: catalog
        track: canary
    spec:
      containers:
      - name: web
        image: nginx:1.25-alpine
EOF_DEPLOY
'
```
