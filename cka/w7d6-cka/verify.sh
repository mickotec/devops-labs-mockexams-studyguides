#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d6-cka: Week 7 Network Mastery Triathlon...${NC}"
SCORE=0; TOTAL=3
# Task 1: Services frontend-svc and backend-svc
FE_EP=$(ssh controlplane 'kubectl get endpoints frontend-svc -n w7d6-triathlon -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
BE_EP=$(ssh controlplane 'kubectl get endpoints backend-svc -n w7d6-triathlon -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
if [ "$FE_EP" -ge 2 ] && [ "$BE_EP" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: Multi-service endpoints verified (frontend=$FE_EP, backend=$BE_EP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Service endpoints insufficient (frontend=$FE_EP, backend=$BE_EP, expected >=2).${NC}"
fi

# Task 2: Ingress with TLS
ING_TLS=$(ssh controlplane 'kubectl get ingress triathlon-ingress -n w7d6-triathlon -o jsonpath="{.spec.tls[0].secretName}" 2>/dev/null || echo "None"')
ING_HOST=$(ssh controlplane 'kubectl get ingress triathlon-ingress -n w7d6-triathlon -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$ING_TLS" == "triathlon-tls" ] && [ "$ING_HOST" == "triathlon.k8s.local" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress triathlon-ingress with TLS termination verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress TLS or host mismatch (tls=$ING_TLS, host=$ING_HOST).${NC}"
fi

# Task 3: NetworkPolicy backend-isolation
NP_TARGET=$(ssh controlplane 'kubectl get netpol backend-isolation -n w7d6-triathlon -o jsonpath="{.spec.podSelector.matchLabels.app}" 2>/dev/null || echo "None"')
NP_ALLOW=$(ssh controlplane 'kubectl get netpol backend-isolation -n w7d6-triathlon -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.app}" 2>/dev/null || echo "None"')
if [ "$NP_TARGET" == "api-backend" ] && [ "$NP_ALLOW" == "web-frontend" ]; then
  echo -e "${GREEN}[PASS] Task 3: NetworkPolicy backend-isolation correctly restricts traffic.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NetworkPolicy rule mismatch (target=$NP_TARGET, allow=$NP_ALLOW).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d6-cka${NC}"
  exit 1
fi
