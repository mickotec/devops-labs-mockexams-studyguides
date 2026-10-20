# [CKAD W6D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Fine-Grained NetworkPolicy
```bash
ssh controlplane 'cat << "EOF_NP" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-only
  namespace: ckad-w6d4
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - protocol: TCP
      port: 8080
EOF_NP
'
```
