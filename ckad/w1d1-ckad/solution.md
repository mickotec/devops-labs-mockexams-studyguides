# [CKAD W1D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Multi-Container Pods & Sidecar Logging
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d1

# 3. Check status:
kubectl get pods -n ckad-w1d1
```
