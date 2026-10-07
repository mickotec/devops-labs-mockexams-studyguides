#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d4-cka (ETCD Snapshot Backup & Disaster Recovery)..."
ssh controlplane '
  mkdir -p /opt/backup
  rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d4-cka"
