# [CKAD W3D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Ambassador Pattern
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: client-ambassador
  namespace: ckad-w3d3-apps
spec:
  containers:
  - name: client
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - while true; do
        if nc -z localhost 6379; then
          echo "AMBASSADOR_CONNECTED" > /tmp/proxy.log;
        fi;
        sleep 2;
      done
  - name: ambassador
    image: busybox:1.36
    command: ["sh", "-c", "nc -lk -p 6379 -e nc redis-svc.ckad-w3d3-infra.svc.cluster.local 6379"]
EOF_POD
'
```
