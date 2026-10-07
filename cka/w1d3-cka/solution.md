# [CKA W1D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create namespace:
`kubectl create namespace fintech`

2. Fix `/opt/k8s-manifests/broken-app.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: transaction-processor
  namespace: fintech
spec:
  containers:
  - name: processor
    image: nginx:1.25-alpine
    env:
    - name: MAX_WORKERS
      value: "8"
    - name: CACHE_DIR
      value: "/tmp/cache"
    ports:
    - name: http
      containerPort: 8080
    - name: metrics
      containerPort: 9090
    resources:
      limits:
        memory: "128Mi"
        cpu: "200m"
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
```
Apply: `kubectl apply -f /opt/k8s-manifests/broken-app.yaml`

3. Deploy event-streamer:
```bash
kubectl run event-streamer -n fintech --image=busybox:1.36 --restart=Always -- \
  sh -c "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"
```
