# [CKAD W4D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: kubectl top
```bash
ssh controlplane '
kubectl top pod -n kube-system --sort-by=cpu --no-headers | head -n 1 | awk "{print \$1}" > /tmp/top-cpu-pod.txt
cat /tmp/top-cpu-pod.txt
'
```
