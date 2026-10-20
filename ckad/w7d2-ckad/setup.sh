#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d2-ckad (PersistentVolumes: AccessModes & Reclaim Policies)..."
ssh controlplane 'kubectl delete pv app-storage-pv --ignore-not-found'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d2-ckad"
