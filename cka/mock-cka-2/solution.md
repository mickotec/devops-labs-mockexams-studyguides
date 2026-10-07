# [CKA MOCK-CKA-2] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Walkthrough & Solution Guide

#### Q1: ServiceAccount & ClusterRole
```bash
kubectl create sa monitoring-sa -n mock-cka-2-q1
kubectl create clusterrole monitoring-role --verb=get,list,watch --resource=pods,services,nodes
kubectl create clusterrolebinding monitoring-binding --clusterrole=monitoring-role --serviceaccount=mock-cka-2-q1:monitoring-sa
```

#### Q2: Certificate Expiry
```bash
kubeadm certs check-expiry > /opt/k8s/apiserver-expiry.txt
```

#### Q3: Worker Static Pod
On `node01`:
```bash
sudo tee /etc/kubernetes/manifests/static-web.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: static-web
spec:
  containers:
  - name: web
    image: nginx:alpine
EOF
```

#### Q4: Node Maintenance
```bash
kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force
sleep 5
kubectl uncordon node02
```

#### Q5: Init Container
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-volume-pod
  namespace: mock-cka-2-q5
spec:
  volumes:
  - name: work-vol
    emptyDir: {}
  initContainers:
  - name: init-writer
    image: busybox:1.36
    command: ["sh", "-c", "echo init-data > /shared/greeting.txt"]
    volumeMounts:
    - name: work-vol
      mountPath: /shared
  containers:
  - name: main-reader
    image: busybox:1.36
    command: ["sh", "-c", "cat /shared/greeting.txt && sleep 3600"]
    volumeMounts:
    - name: work-vol
      mountPath: /shared
```

#### Q6: HPA
```bash
kubectl autoscale deploy hpa-deployment --cpu-percent=60 --min=2 --max=8 -n mock-cka-2-q6
```

#### Q7: CronJob
```bash
kubectl create cronjob periodic-task --image=busybox:1.36 --schedule="*/5 * * * *" -n mock-cka-2-q7 -- sh -c "date"
kubectl patch cronjob periodic-task -n mock-cka-2-q7 -p '{"spec":{"concurrencyPolicy":"Forbid"}}'
```

#### Q8: Headless Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-headless
  namespace: mock-cka-2-q8
spec:
  clusterIP: None
  selector:
    app: db
  ports:
  - port: 3306
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-deployment
  namespace: mock-cka-2-q8
spec:
  replicas: 3
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
      - name: db
        image: nginx:alpine
```

#### Q9: Cross-Namespace NetworkPolicy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: mock-cka-2-q9
spec:
  podSelector:
    matchLabels:
      role: backend
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: mock-cka-2-q9-frontend
```

#### Q10: ExternalName Service
```bash
kubectl create svc externalname db-external --external-name=database.example.com -n mock-cka-2-q10
```

#### Q11: Manual PV/PVC
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: manual-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /mnt/manual-data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: manual-pvc
  namespace: mock-cka-2-q11
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 2Gi
```

#### Q13: Restart Kubelet
`ssh node02 'sudo systemctl restart kubelet'`

#### Q14: Remove Node Taint
`kubectl taint nodes node01 tier=special:NoSchedule-`

#### Q15: Repair Broken Logger Pod
```bash
kubectl delete pod broken-logger -n mock-cka-2-q15 --force --grace-period=0
kubectl run broken-logger -n mock-cka-2-q15 --image=busybox:1.36 -- sh -c "while true; do date; sleep 5; done"
```

#### Q16: Ingress Resource
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: mock-cka-2-q16
spec:
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

#### Q17: Fix Deployment Image
`kubectl set image deploy/broken-deployment nginx=nginx:1.25-alpine -n mock-cka-2-q17`
