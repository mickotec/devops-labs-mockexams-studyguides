#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d3-cka: Resource Requirements, Limits & LimitRanges...${NC}"
SCORE=0; TOTAL=3
# Task 1: LimitRange
LR=$(ssh controlplane 'kubectl get limitrange resource-bounds -n w3d3-resources -o jsonpath="{.spec.limits[0].default.memory}" 2>/dev/null || echo "None"')
if [ "$LR" == "128Mi" ]; then
  echo -e "${GREEN}[PASS] Task 1: LimitRange resource-bounds configured with default limit 128Mi.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: LimitRange resource-bounds missing or default memory is $LR.${NC}"
fi

# Task 2: bounded-service
BS_MEM=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
BS_STATUS=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$BS_MEM" == "200Mi" ] && [ "$BS_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: bounded-service has 200Mi limit and is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: bounded-service limit=$BS_MEM, status=$BS_STATUS.${NC}"
fi

# Task 3: unconstrained-pod default injection
UP_LIMIT=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
UP_REQ=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.requests.memory}" 2>/dev/null || echo "None"')
if [ "$UP_LIMIT" == "128Mi" ] && [ "$UP_REQ" == "64Mi" ]; then
  echo -e "${GREEN}[PASS] Task 3: unconstrained-pod received injected defaults from LimitRange (64Mi/128Mi).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Injected values mismatch: req=$UP_REQ, limit=$UP_LIMIT.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d3-cka${NC}"
  exit 1
fi
