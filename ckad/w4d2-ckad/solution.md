# [CKAD W4D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Liveness Probes
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: health-monitor
  namespace: ckad-w4d2
spec:
  containers:
  - name: monitor
    image: busybox:1.36
    command: ["sh", "-c", "touch /tmp/healthy && sleep 3600"]
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5
EOF_POD
'
```
