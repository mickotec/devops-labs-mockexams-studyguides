# [CKAD W7D4-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Data Persistence
```bash
ssh controlplane '
# 1. Run writer pod:
cat << "EOF_WRITER" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: state-writer
  namespace: ckad-w7d4
spec:
  volumes:
  - name: storage-vol
    persistentVolumeClaim:
      claimName: data-claim
  containers:
  - name: writer
    image: busybox:1.36
    command: ["sh", "-c", "echo 'PERSISTED_STATE_OK' > /var/storage/state.txt && sleep 10"]
    volumeMounts:
    - name: storage-vol
      mountPath: /var/storage
EOF_WRITER

sleep 3
kubectl delete pod state-writer -n ckad-w7d4 --force --grace-period=0

# 2. Run reader pod:
cat << "EOF_READER" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: state-reader
  namespace: ckad-w7d4
spec:
  volumes:
  - name: storage-vol
    persistentVolumeClaim:
      claimName: data-claim
  containers:
  - name: reader
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: storage-vol
      mountPath: /var/storage
EOF_READER
'
```
