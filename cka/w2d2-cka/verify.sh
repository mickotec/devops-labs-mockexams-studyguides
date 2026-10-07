#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d2-cka: Deployments, Rollouts & Revisions...${NC}"
SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1 & 2: Rolling update & image version...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')

if [ "$IMAGE" == "nginx:1.25-alpine" ] && [ "$REPLICAS" == "3" ]; then
  echo -e "${GREEN}[PASS] payment-app deployment rolled back to stable 1.25-alpine with 3/3 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is '$IMAGE' (expected nginx:1.25-alpine) or readyReplicas=$REPLICAS (expected 3).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Deployment strategy...${NC}"
SURGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxSurge}" 2>/dev/null || echo "None"')
UNAVAIL=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo "None"')

if [ "$SURGE" == "1" ] && [ "$UNAVAIL" == "0" ]; then
  echo -e "${GREEN}[PASS] RollingUpdate strategy verified (maxSurge=1, maxUnavailable=0).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Strategy: maxSurge=$SURGE, maxUnavailable=$UNAVAIL.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d2-cka${NC}"
  exit 1
fi
