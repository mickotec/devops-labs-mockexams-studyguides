#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D2: Liveness Probes in ckad-w4d2..."

PHASE=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESTARTS=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.status.containerStatuses[0].restartCount}" 2>/dev/null || echo 99')
PROBE=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.spec.containers[0].livenessProbe.exec.command}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$RESTARTS" -eq 0 ] && [[ "$PROBE" =~ "healthy" ]]; then
  echo -e "[0;32m[PASS] Pod health-monitor running 1/1 with active exec liveness probe (0 restarts).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, Restarts: $RESTARTS (expected 0), Probe: '$PROBE'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi