#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d6-cka (Killer.sh Simulator Marathon (Exam Benchmark))..."
ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d6-benchmark
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/etcd-backup.db
  kubectl run database -n w8d6-benchmark --image=nginx:alpine --labels=role=db
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d6-cka"
