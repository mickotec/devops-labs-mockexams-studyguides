# [CKAD W3D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Sidecar Log Streaming
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: app-logger
  namespace: ckad-w3d1
spec:
  volumes:
  - name: log-storage
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'TRANSACTION_ID='$(date +%s%N) >> /var/log/app/tx.log; sleep 2; done"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log/app
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -F /var/log/app/tx.log"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log/app
EOF_POD
'
```
