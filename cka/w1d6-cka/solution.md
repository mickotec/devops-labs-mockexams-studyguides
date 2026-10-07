# [CKA W1D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Restore manifests directory:
```bash
sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
sudo systemctl restart kubelet
```

2. Multi-tier application:
```bash
kubectl create ns triathlon-w1
kubectl create deploy web-ui -n triathlon-w1 --image=nginx:1.25-alpine --replicas=2
kubectl set resources deploy web-ui -n triathlon-w1 --limits=cpu=150m,memory=128Mi
kubectl expose deploy web-ui -n triathlon-w1 --name=web-ui-svc --port=80
```

3. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/triathlon-etcd.db
```

4. Worker static pod on `node01`:
`ssh node01`
```bash
sudo tee /etc/kubernetes/manifests/w1-worker-agent.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: w1-worker-agent
spec:
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
```
