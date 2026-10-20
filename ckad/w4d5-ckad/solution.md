# [CKAD W4D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: CronJobs: Schedule Syntax & Concurrency Policies
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d5

# 3. Check status:
kubectl get pods -n ckad-w4d5
```
