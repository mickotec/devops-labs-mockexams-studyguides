#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D5: Taints & Tolerations in ckad-w3d5..."

PHASE=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
NODE=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "none"')
TOL_KEY=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.spec.tolerations[?(@.key=="dedicated")].key}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$NODE" == "node01" ] && [ "$TOL_KEY" == "dedicated" ]; then
  echo -e "[0;32m[PASS] Pod analytics-engine running on tainted node01 with matching toleration.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Node: $NODE (expected node01), Toleration: '$TOL_KEY'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi