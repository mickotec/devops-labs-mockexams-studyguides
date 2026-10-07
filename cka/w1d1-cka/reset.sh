#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d1-cka..."
ssh controlplane '
if [ -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo mv -f /etc/kubernetes/kube-scheduler.yaml.orig /etc/kubernetes/manifests/kube-scheduler.yaml
else
  sudo sed -i "s/^apiVersion: v1.0/apiVersion: v1/" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
fi
sudo sed -i "s/scheduler-broken\.conf/scheduler\.conf/g" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
sudo systemctl restart kubelet
kubectl delete pod w1d1-pending-test node01-monitor-node01 --force --grace-period=0 2>/dev/null || true
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
[ -n "$CID" ] && sudo crictl stop "$CID" 2>/dev/null && sudo crictl rm "$CID" 2>/dev/null || true
'
echo "[✓] Reset complete."
