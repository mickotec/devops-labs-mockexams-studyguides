# [CKAD W6D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Headless Service
```bash
ssh controlplane '
kubectl run db-node-0 --image=redis:alpine -n ckad-w6d2 -l app=database
kubectl run db-node-1 --image=redis:alpine -n ckad-w6d2 -l app=database

cat << "EOF_HL" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: db-headless
  namespace: ckad-w6d2
spec:
  clusterIP: None
  selector:
    app: database
  ports:
  - port: 6379
    targetPort: 6379
EOF_HL
'
```
