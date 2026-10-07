# [CKA MOCK-CKA-1] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: ETCD Snapshot
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/etcd-backup.db
```

#### Q2: Role & RoleBinding
```bash
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n mock-cka-1-q2
kubectl create rolebinding read-pods --role=pod-reader --user=jane -n mock-cka-1-q2
```

#### Q3: ClusterRole & ClusterRoleBinding
```bash
kubectl create clusterrole node-watcher --verb=get,list,watch --resource=nodes
kubectl create clusterrolebinding node-watchers-binding --clusterrole=node-watcher --group=system:nodes
```

#### Q4: Custom Kubeconfig
```bash
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-cluster k8s-cluster --server=https://172.16.16.210:6443 --insecure-skip-tls-verify=true
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-credentials dev-user --token=mock-token
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-context dev-context --cluster=k8s-cluster --user=dev-user
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig use-context dev-context
```

#### Q5: Deployment Rollback
```bash
kubectl set image deploy/nginx-deploy nginx=nginx:1.25-alpine -n mock-cka-1-q5
kubectl rollout undo deploy/nginx-deploy -n mock-cka-1-q5 --to-revision=1
```

#### Q6: Sidecar Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
  namespace: mock-cka-1-q6
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo app running >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: shared-data
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /var/log/app.log"]
    volumeMounts:
    - name: shared-data
      mountPath: /var/log
```

#### Q7: ConfigMap & Secret Pod
```bash
kubectl create configmap app-config --from-literal=ENV_MODE=production -n mock-cka-1-q7
kubectl create secret generic app-secret --from-literal=API_KEY=secret123 -n mock-cka-1-q7
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
  namespace: mock-cka-1-q7
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    env:
    - name: CONFIG_VAL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: ENV_MODE
    - name: SECRET_VAL
      valueFrom:
        secretKeyRef:
          name: app-secret
          key: API_KEY
```

#### Q8: Services Exposure
```bash
kubectl expose deploy web -n mock-cka-1-q8 --name=web-svc --port=80
kubectl expose deploy web -n mock-cka-1-q8 --name=web-nodeport --type=NodePort --port=80
kubectl patch svc web-nodeport -n mock-cka-1-q8 --type='json' -p='[{"op":"replace","path":"/spec/ports/0/nodePort","value":31555}]'
```

#### Q9: NetworkPolicy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-client
  namespace: mock-cka-1-q9
spec:
  podSelector:
    matchLabels:
      app: nginx
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: client
```

#### Q10: CoreDNS Query
```bash
ssh controlplane 'kubectl run dns-test --image=busybox:1.36 --restart=Never -- nslookup kubernetes.default.svc.cluster.local > /opt/k8s/dns-test.txt; kubectl delete pod dns-test'
```

#### Q11 & Q12: Storage PV/PVC & Pod
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mock-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/mock-data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mock-pvc
  namespace: mock-cka-1-q11
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```
In Q12, create pod mounting `mock-pvc` at `/data` and write `storage-ok` to `/data/status.txt`.

#### Q13: Scheduler Repair
On `controlplane`:
`sudo sed -i 's|scheduler-broken.conf|scheduler.conf|' /etc/kubernetes/manifests/kube-scheduler.yaml`
`sudo systemctl restart kubelet`

#### Q14: CrashLoop Repair
Edit `broken-worker` command to `["sh", "-c", "sleep 3600"]`.

#### Q15: Uncordon Node
`kubectl uncordon node01`

#### Q16: Service Selector Repair
`kubectl patch svc api-service -n mock-cka-1-q16 --type='json' -p='[{"op":"replace","path":"/spec/selector/app","value":"api-v1"}]'`

#### Q17: Deployment Environment Variable
`kubectl set env deploy/db-client -n mock-cka-1-q17 DB_HOST=10.0.0.1`
