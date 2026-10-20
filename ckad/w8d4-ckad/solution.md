# [CKAD W8D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Custom Resource Definitions (CRDs) & API Extensions
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=crd -n ckad-w8d4

# 3. Check status:
kubectl get pods -n ckad-w8d4
```
