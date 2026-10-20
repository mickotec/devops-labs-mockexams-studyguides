# [CKAD W4D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Rolling Updates, Rollout History & Undo/Rollback
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d1

# 3. Check status:
kubectl get pods -n ckad-w4d1
```
