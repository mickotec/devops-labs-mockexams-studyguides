# [CKAD W3D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Adapter Pattern
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: metric-adapter-pod
  namespace: ckad-w3d2
spec:
  volumes:
  - name: metrics-vol
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'cpu_usage: 42' > /var/metrics/system.raw; sleep 2; done"]
    volumeMounts:
    - name: metrics-vol
      mountPath: /var/metrics
  - name: adapter
    image: busybox:1.36
    command: ["sh", "-c", "while true; do [ -f /var/metrics/system.raw ] && echo 'node_cpu_usage 42' > /var/metrics/metrics.prom; sleep 2; done"]
    volumeMounts:
    - name: metrics-vol
      mountPath: /var/metrics
EOF_POD
'
```
