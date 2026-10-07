# [CKA W5D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Snapshot:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/milestone5-etcd.db`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Certs:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/m5_certs_audit.txt`
