#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-cka-1..."
ssh controlplane '
if [ -f /etc/kubernetes/kube-scheduler.yaml.bak ]; then
  sudo mv -f /etc/kubernetes/kube-scheduler.yaml.bak /etc/kubernetes/manifests/kube-scheduler.yaml
fi
sudo sed -i "s/scheduler-broken\.conf/scheduler\.conf/g" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
sudo systemctl restart kubelet
kubectl uncordon node01 2>/dev/null || true
kubectl delete ns mock-cka-1-q2 mock-cka-1-q3 mock-cka-1-q4 mock-cka-1-q5 mock-cka-1-q6 mock-cka-1-q7 mock-cka-1-q8 mock-cka-1-q9 mock-cka-1-q11 mock-cka-1-q12 mock-cka-1-q14 mock-cka-1-q16 mock-cka-1-q17 --grace-period=0 --force --wait=false 2>/dev/null || true
kubectl delete pv mock-pv 2>/dev/null || true
kubectl delete clusterrole node-watcher 2>/dev/null || true
kubectl delete clusterrolebinding node-watchers-binding 2>/dev/null || true
sudo rm -rf /opt/backup/etcd-backup.db /opt/k8s/custom-kubeconfig /mnt/mock-data
'
echo "[✓] Reset complete."
