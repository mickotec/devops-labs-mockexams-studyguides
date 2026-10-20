# [CKAD W5D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Labels & Selectors
```bash
ssh controlplane '
# 1. Query matching pods:
kubectl get pods -n ckad-w5d1 -l "tier in (backend, cache), env!=dev" -o jsonpath="{.items[*].metadata.name}" | tr " " "
" > /tmp/matched-pods.txt

# 2. Apply annotation:
kubectl annotate pods -n ckad-w5d1 -l "tier in (backend, cache), env!=dev" release.version=v3.2
'
```
