#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D1: emptyDir Memory in ckad-w7d1..."

PHASE=$(ssh controlplane 'kubectl get pod cache-node -n ckad-w7d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
FS_TYPE=$(ssh controlplane 'kubectl exec cache-node -n ckad-w7d1 -- df -T /cache 2>/dev/null | tail -n 1 | awk "{print \$2}" || echo ""')

if [ "$PHASE" == "Running" ] && [ "$FS_TYPE" == "tmpfs" ]; then
  echo -e "[0;32m[PASS] Pod cache-node running with in-memory emptyDir (tmpfs) mounted at /cache.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE | /cache filesystem type: '$FS_TYPE' (expected tmpfs).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi