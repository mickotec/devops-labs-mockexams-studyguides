# [CKAD W5D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Readiness Probes & Service Traffic Gating
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d2

# 3. Check status:
kubectl get pods -n ckad-w5d2
```
