# [CKAD W1D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Cross-Namespace DNS
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: query-client
  namespace: ckad-w1d5-frontend
spec:
  containers:
  - name: client
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - while true; do
        if nc -z -w 3 db-service.ckad-w1d5-backend.svc.cluster.local 6379; then
          echo "CONNECTION_SUCCESS" > /tmp/conn.log;
        fi;
        sleep 2;
      done
EOF_POD
'
```
