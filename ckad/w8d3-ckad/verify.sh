#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D3: ClusterRole cluster-inspector..."

CAN_NODES=$(ssh controlplane 'kubectl auth can-i get nodes --as=system:serviceaccount:default:auditor-sa 2>/dev/null || echo "no"')
CAN_PVS=$(ssh controlplane 'kubectl auth can-i get persistentvolumes --as=system:serviceaccount:default:auditor-sa 2>/dev/null || echo "no"')

if [ "$CAN_NODES" == "yes" ] && [ "$CAN_PVS" == "yes" ]; then
  echo -e "[0;32m[PASS] ClusterRoleBinding bind-cluster-inspector grants cluster-wide node & PV read access.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] can-i get nodes: '$CAN_NODES' | can-i get pvs: '$CAN_PVS'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi