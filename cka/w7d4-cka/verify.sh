#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d4-cka: Gateway API (2025 Updates)...${NC}"
SCORE=0; TOTAL=3
# Task 1: GatewayClass exists
GW_CLASS=$(ssh controlplane 'kubectl get gatewayclass cluster-gateway-class -o jsonpath="{.spec.controllerName}" 2>/dev/null || echo "None"')
if [ "$GW_CLASS" != "None" ]; then
  echo -e "${GREEN}[PASS] Task 1: GatewayClass cluster-gateway-class verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GatewayClass cluster-gateway-class not found.${NC}"
fi

# Task 2: Gateway prod-gateway in w7d4-gw
GW_NAME=$(ssh controlplane 'kubectl get gateway prod-gateway -n w7d4-gw -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
GW_PORT=$(ssh controlplane 'kubectl get gateway prod-gateway -n w7d4-gw -o jsonpath="{.spec.listeners[0].port}" 2>/dev/null || echo "0"')
if [ "$GW_NAME" == "prod-gateway" ] && [ "$GW_PORT" == "80" ]; then
  echo -e "${GREEN}[PASS] Task 2: Gateway prod-gateway listening on HTTP port 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Gateway prod-gateway missing or port is $GW_PORT (expected 80).${NC}"
fi

# Task 3: HTTPRoute api-route
ROUTE_NAME=$(ssh controlplane 'kubectl get httproute api-route -n w7d4-gw -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
ROUTE_BACKEND=$(ssh controlplane 'kubectl get httproute api-route -n w7d4-gw -o jsonpath="{.spec.rules[0].backendRefs[0].name}" 2>/dev/null || echo "None"')
if [ "$ROUTE_NAME" == "api-route" ] && [ "$ROUTE_BACKEND" == "api-service" ]; then
  echo -e "${GREEN}[PASS] Task 3: HTTPRoute api-route routes to api-service.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: HTTPRoute api-route invalid (name=$ROUTE_NAME, backend=$ROUTE_BACKEND).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d4-cka${NC}"
  exit 1
fi
