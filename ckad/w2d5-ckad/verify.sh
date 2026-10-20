#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D5: SecurityContexts & Capabilities in ckad-w2d5..."

PHASE=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
UID_VAL=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.spec.securityContext.runAsUser}" 2>/dev/null || echo 0')
READONLY=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo "false"')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ] && [ "$UID_VAL" -eq 2000 ] && [ "$READONLY" == "true" ]; then
  echo -e "[0;32m[PASS] Pod locked-container running as non-root (UID 2000) with readOnlyRootFilesystem.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Ready: $READY, UID: $UID_VAL (expected 2000), ReadOnly: $READONLY (expected true).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi