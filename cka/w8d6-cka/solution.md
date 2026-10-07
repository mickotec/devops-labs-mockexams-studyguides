# [CKA W8D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Sidecar pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: audit-counter
  namespace: w8d6-benchmark
spec:
  volumes:
  - name: log-storage
    emptyDir: {}
  containers:
  - name: counter
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/counter.log"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
```

2. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/k8s/etcd-backup.db
```

3. Ingress & TLS:
```bash
kubectl create deployment frontend -n w8d6-benchmark --image=nginx:alpine --port=80
kubectl expose deployment frontend -n w8d6-benchmark --name=frontend-svc --port=80
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/bench.key -out /tmp/bench.crt -subj "/CN=benchmark.k8s.local"
kubectl create secret tls benchmark-tls -n w8d6-benchmark --cert=/tmp/bench.crt --key=/tmp/bench.key
```
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: benchmark-ingress
  namespace: w8d6-benchmark
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - benchmark.k8s.local
    secretName: benchmark-tls
  rules:
  - host: benchmark.k8s.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
```

4. NetworkPolicy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: strict-db-policy
  namespace: w8d6-benchmark
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
```
