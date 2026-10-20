# [CKAD W2D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Container Commands & Arguments
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: report-worker
  namespace: ckad-w2d1
spec:
  containers:
  - name: worker
    image: busybox:1.36
    command: ["/bin/sh"]
    args: ["-c", "mkdir -p /tmp/reports && while true; do date >> /tmp/reports/output.txt; sleep 3; done"]
EOF_POD
'
```
