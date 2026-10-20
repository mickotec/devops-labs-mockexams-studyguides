# [CKAD W6D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Headless Services & StatefulSets Architecture
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=redis:alpine -n ckad-w6d2

# 3. Check status:
kubectl get pods -n ckad-w6d2
```
