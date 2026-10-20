# [CKAD W1D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Editing Pods
```bash
# 1. Export pod spec to yaml:
ssh controlplane '
kubectl get pod data-worker -n ckad-w1d2 -o yaml > /tmp/worker.yaml

# 2. Update command and args in /tmp/worker.yaml and replace:
cat << "EOF_POD" > /tmp/worker.yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-worker
  namespace: ckad-w1d2
spec:
  containers:
  - name: data-worker
    image: busybox:1.36
    command: ["/bin/sh"]
    args: ["-c", "while true; do date >> /tmp/processed.log; sleep 2; done"]
EOF_POD

kubectl replace --force -f /tmp/worker.yaml
'
```
