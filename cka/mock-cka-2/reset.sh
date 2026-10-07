#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-cka-2..."
ssh controlplane '
kubectl delete ns mock-cka-2-q1 mock-cka-2-q5 mock-cka-2-q6 mock-cka-2-q7 mock-cka-2-q8 mock-cka-2-q9 mock-cka-2-q9-frontend mock-cka-2-q10 mock-cka-2-q11 mock-cka-2-q12 mock-cka-2-q14 mock-cka-2-q15 mock-cka-2-q16 mock-cka-2-q17 --grace-period=0 --force --wait=false 2>/dev/null || true
kubectl delete pv manual-pv 2>/dev/null || true
kubectl delete clusterrole monitoring-role 2>/dev/null || true
kubectl delete clusterrolebinding monitoring-binding 2>/dev/null || true
kubectl taint nodes node01 tier=special:NoSchedule- 2>/dev/null || true
kubectl uncordon node02 2>/dev/null || true
kubectl delete pod static-web-node01 --force --grace-period=0 2>/dev/null || true
sudo rm -rf /opt/k8s/apiserver-expiry.txt /mnt/manual-data
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/static-web.yaml
POD_ID=$(sudo crictl pods -q --name static-web-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
ssh node02 'sudo systemctl restart kubelet 2>/dev/null || true'
echo "[✓] Reset complete."
