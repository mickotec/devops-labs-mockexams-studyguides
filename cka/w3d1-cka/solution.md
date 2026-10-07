# [CKA W3D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Label nodes:
`kubectl label node node01 disktype=ssd`
`kubectl label node node02 environment=production`

2. Deploy `storage-worker`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-worker
  namespace: w3d1-sched
spec:
  nodeSelector:
    disktype: ssd
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f storage-worker.yaml`

3. Modify `/opt/k8s/orphan-pod.yaml`: add `nodeName: node02` under `spec`:
```yaml
spec:
  nodeName: node02
  containers:
  ...
```
`kubectl apply -f /opt/k8s/orphan-pod.yaml`
