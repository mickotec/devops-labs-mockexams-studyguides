# [CKA W7D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create `default-deny-ingress`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: w7d5-netpol
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

2. Create `allow-fe-to-be`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-fe-to-be
  namespace: w7d5-netpol
spec:
  podSelector:
    matchLabels:
      role: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 80
```

3. Create `allow-be-to-db`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-be-to-db
  namespace: w7d5-netpol
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
```
