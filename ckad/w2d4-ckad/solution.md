# [CKAD W2D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Secrets & Restricted Modes
```bash
ssh controlplane '
kubectl create secret generic api-credentials -n ckad-w2d4   --from-literal=api-key=secret-alpha-9988   --from-literal=api-token=token-beta-7766

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: auth-consumer
  namespace: ckad-w2d4
spec:
  volumes:
  - name: secret-vol
    secret:
      secretName: api-credentials
      defaultMode: 0400
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: secret-vol
      mountPath: /etc/api-keys
EOF_POD
'
```
