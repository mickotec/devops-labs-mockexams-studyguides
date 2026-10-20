# [CKAD W2D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ServiceAccounts & Token Auto-mount Policies
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d5

# 3. Check status:
kubectl get pods -n ckad-w2d5
```
