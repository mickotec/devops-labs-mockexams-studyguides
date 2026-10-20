# [CKAD W7D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Kustomize Basics: Overlays, Patches & Transformers
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=kustomize -n ckad-w7d5

# 3. Check status:
kubectl get pods -n ckad-w7d5
```
