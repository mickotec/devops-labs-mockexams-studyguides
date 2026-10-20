# [CKAD W8D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Helm Release Management
```bash
ssh controlplane '
helm install frontend-app /tmp/sample-chart -n ckad-w8d5 --set replicaCount=3
helm list -n ckad-w8d5
'
```
