# [CKAD W6D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Default Deny Ingress
```bash
ssh controlplane 'cat << "EOF_NP" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: ckad-w6d3
spec:
  podSelector: {}
  policyTypes:
  - Ingress
EOF_NP
'
```
