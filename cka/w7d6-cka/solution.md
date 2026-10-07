# [CKA W7D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Deploy services:
```bash
kubectl create deployment web-frontend -n w7d6-triathlon --image=nginx:alpine --replicas=2 --port=80
kubectl expose deployment web-frontend -n w7d6-triathlon --name=frontend-svc --port=80
kubectl create deployment api-backend -n w7d6-triathlon --image=nginx:alpine --replicas=2 --port=80
kubectl expose deployment api-backend -n w7d6-triathlon --name=backend-svc --port=80
```

2. Create TLS Secret and Ingress:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/tls.key -out /tmp/tls.crt -subj "/CN=triathlon.k8s.local"
kubectl create secret tls triathlon-tls -n w7d6-triathlon --cert=/tmp/tls.crt --key=/tmp/tls.key
```
Ingress manifest:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: triathlon-ingress
  namespace: w7d6-triathlon
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - triathlon.k8s.local
    secretName: triathlon-tls
  rules:
  - host: triathlon.k8s.local
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend-svc
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
```

3. NetworkPolicy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-isolation
  namespace: w7d6-triathlon
spec:
  podSelector:
    matchLabels:
      app: api-backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: web-frontend
    ports:
    - protocol: TCP
      port: 80
```
