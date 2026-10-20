# [CKAD W5D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Metrics Server & CLI Resource Monitoring
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=metrics-server -n ckad-w5d5

# 3. Check status:
kubectl get pods -n ckad-w5d5
```
