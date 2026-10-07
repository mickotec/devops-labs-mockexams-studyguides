# [CKA W7D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create Gateway manifest `gateway.yaml`:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-gateway
  namespace: w7d4-gw
spec:
  gatewayClassName: cluster-gateway-class
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
```
`kubectl apply -f gateway.yaml`

2. Create HTTPRoute manifest `httproute.yaml`:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: api-route
  namespace: w7d4-gw
spec:
  parentRefs:
  - name: prod-gateway
    sectionName: http
  hostnames:
  - "api.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /v1
    backendRefs:
    - name: api-service
      port: 8080
```
`kubectl apply -f httproute.yaml`
