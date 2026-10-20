# [CKAD W4D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Debugging Exit Codes
```bash
ssh controlplane '
# 1. Fix memory-hungry:
cat << "EOF_MEM" | kubectl replace --force -f -
apiVersion: v1
kind: Pod
metadata:
  name: memory-hungry
  namespace: ckad-w4d6
spec:
  containers:
  - name: mem
    image: busybox:1.36
    command: ["sh", "-c", "head -c 40M </dev/zero | tail -c 40M; sleep 3600"]
    resources:
      limits:
        memory: "128Mi"
      requests:
        memory: "64Mi"
EOF_MEM

# 2. Fix broken-exec:
cat << "EOF_EXEC" | kubectl replace --force -f -
apiVersion: v1
kind: Pod
metadata:
  name: broken-exec
  namespace: ckad-w4d6
spec:
  containers:
  - name: exec
    image: busybox:1.36
    command: ["/bin/sh", "-c", "sleep 3600"]
EOF_EXEC
'
```
