# [CKAD W5D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Container Logging: Multi-Container & Previous Logs
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w5d4

# 3. Check status:
kubectl get pods -n ckad-w5d4
```
