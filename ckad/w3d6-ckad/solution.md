# [CKAD W3D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: NodeAffinity
```bash
ssh controlplane '
# 1. Label node02:
kubectl label nodes node02 storage-tier=nvme --overwrite

# 2. Deploy pod with nodeAffinity:
cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: fast-io-worker
  namespace: ckad-w3d6
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: storage-tier
            operator: In
            values:
            - nvme
  containers:
  - name: redis
    image: redis:alpine
EOF_POD
'
```
