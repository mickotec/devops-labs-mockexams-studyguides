# [CKAD W2D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ServiceAccounts
```bash
ssh controlplane '
kubectl create serviceaccount build-deployer -n ckad-w2d6

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: isolated-agent
  namespace: ckad-w2d6
spec:
  serviceAccountName: build-deployer
  automountServiceAccountToken: false
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sleep", "3600"]
EOF_POD
'
```
