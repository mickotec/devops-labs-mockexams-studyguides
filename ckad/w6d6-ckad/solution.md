# [CKAD W6D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Ingress Rewrite-Target
```bash
ssh controlplane 'cat << "EOF_ING" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-rewrite-ingress
  namespace: ckad-w6d6
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - http:
      paths:
      - path: /api(/|$)(.*)
        pathType: ImplementationSpecific
        backend:
          service:
            name: service-api
            port:
              number: 80
EOF_ING
'
```
