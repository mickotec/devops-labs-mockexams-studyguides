# [CKA W5D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Take snapshot on controlplane:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/etcd-snapshot-w5.db`

2. Status table:
`sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table | sudo tee /opt/backup/etcd_snapshot_status.txt`
