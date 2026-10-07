#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d5-cka: Network Policies Deep Dive...${NC}"
SCORE=0; TOTAL=3
# Task 1: default-deny-ingress
DD_MATCH=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n w7d5-netpol -o jsonpath="{.spec.policyTypes[0]}" 2>/dev/null || echo "None"')
if [ "$DD_MATCH" == "Ingress" ]; then
  echo -e "${GREEN}[PASS] Task 1: default-deny-ingress policy verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: default-deny-ingress missing or policyType is $DD_MATCH.${NC}"
fi

# Task 2: allow-fe-to-be
FE_PORT=$(ssh controlplane 'kubectl get netpol allow-fe-to-be -n w7d5-netpol -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
FE_FROM=$(ssh controlplane 'kubectl get netpol allow-fe-to-be -n w7d5-netpol -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
if [ "$FE_PORT" == "80" ] && [ "$FE_FROM" == "frontend" ]; then
  echo -e "${GREEN}[PASS] Task 2: allow-fe-to-be allows role=frontend on port 80.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: allow-fe-to-be incorrect (from=$FE_FROM, port=$FE_PORT).${NC}"
fi

# Task 3: allow-be-to-db
DB_PORT=$(ssh controlplane 'kubectl get netpol allow-be-to-db -n w7d5-netpol -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
DB_FROM=$(ssh controlplane 'kubectl get netpol allow-be-to-db -n w7d5-netpol -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
if [ "$DB_PORT" == "5432" ] && [ "$DB_FROM" == "backend" ]; then
  echo -e "${GREEN}[PASS] Task 3: allow-be-to-db allows role=backend on port 5432.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: allow-be-to-db incorrect (from=$DB_FROM, port=$DB_PORT).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d5-cka${NC}"
  exit 1
fi
