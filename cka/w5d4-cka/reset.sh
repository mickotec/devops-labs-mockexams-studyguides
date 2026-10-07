#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d4-cka..."
ssh controlplane 'rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt'
echo "[✓] Reset complete."
