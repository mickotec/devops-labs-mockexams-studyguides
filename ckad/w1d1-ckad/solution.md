# [CKAD W1D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Multi-Container Pod
```bash
# 1. Edit /tmp/webapp-core.yaml on controlplane:
# Fix the volumeMount name in container 'log-shipper' to match 'shared-logs':
ssh controlplane 'cat << "EOF_FIX" > /tmp/webapp-core.yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp-core
  namespace: ckad-w1d1
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: web-app
    image: nginx:1.24-alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
  - name: log-shipper
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
EOF_FIX
kubectl apply -f /tmp/webapp-core.yaml
'
```
