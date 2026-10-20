#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d4-ckad (Consuming PVCs in Pods & Data Persistence)..."
ssh controlplane '
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_STORAGE" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: persist-test-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: persist-class
  hostPath:
    path: /mnt/persist-data
    type: DirectoryOrCreate
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-claim
  namespace: ckad-w7d4
spec:
  storageClassName: persist-class
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
EOF_STORAGE
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d4-ckad"
