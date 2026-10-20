# [CKAD W7D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: emptyDir Memory
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cache-node
  namespace: ckad-w7d1
spec:
  volumes:
  - name: ram-cache
    emptyDir:
      medium: Memory
      sizeLimit: 64Mi
  - name: host-logs
    hostPath:
      path: /var/log
      type: Directory
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: ram-cache
      mountPath: /cache
    - name: host-logs
      mountPath: /node-logs
      readOnly: true
EOF_POD
'
```
