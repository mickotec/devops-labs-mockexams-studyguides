#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d2-cka (ETCD Fundamentals & Cluster State Store)..."
ssh controlplane '
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/etcd-health.txt /opt/backup/etcd-snapshot-w1d2.db /opt/backup/snapshot-status.txt /opt/backup/namespace-count.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d2-cka"
