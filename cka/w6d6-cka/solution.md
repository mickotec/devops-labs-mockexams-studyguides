# [CKA W6D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. ServiceAccount & RBAC:
`kubectl create sa vault-operator -n w6-milestone`
`kubectl create role secret-reader -n w6-milestone --verb=get,list --resource=secrets`
`kubectl create rolebinding bind-secret-reader -n w6-milestone --role=secret-reader --serviceaccount=w6-milestone:vault-operator`

2. PV & PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: m6-pv
spec:
  capacity:
    storage: 150Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  hostPath:
    path: /tmp/m6-pv
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: m6-pvc
  namespace: w6-milestone
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f storage.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-pod
  namespace: w6-milestone
spec:
  serviceAccountName: vault-operator
  securityContext:
    runAsUser: 10001
  containers:
  - name: box
    image: busybox:1.36
    command: ["sh", "-c", "echo Milestone6Complete > /data/flag.txt && sleep 3600"]
    volumeMounts:
    - name: vol
      mountPath: /data
  volumes:
  - name: vol
    persistentVolumeClaim:
      claimName: m6-pvc
```
`kubectl apply -f pod.yaml`
