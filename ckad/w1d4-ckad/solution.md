# [CKAD W1D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Deployments & Rolling Updates
```bash
ssh controlplane '
kubectl patch deployment api-gateway -n ckad-w1d4 -p "{"spec":{"strategy":{"type":"RollingUpdate","rollingUpdate":{"maxSurge":1,"maxUnavailable":0}}}}"
kubectl set image deployment/api-gateway api-gateway=nginx:1.25-alpine -n ckad-w1d4
kubectl scale deployment api-gateway --replicas=4 -n ckad-w1d4
kubectl rollout status deployment/api-gateway -n ckad-w1d4
'
```
