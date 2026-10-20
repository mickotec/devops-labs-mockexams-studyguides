# [CKAD W4D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Batch Jobs: Completions, Parallelism & Retries
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d4

# 3. Check status:
kubectl get pods -n ckad-w4d4
```
