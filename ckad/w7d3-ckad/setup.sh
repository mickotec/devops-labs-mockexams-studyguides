#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d3-ckad (PersistentVolumeClaims & Volume Binding)..."
ssh controlplane '
kubectl create namespace ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: claim-target-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: manual-target
  hostPath:
    path: /mnt/target-data
    type: DirectoryOrCreate
EOF_PV
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d3-ckad"
