#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D2: Rolling Updates in ckad-w5d2..."

IMG=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
SURGE=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.strategy.rollingUpdate.maxSurge}" 2>/dev/null || echo ""')
UNAVAIL=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo ""')

if [[ "$IMG" =~ "nginx:1.25" ]] && [ "$REPLICAS" -eq 5 ] && [ "$SURGE" == "2" ] && [ "$UNAVAIL" == "0" ]; then
  echo -e "[0;32m[PASS] payment-gateway rolling update completed with maxSurge=2, maxUnavailable=0.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Image: $IMG, Replicas: $REPLICAS (expected 5), Surge: $SURGE, Unavail: $UNAVAIL[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi