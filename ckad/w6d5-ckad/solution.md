# [CKAD W6D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Ingress Routing
```bash
ssh controlplane 'cat << "EOF_ING" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ecommerce-ingress
  namespace: ckad-w6d5
spec:
  rules:
  - host: store.internal
    http:
      paths:
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: orders-svc
            port:
              number: 8080
      - path: /catalog
        pathType: Prefix
        backend:
          service:
            name: catalog-svc
            port:
              number: 8080
EOF_ING
'
```
