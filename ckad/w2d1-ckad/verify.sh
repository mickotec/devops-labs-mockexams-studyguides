#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D1: Container Commands & Arguments in ckad-w2d1..."

PHASE=$(ssh controlplane 'kubectl get pod report-worker -n ckad-w2d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
OUTPUT=$(ssh controlplane 'kubectl exec report-worker -n ckad-w2d1 -- cat /tmp/reports/output.txt 2>/dev/null | head -n 1 || echo "Empty"')

if [ "$PHASE" == "Running" ] && [ "$OUTPUT" != "Empty" ]; then
  echo -e "[0;32m[PASS] Pod report-worker running with custom command & args generating output.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: '$PHASE' | Output: '$OUTPUT' (expected Running with report content).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi