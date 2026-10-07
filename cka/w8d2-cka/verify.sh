#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d2-cka: Troubleshooting: Worker Nodes & Network Failure...${NC}"
SCORE=0; TOTAL=3
# Task 1: node02 is Ready
N2_STATUS=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
if [ "$N2_STATUS" == "True" ]; then
  echo -e "${GREEN}[PASS] Task 1: Worker node node02 is Ready.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: node02 Ready status is $N2_STATUS (expected True).${NC}"
fi

# Task 2: Taint removed
TAINT_CHECK=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.taints[?(@.key=="trouble")].key}" 2>/dev/null || echo "None"')
if [ "$TAINT_CHECK" == "None" ] || [ -z "$TAINT_CHECK" ]; then
  echo -e "${GREEN}[PASS] Task 2: Taint trouble=unreachable:NoSchedule removed from node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Taint trouble still present on node02.${NC}"
fi

# Task 3: canary pod running on node02
POD_NODE=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
POD_STATUS=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_NODE" == "node02" ] && [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-canary running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: worker-canary node=$POD_NODE, status=$POD_STATUS (expected node02, Running).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d2-cka${NC}"
  exit 1
fi
