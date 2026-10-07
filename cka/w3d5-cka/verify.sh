#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d5-cka: Priority Classes & Multiple Schedulers...${NC}"
SCORE=0; TOTAL=3
# Task 1: PriorityClasses
PC_VAL1=$(ssh controlplane 'kubectl get priorityclass mission-critical -o jsonpath="{.value}" 2>/dev/null || echo "0"')
PC_VAL2=$(ssh controlplane 'kubectl get priorityclass low-priority -o jsonpath="{.value}" 2>/dev/null || echo "0"')
if [ "$PC_VAL1" == "1000000" ] && [ "$PC_VAL2" == "500" ]; then
  echo -e "${GREEN}[PASS] Task 1: PriorityClasses mission-critical and low-priority verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PriorityClass values incorrect: critical=$PC_VAL1, low=$PC_VAL2.${NC}"
fi

# Task 2: critical-db pod
P1_NAME=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P1_STATUS=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P1_NAME" == "mission-critical" ] && [ "$P1_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod critical-db assigned mission-critical priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-db priority=$P1_NAME, status=$P1_STATUS.${NC}"
fi

# Task 3: batch-worker pod
P2_NAME=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P2_STATUS=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P2_NAME" == "low-priority" ] && [ "$P2_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: Pod batch-worker assigned low-priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: batch-worker priority=$P2_NAME, status=$P2_STATUS.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d5-cka${NC}"
  exit 1
fi
