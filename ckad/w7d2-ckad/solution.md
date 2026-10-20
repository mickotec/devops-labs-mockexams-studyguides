# [CKAD W7D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: PersistentVolume
```bash
ssh controlplane 'cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-storage-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual-storage
  hostPath:
    path: /mnt/k8s-pv-data
    type: DirectoryOrCreate
EOF_PV
'
```
