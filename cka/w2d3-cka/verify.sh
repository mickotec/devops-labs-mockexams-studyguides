#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d3-cka: Services: ClusterIP, NodePort & LoadBalancer...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ClusterIP service api-internal...${NC}"
C_TYPE=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
C_PORTS=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.ports[*].port}" 2>/dev/null || true')
if [ "$C_TYPE" == "ClusterIP" ] && echo "$C_PORTS" | grep -qw "80" && echo "$C_PORTS" | grep -qw "443"; then
  echo -e "${GREEN}[PASS] ClusterIP service api-internal verified with ports 80 and 443.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service api-internal: type=$C_TYPE, ports=$C_PORTS.${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service web-public...${NC}"
N_PORT=$(ssh controlplane 'kubectl get svc web-public -n prod -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$N_PORT" == "31200" ]; then
  echo -e "${GREEN}[PASS] NodePort service on port 31200 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $N_PORT (expected 31200).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Endpoints populated...${NC}"
EP=$(ssh controlplane 'kubectl get endpoints api-internal -n prod -o jsonpath="{.subsets[0].addresses[0].ip}" 2>/dev/null || echo "None"')
POD_IP=$(ssh controlplane 'kubectl get pod backend-api -n prod -o jsonpath="{.status.podIP}" 2>/dev/null || echo "PodNone"')
if [ "$EP" != "None" ] && [ "$EP" == "$POD_IP" ]; then
  echo -e "${GREEN}[PASS] Service endpoints mapped to backend-api IP ($EP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Endpoints IP '$EP' does not match Pod IP '$POD_IP'.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d3-cka${NC}"
  exit 1
fi
