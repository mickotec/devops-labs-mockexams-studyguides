#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d5-cka: Kubectl Explain & Declarative Workflow...${NC}"
SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1: Schema paths documented...${NC}"
PATHS=$(ssh controlplane 'cat /opt/k8s/schema-paths.txt 2>/dev/null || true')
if echo "$PATHS" | grep -qi "capabilities" && echo "$PATHS" | grep -qi "terminationGracePeriodSeconds"; then
  echo -e "${GREEN}[PASS] Schema paths documented in /opt/k8s/schema-paths.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/schema-paths.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Declarative secure-pod...${NC}"
SEC_POD=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.spec.containers[0].securityContext.runAsNonRoot}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_POD" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] secure-nginx is Running with runAsNonRoot=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] secure-nginx: runAsNonRoot=$SEC_POD, phase=$PHASE.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d5-cka${NC}"
  exit 1
fi
