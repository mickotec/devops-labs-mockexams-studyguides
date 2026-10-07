#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d4-cka: Namespaces & DNS Resolution Inside Clusters...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Service in database-ns...${NC}"
SVC=$(ssh controlplane 'kubectl get svc mysql-svc -n database-ns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Service mysql-svc Active in database-ns ($SVC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service mysql-svc missing in database-ns.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod tester in frontend-ns...${NC}"
POD_STATUS=$(ssh controlplane 'kubectl get pod tester -n frontend-ns -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Pod tester is Running in frontend-ns.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod tester status: $POD_STATUS.${NC}"
fi

echo -e "${BOLD}Checking Task 3: DNS resolution inside tester...${NC}"
DNS_OUT=$(ssh controlplane 'kubectl exec -n frontend-ns tester -- cat /tmp/dns-record.txt 2>/dev/null || true')
if echo "$DNS_OUT" | grep -q "database-ns.svc.cluster.local"; then
  echo -e "${GREEN}[PASS] Cross-namespace DNS lookup verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /tmp/dns-record.txt in tester lacks FQDN lookup.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d4-cka${NC}"
  exit 1
fi
