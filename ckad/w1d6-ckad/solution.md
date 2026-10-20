# [CKAD W1D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Imperative CLI & JSONPath
```bash
ssh controlplane '
# 1. Imperatively create pod:
kubectl run imperative-pod --image=redis:7-alpine -n ckad-w1d6 --port=6379 -l tier=cache

# 2. Extract Pod IP:
kubectl wait --for=condition=Ready pod/target-alpha -n ckad-w1d6 --timeout=30s 2>/dev/null || true
kubectl get pod target-alpha -n ckad-w1d6 -o jsonpath="{.status.podIP}" > /tmp/alpha-ip.txt

# 3. Explain query:
kubectl explain pod.spec.terminationGracePeriodSeconds > /tmp/explain.txt
'
```
