# [CKAD W1D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Advanced Output Formatting with JSONPath
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=kube-system pods -n ckad-w1d4

# 3. Check status:
kubectl get pods -n ckad-w1d4
```
