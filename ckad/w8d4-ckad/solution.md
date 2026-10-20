# [CKAD W8D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: API Deprecations
```bash
ssh controlplane 'cat << "EOF_FIX" > /tmp/deprecated-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: legacy-ingress
  namespace: ckad-w8d4
spec:
  rules:
  - host: legacy.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-svc
            port:
              number: 80
EOF_FIX
kubectl apply -f /tmp/deprecated-ingress.yaml
'
```
