#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D3: Startup Probes in ckad-w4d3..."

PHASE=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESTARTS=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.status.containerStatuses[0].restartCount}" 2>/dev/null || echo 99')
THRESHOLD=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.spec.containers[0].startupProbe.failureThreshold}" 2>/dev/null || echo 0')

if [ "$PHASE" == "Running" ] && [ "$RESTARTS" -eq 0 ] && [ "$THRESHOLD" -eq 15 ]; then
  echo -e "[0;32m[PASS] slow-boot-app successfully bootstrapped with startupProbe shield (0 restarts).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Restarts: $RESTARTS (expected 0), Startup failureThreshold: $THRESHOLD (expected 15).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi