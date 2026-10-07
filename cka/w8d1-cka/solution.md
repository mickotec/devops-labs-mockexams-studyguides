# [CKA W8D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Fix static pod:
On `controlplane`, edit `/etc/kubernetes/manifests/broken-watchdog.yaml`:
Change `image: busybox:invalid-v999` to `image: busybox:1.36`.
Save and wait for kubelet to restart the pod.

2. Fix `db-connector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    env:
    - name: DB_HOST
      value: "10.0.0.1"
    command: ["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]
```
`kubectl replace --force -f db-connector.yaml`

3. Save kube-apiserver logs:
```bash
APIPOD=$(kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath='{.items[0].metadata.name}')
kubectl logs -n kube-system $APIPOD --tail=20 > /opt/k8s/apiserver_log_sample.txt
```
