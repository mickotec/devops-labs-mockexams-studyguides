# [CKA W3D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create LimitRange manifest `limitrange.yaml`:
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: resource-bounds
  namespace: w3d3-resources
spec:
  limits:
  - default:
      cpu: 200m
      memory: 128Mi
    defaultRequest:
      cpu: 100m
      memory: 64Mi
    max:
      cpu: 500m
      memory: 256Mi
    type: Container
```
`kubectl apply -f limitrange.yaml`

2. Deploy `bounded-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bounded-service
  namespace: w3d3-resources
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    resources:
      requests:
        cpu: 150m
        memory: 100Mi
      limits:
        cpu: 300m
        memory: 200Mi
```
`kubectl apply -f bounded-service.yaml`

3. Deploy `unconstrained-pod`:
`kubectl run unconstrained-pod -n w3d3-resources --image=nginx:alpine`
