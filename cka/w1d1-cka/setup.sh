#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d1-cka (Kubernetes Architecture & Container Runtimes)..."
# Setup Task 1: Break kube-scheduler on controlplane
ssh controlplane '
if [ ! -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo cp /etc/kubernetes/manifests/kube-scheduler.yaml /etc/kubernetes/kube-scheduler.yaml.orig
fi
sudo sed -i "s|^apiVersion: v1\$|apiVersion: v1.0|" /etc/kubernetes/manifests/kube-scheduler.yaml
CID=$(sudo crictl ps -q --name kube-scheduler 2>/dev/null || true)
if [ -n "$CID" ]; then
  sudo crictl stop "$CID" 2>/dev/null || true
  sudo crictl rm "$CID" 2>/dev/null || true
fi
sudo systemctl restart kubelet
'

# Deploy test pod that hangs in Pending
ssh controlplane '
kubectl delete pod w1d1-pending-test --force --grace-period=0 2>/dev/null || true
kubectl run w1d1-pending-test --image=nginx:alpine --restart=Never
'

# Setup Task 2: Rogue container on node01
ssh node01 '
sudo crictl inspecti docker.io/library/busybox:1.36 >/dev/null 2>&1 || sudo crictl pull docker.io/library/busybox:1.36 >/dev/null 2>&1

OLD_CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
if [ -n "$OLD_CID" ]; then
  sudo crictl stop "$OLD_CID" 2>/dev/null || true
  sudo crictl rm "$OLD_CID" 2>/dev/null || true
fi
OLD_SB=$(sudo crictl pods -q --name rogue-sandbox 2>/dev/null || true)
if [ -n "$OLD_SB" ]; then
  sudo crictl stopp "$OLD_SB" 2>/dev/null || true
  sudo crictl rmp -f "$OLD_SB" 2>/dev/null || true
fi

sudo rm -f /tmp/rogue-sandbox.json /tmp/rogue-container.json
sudo tee /tmp/rogue-sandbox.json << "EOF_SB" > /dev/null
{
  "metadata": { "name": "rogue-sandbox", "namespace": "default", "attempt": 0, "uid": "rogue-uid-001" },
  "log_directory": "/tmp/rogue-logs",
  "linux": {
    "cgroup_parent": "kubepods.slice",
    "security_context": { "namespace_options": { "network": 2, "pid": 1, "ipc": 1 }, "run_as_user": { "value": 0 } }
  }
}
EOF_SB

sudo mkdir -p /tmp/rogue-logs
SB=$(sudo crictl runp /tmp/rogue-sandbox.json 2>/dev/null || true)
if [ -n "$SB" ]; then
  sudo tee /tmp/rogue-container.json << "EOF_CN" > /dev/null
{
  "metadata": { "name": "rogue-crypto-miner" },
  "image": { "image": "docker.io/library/busybox:1.36" },
  "command": ["sh", "-c", "while true; do sleep 3600; done"],
  "log_path": "miner.log"
}
EOF_CN
  CN=$(sudo crictl create "$SB" /tmp/rogue-container.json /tmp/rogue-sandbox.json 2>/dev/null || true)
  if [ -n "$CN" ]; then
    sudo crictl start "$CN" >/dev/null 2>&1 || true
  fi
fi
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d1-cka"
