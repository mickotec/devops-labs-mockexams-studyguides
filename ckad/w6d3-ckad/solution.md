# [CKAD W6D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: NetworkPolicy: Ingress Isolation & Pod Selectors
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d3

# 3. Check status:
kubectl get pods -n ckad-w6d3
```
