# [CKAD W3D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Taints & Tolerations
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: analytics-engine
  namespace: ckad-w3d5
spec:
  nodeName: node01
  tolerations:
  - key: dedicated
    operator: Equal
    value: analytics
    effect: NoSchedule
  containers:
  - name: engine
    image: nginx:alpine
EOF_POD
'
```
