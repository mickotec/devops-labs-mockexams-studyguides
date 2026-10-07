#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d1-cka: Node Maintenance: Cordon, Drain & Uncordon...${NC}"
SCORE=0; TOTAL=2
# Task 1 & 2: Verification of node02 status
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
# Check user pods on node02 in w5d1-maint
PODS_ON_N2=$(ssh controlplane 'kubectl get pods -n w5d1-maint --field-selector spec.nodeName=node02 --no-headers 2>/dev/null | wc -l')

# Note: After maintenance test, candidate uncordons node02
if [ "$UNSCHED" != "true" ] && [ "$PODS_ON_N2" -eq 0 ]; then
  echo -e "${GREEN}[PASS] Tasks 1-3: node02 drained cleanly and returned to schedulable state.${NC}"
  SCORE=$((SCORE + 2))
elif [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Node is currently cordoned. Now uncordon node02 to complete Task 3!${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Maintenance steps incomplete.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d1-cka${NC}"
  exit 1
fi
