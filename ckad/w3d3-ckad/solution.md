# [CKAD W3D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Node Affinity: Required vs Preferred
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d3

# 3. Check status:
kubectl get pods -n ckad-w3d3
```
