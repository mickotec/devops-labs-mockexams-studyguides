#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D2: PersistentVolume app-storage-pv..."

CAP=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.spec.capacity.storage}" 2>/dev/null || echo ""')
RECLAIM=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.spec.persistentVolumeReclaimPolicy}" 2>/dev/null || echo ""')
STATUS=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')

if [ "$CAP" == "2Gi" ] && [ "$RECLAIM" == "Retain" ] && [ "$STATUS" == "Available" ]; then
  echo -e "[0;32m[PASS] PersistentVolume app-storage-pv Available (2Gi, Retain, ReadWriteOnce).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Capacity: $CAP | Reclaim: $RECLAIM | Status: $STATUS (expected Available).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi