# [CKAD W7D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Helm Fundamentals: Repos, Releases & Values Overrides
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=helm -n ckad-w7d4

# 3. Check status:
kubectl get pods -n ckad-w7d4
```
