# [CKAD W3D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Week 3 Milestone: Precision Workload Placement
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d6

# 3. Check status:
kubectl get pods -n ckad-w3d6
```
