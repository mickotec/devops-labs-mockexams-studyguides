# [CKAD W7D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: PersistentVolumeClaims
```bash
ssh controlplane 'cat << "EOF_PVC" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-storage-pvc
  namespace: ckad-w7d3
spec:
  storageClassName: manual-target
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF_PVC
'
```
