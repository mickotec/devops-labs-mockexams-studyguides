# [CKAD W6D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: NetworkPolicy: Egress Lockdown & DNS Resolution
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w6d4

# 3. Check status:
kubectl get pods -n ckad-w6d4
```
