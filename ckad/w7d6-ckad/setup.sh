#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d6-ckad (StatefulSets & VolumeClaimTemplates)..."
ssh controlplane '
kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv-0
spec:
  capacity:
    storage: 500Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: redis-sc
  hostPath:
    path: /mnt/redis-0
    type: DirectoryOrCreate
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv-1
spec:
  capacity:
    storage: 500Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: redis-sc
  hostPath:
    path: /mnt/redis-1
    type: DirectoryOrCreate
EOF_PV
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d6-ckad"
