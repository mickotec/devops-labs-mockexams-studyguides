# [CKA W6D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. PV:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-data-pv
spec:
  capacity:
    storage: 200Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /tmp/app-data-pv
```
`kubectl apply -f pv.yaml`

2. PVC:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data-pvc
  namespace: w6d4-storage
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f pvc.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-writer
  namespace: w6d4-storage
spec:
  containers:
  - name: writer
    image: busybox:1.36
    command: ["sh", "-c", "echo StorageVerified > /mnt/data/success.txt && sleep 3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /mnt/data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: app-data-pvc
```
`kubectl apply -f pod.yaml`
