# [CKA W1D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Identify ETCD flags from `/etc/kubernetes/manifests/etcd.yaml`:
- CACERT: `/etc/kubernetes/pki/etcd/ca.crt`
- CERT: `/etc/kubernetes/pki/etcd/server.crt`
- KEY: `/etc/kubernetes/pki/etcd/server.key`
- ENDPOINT: `https://127.0.0.1:2379`

2. Task 1: Query endpoint health:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   endpoint health | sudo tee /opt/backup/etcd-health.txt
```

3. Task 2: Snapshot save and verify status:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/etcd-snapshot-w1d2.db

sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table | sudo tee /opt/backup/snapshot-status.txt
```

4. Task 3: Query namespace prefix count:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   get /registry/namespaces --prefix --keys-only | grep -v '^$' | wc -l | sudo tee /opt/backup/namespace-count.txt
```
