# [CKAD W2D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Secrets Creation, Base64 & Safe Mounting
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d3

# 3. Check status:
kubectl get pods -n ckad-w2d3
```
