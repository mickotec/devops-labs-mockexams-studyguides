# [CKA W3D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create DaemonSet `ds.yaml`:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  namespace: w3d4-ds
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
        tier: monitoring
    spec:
      containers:
      - name: collector
        image: nginx:alpine
```
`kubectl apply -f ds.yaml`

2. On node02:
`ssh node02`
`sudo tee /etc/kubernetes/manifests/node02-telemetry.yaml << 'EOF'`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node02-telemetry
spec:
  containers:
  - name: telemetry
    image: nginx:alpine
```
`EOF`
