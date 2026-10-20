# [CKAD W5D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Week 5 Milestone: Comprehensive Health & Triage Suite
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d6

# 3. Check status:
kubectl get pods -n ckad-w5d6
```
