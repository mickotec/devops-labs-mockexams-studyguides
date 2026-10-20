# [CKAD W8D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: RBAC: Role & RoleBinding Scoped Authorizations
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=rbac -n ckad-w8d2

# 3. Check status:
kubectl get pods -n ckad-w8d2
```
