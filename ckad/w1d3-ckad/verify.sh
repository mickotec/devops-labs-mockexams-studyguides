#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D3: ReplicaSets & Pod Adoption in ckad-w1d3..."

RS_REPLICAS=$(ssh controlplane 'kubectl get rs frontend-rs -n ckad-w1d3 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
ORPHAN_LABEL=$(ssh controlplane 'kubectl get pod orphan-web -n ckad-w1d3 -o jsonpath="{.metadata.labels.tier}" 2>/dev/null || echo "none"')

if [ "$RS_REPLICAS" -eq 3 ] && [ "$ORPHAN_LABEL" == "web" ]; then
  echo -e "\033[0;32m[PASS] ReplicaSet frontend-rs ready with 3 replicas including adopted orphan-web.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Ready replicas: $RS_REPLICAS (expected 3) | orphan-web tier label: $ORPHAN_LABEL (expected web).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi