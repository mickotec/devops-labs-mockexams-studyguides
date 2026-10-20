#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D6: StatefulSets in ckad-w7d6..."

REPLICAS=$(ssh controlplane 'kubectl get statefulset redis-cluster -n ckad-w7d6 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
PVC_0=$(ssh controlplane 'kubectl get pvc redis-data-redis-cluster-0 -n ckad-w7d6 -o jsonpath="{.metadata.name}" 2>/dev/null || echo ""')
PVC_1=$(ssh controlplane 'kubectl get pvc redis-data-redis-cluster-1 -n ckad-w7d6 -o jsonpath="{.metadata.name}" 2>/dev/null || echo ""')

if [ "$REPLICAS" -eq 2 ] && [ -n "$PVC_0" ] && [ -n "$PVC_1" ]; then
  echo -e "\033[0;32m[PASS] StatefulSet redis-cluster 2/2 ready with dedicated volumeClaimTemplates PVCs.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Ready replicas: $REPLICAS/2 | PVC 0: '''$PVC_0''' | PVC 1: '''$PVC_1'''\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi