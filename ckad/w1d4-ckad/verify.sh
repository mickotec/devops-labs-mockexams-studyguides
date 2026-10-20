#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D4: Deployments & Rolling Updates in ckad-w1d4..."

IMAGE=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "none"')
REPLICAS=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
MAX_UNAVAIL=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo "none"')

if [[ "$IMAGE" =~ "nginx:1.25" ]] && [ "$REPLICAS" -eq 4 ] && [ "$MAX_UNAVAIL" == "0" ]; then
  echo -e "\033[0;32m[PASS] api-gateway scaled to 4 replicas of nginx:1.25-alpine with maxUnavailable=0.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Image: $IMAGE, Replicas: $REPLICAS (expected 4), maxUnavailable: $MAX_UNAVAIL (expected 0).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi