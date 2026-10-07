# [CKA W1D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create namespace:
`kubectl create namespace telemetry`

2. Deploy `order-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: order-service
  namespace: telemetry
spec:
  volumes:
  - name: log-volume
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
  - name: logger
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
      readOnly: true
```

3. Deploy `web-portal`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-portal
  namespace: telemetry
spec:
  volumes:
  - name: data-vol
    emptyDir: {}
  initContainers:
  - name: db-wait
    image: busybox:1.36
    command: ["sh", "-c", "echo ready > /opt/data/ready.flag"]
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
  containers:
  - name: web
    image: nginx:1.25-alpine
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
```
