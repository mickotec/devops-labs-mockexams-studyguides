# [CKAD W5D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Rollback Strategies
```bash
ssh controlplane '
kubectl rollout undo deployment/checkout-api -n ckad-w5d3
kubectl rollout status deployment/checkout-api -n ckad-w5d3
'
```
