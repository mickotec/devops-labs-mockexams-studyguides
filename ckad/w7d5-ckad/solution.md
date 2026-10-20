# [CKAD W7D5-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: StorageClasses
```bash
ssh controlplane 'cat << "EOF_SC" | kubectl apply -f -
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: delayed-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: delayed-pvc
  namespace: ckad-w7d5
spec:
  storageClassName: delayed-storage
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF_SC
'
```
