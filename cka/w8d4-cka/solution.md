# [CKA W8D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. RBAC:
```bash
kubectl create sa deploy-bot -n w8d4-exam
kubectl create role pod-reader -n w8d4-exam --verb=get,list,watch --resource=pods
kubectl create rolebinding deploy-bot-reader -n w8d4-exam --role=pod-reader --serviceaccount=w8d4-exam:deploy-bot
```

2. Multi-container pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-logger
  namespace: w8d4-exam
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: producer
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
  - name: consumer
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /var/log/app.log"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
```

3. Secret and pod:
```bash
kubectl create secret generic db-credentials -n w8d4-exam --from-literal=DB_USER=dbadmin --from-literal=DB_PASS=SuperSecret101
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-client
  namespace: w8d4-exam
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_USER
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_PASS
```

4. DaemonSet:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-sentinel
  namespace: w8d4-exam
spec:
  selector:
    matchLabels:
      app: node-sentinel
  template:
    metadata:
      labels:
        app: node-sentinel
    spec:
      containers:
      - name: sentinel
        image: busybox:1.36
        command: ["sleep", "3600"]
```
