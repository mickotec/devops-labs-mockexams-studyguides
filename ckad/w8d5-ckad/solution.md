# [CKAD W8D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: CKAD killer.sh Mock Exam 1 (Timed Simulation)
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=mock-ckad-1 -n ckad-w8d5

# 3. Check status:
kubectl get pods -n ckad-w8d5
```
