#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d2-cka: RBAC (Roles, RoleBindings & ClusterRoles)...${NC}"
SCORE=0; TOTAL=2
# Task 1 & 3: Role and auth check
CAN_PODS=$(ssh controlplane 'kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_PODS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount dev-sa authorized to list pods in w6d2-rbac.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: dev-sa cannot list pods in w6d2-rbac.${NC}"
fi

# Task 2 & 3: ClusterRole and auth check
CAN_NODES=$(ssh controlplane 'kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_NODES" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: ServiceAccount dev-sa authorized to list nodes cluster-wide.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: dev-sa cannot list nodes cluster-wide.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d2-cka${NC}"
  exit 1
fi
