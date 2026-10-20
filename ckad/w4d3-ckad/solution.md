# [CKAD W4D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Startup Probes
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: slow-boot-app
  namespace: ckad-w4d3
spec:
  containers:
  - name: slow-app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 20 && touch /tmp/initialized && sleep 3600"]
    startupProbe:
      exec:
        command:
        - cat
        - /tmp/initialized
      failureThreshold: 15
      periodSeconds: 3
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/initialized
      periodSeconds: 5
EOF_POD
'
```
