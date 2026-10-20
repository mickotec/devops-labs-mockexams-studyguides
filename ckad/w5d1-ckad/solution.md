# [CKAD W5D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Liveness Probes: HTTP, Command & TCP Checks
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d1

# 3. Check status:
kubectl get pods -n ckad-w5d1
```
