#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D6: NodeAffinity in ckad-w3d6..."

PHASE=$(ssh controlplane 'kubectl get pod fast-io-worker -n ckad-w3d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
NODE=$(ssh controlplane 'kubectl get pod fast-io-worker -n ckad-w3d6 -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "none"')
LABEL=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.metadata.labels.storage-tier}" 2>/dev/null || echo "none"')

if [ "$PHASE" == "Running" ] && [ "$NODE" == "node02" ] && [ "$LABEL" == "nvme" ]; then
  echo -e "[0;32m[PASS] Pod fast-io-worker scheduled on node02 matching required nodeAffinity.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Node: $NODE (expected node02), node02 label: $LABEL (expected nvme).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi