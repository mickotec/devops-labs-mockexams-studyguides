#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D6: Imperative Commands & JSONPath in ckad-w1d6..."

POD_PHASE=$(ssh controlplane 'kubectl get pod imperative-pod -n ckad-w1d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
POD_LABEL=$(ssh controlplane 'kubectl get pod imperative-pod -n ckad-w1d6 -o jsonpath="{.metadata.labels.tier}" 2>/dev/null || echo "none"')

ACTUAL_IP=$(ssh controlplane 'kubectl get pod target-alpha -n ckad-w1d6 -o jsonpath="{.status.podIP}" 2>/dev/null || echo "none"')
SAVED_IP=$(ssh controlplane 'cat /tmp/alpha-ip.txt 2>/dev/null || echo "empty"')

if [ "$POD_PHASE" == "Running" ] && [ "$POD_LABEL" == "cache" ] && [ "$SAVED_IP" == "$ACTUAL_IP" ] && [ "$SAVED_IP" != "empty" ]; then
  echo -e "\033[0;32m[PASS] Imperative pod created and JSONPath IP correctly extracted to /tmp/alpha-ip.txt.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $POD_PHASE, Label: $POD_LABEL, Saved IP: '$SAVED_IP' vs Actual IP: '$ACTUAL_IP'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi