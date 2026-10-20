# [CKAD W8D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: CKAD killer.sh Mock Exam 2 (Timed Simulation)
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=mock-ckad-2 -n ckad-w8d6

# 3. Check status:
kubectl get pods -n ckad-w8d6
```
