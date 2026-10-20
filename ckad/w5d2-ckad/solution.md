# [CKAD W5D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Rolling Updates
```bash
ssh controlplane '
kubectl patch deployment payment-gateway -n ckad-w5d2 --type="strategic" -p "{\"spec\":{\"strategy\":{\"rollingUpdate\":{\"maxSurge\":2,\"maxUnavailable\":0}}}}"
kubectl set image deployment/payment-gateway nginx=nginx:1.25-alpine -n ckad-w5d2
kubectl scale deployment payment-gateway --replicas=5 -n ckad-w5d2
kubectl rollout status deployment/payment-gateway -n ckad-w5d2
'
```
