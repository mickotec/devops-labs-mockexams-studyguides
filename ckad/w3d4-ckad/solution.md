# [CKAD W3D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Init Containers
```bash
ssh controlplane '
# 1. Inspect init container:
kubectl describe pod webapp-gated -n ckad-w3d4

# 2. Deploy dummy backend and expose as mysql-backend:
kubectl run mysql-dummy --image=busybox:1.36 -n ckad-w3d4 --command -- nc -lk -p 3306
kubectl expose pod mysql-dummy -n ckad-w3d4 --name=mysql-backend --port=3306 --target-port=3306

# 3. Check webapp transitions to Running:
kubectl get pod webapp-gated -n ckad-w3d4
'
```
