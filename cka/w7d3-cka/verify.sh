#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d3-cka: Ingress Controllers & Routing Rules...${NC}"
SCORE=0; TOTAL=3
# Task 1: Services catalog-svc and orders-svc active
CSVC=$(ssh controlplane 'kubectl get svc catalog-svc -n w7d3-ingress -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
OSVC=$(ssh controlplane 'kubectl get svc orders-svc -n w7d3-ingress -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
if [ "$CSVC" == "80" ] && [ "$OSVC" == "80" ]; then
  echo -e "${GREEN}[PASS] Task 1: Backend services catalog-svc and orders-svc active on port 80.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Services missing or ports incorrect (catalog-svc=$CSVC, orders-svc=$OSVC).${NC}"
fi

# Task 2: Ingress store-ingress host and path routing
HOST=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
P1=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/catalog")].backend.service.name}" 2>/dev/null || echo "None"')
P2=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/orders")].backend.service.name}" 2>/dev/null || echo "None"')

if [ "$HOST" == "store.internal.example.com" ] && [ "$P1" == "catalog-svc" ] && [ "$P2" == "orders-svc" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress store-ingress routes host $HOST to catalog-svc and orders-svc.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress routing mismatch (host=$HOST, /catalog=$P1, /orders=$P2).${NC}"
fi

# Task 3: Rewrite annotation
REWRITE=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.metadata.annotations.nginx\.ingress\.kubernetes\.io/rewrite-target}" 2>/dev/null || echo "None"')
if [ "$REWRITE" == "/" ]; then
  echo -e "${GREEN}[PASS] Task 3: Rewrite annotation nginx.ingress.kubernetes.io/rewrite-target: / verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Rewrite annotation is $REWRITE (expected /).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d3-cka${NC}"
  exit 1
fi
