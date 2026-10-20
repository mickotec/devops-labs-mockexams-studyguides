# [CKAD W4D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Previous Logs Extraction
```bash
ssh controlplane '
kubectl logs microservice-pod -c database-sync -n ckad-w4d4 --previous | grep -i fatal > /tmp/fatal-sync.log
cat /tmp/fatal-sync.log
'
```
