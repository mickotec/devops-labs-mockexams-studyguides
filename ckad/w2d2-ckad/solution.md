# [CKAD W2D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ConfigMaps from Literals, Files & Env Injection
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=alpine:3.19 -n ckad-w2d2

# 3. Check status:
kubectl get pods -n ckad-w2d2
```
