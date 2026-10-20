# [CKAD W6D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Services
```bash
ssh controlplane '
# 1. Deploy workloads:
kubectl create deployment backend-deploy --image=redis:alpine --replicas=2 -n ckad-w6d1
kubectl create deployment frontend-deploy --image=nginx:alpine --replicas=2 -n ckad-w6d1

# 2. Expose backend as ClusterIP:
kubectl expose deployment backend-deploy --name=backend-svc --port=6379 --target-port=6379 -n ckad-w6d1

# 3. Expose frontend as NodePort 30080:
cat << "EOF_NP" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: frontend-svc
  namespace: ckad-w6d1
spec:
  type: NodePort
  selector:
    app: frontend-deploy
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
EOF_NP
'
```
