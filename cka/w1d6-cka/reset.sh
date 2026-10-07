#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d6-cka..."
ssh controlplane '
if [ -d /etc/kubernetes/manifests_broken ]; then
  sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
  sudo systemctl restart kubelet
fi
for i in $(seq 1 30); do
  kubectl get nodes >/dev/null 2>&1 && break
  sleep 1
done
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
kubectl delete pod w1-worker-agent-node01 --force --grace-period=0 2>/dev/null || true
sudo rm -rf /opt/backup
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
echo "[✓] Reset complete."
