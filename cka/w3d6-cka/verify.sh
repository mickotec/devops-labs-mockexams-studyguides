#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d6-cka: Week 3 Scheduling Troubleshooting Matrix...${NC}"
SCORE=0; TOTAL=3
# Task 1: stuck-selector is Running on node02
S1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
N1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$S1" == "Running" ] && [ "$N1" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 1: stuck-selector is Running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: stuck-selector status=$S1, node=$N1.${NC}"
fi

# Task 2: stuck-taint has toleration and is Running
S2=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
TOL=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.spec.tolerations[?(@.key=="dedicated")].value}" 2>/dev/null || echo "None"')
if [ "$S2" == "Running" ] && [ "$TOL" == "web" ]; then
  echo -e "${GREEN}[PASS] Task 2: stuck-taint has toleration and is Running on node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: stuck-taint status=$S2, toleration=$TOL.${NC}"
fi

# Task 3: infra-agent DaemonSet running on controlplane
CP_POD=$(ssh controlplane 'kubectl get pods -n w3-milestone -l app=infra-agent --field-selector spec.nodeName=controlplane -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$CP_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: infra-agent DaemonSet scheduled and Running on controlplane.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: infra-agent pod on controlplane is $CP_POD.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d6-cka${NC}"
  exit 1
fi
