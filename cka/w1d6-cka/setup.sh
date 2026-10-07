#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d6-cka (Week 1 Integration & Milestone Triathlon)..."
ssh controlplane '
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/triathlon-etcd.db
sudo bash -c "
if [ -d /etc/kubernetes/manifests ] && [ ! -d /etc/kubernetes/manifests_broken ]; then
  mv /etc/kubernetes/manifests /etc/kubernetes/manifests_broken
  systemctl restart kubelet
fi
"
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d6-cka"
