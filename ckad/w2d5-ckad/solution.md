# [CKAD W2D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: SecurityContexts
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: locked-container
  namespace: ckad-w2d5
spec:
  securityContext:
    runAsUser: 2000
    runAsGroup: 2000
    runAsNonRoot: true
  volumes:
  - name: cache-vol
    emptyDir: {}
  - name: run-vol
    emptyDir: {}
  - name: tmp-vol
    emptyDir: {}
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
        add: ["NET_BIND_SERVICE"]
    volumeMounts:
    - name: cache-vol
      mountPath: /var/cache/nginx
    - name: run-vol
      mountPath: /var/run
    - name: tmp-vol
      mountPath: /tmp
EOF_POD
'
```
