#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d5-cka: Timed Mock Exam 2 & 3 Marathon...${NC}"
SCORE=0; TOTAL=4
# Task 1: PVC Bound
PVC_STAT=$(ssh controlplane 'kubectl get pvc pvc-marathon -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 1: PVC pvc-marathon is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PVC pvc-marathon status is $PVC_STAT (expected Bound).${NC}"
fi

# Task 2: zone-app scheduled to node01
POD_NODES=$(ssh controlplane 'kubectl get pods -n w8d5-marathon -l app=zone-app -o jsonpath="{.items[*].spec.nodeName}" 2>/dev/null || echo ""')
if [ -n "$POD_NODES" ] && [[ ! "$POD_NODES" =~ node02 ]] && [[ "$POD_NODES" =~ node01 ]]; then
  echo -e "${GREEN}[PASS] Task 2: Deployment zone-app pods scheduled strictly on node01 ($POD_NODES).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment zone-app pods nodes: '$POD_NODES' (expected only node01).${NC}"
fi

# Task 3: special-worker on node02
SW_STATUS=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
SW_NODE=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$SW_STATUS" == "Running" ] && [ "$SW_NODE" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 3: special-worker running on tainted node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: special-worker status=$SW_STATUS, node=$SW_NODE.${NC}"
fi

# Task 4: zone-app image is nginx:alpine
CUR_IMG=$(ssh controlplane 'kubectl get deployment zone-app -n w8d5-marathon -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
if [ "$CUR_IMG" == "nginx:alpine" ]; then
  echo -e "${GREEN}[PASS] Task 4: Deployment zone-app rolled back to nginx:alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Deployment zone-app image is '$CUR_IMG' (expected nginx:alpine).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d5-cka${NC}"
  exit 1
fi
