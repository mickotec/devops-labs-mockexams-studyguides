# [CKA W2D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Multi-port ClusterIP:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-internal
  namespace: prod
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 443
```
`kubectl apply -f api-internal.yaml`

2. NodePort:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-public
  namespace: prod
spec:
  type: NodePort
  selector:
    app: api
  ports:
  - port: 80
    targetPort: 80
    nodePort: 31200
```
`kubectl apply -f web-public.yaml`
