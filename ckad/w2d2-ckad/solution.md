# [CKAD W2D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ConfigMaps & Env
```bash
ssh controlplane '
kubectl create configmap backend-config -n ckad-w2d2   --from-literal=DB_HOST=postgres.internal   --from-literal=DB_PORT=5432   --from-literal=CACHE_TTL=3600

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: app-server
  namespace: ckad-w2d2
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    env:
    - name: APP_ENV
      value: "production"
    envFrom:
    - configMapRef:
        name: backend-config
EOF_POD
'
```
