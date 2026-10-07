#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d4-cka: Timed Mock Exam 1 & Step-by-Step Review...${NC}"
SCORE=0; TOTAL=4
# Task 1: RBAC can-i
AUTH_CHECK=$(ssh controlplane 'kubectl auth can-i get pods --as=system:serviceaccount:w8d4-exam:deploy-bot -n w8d4-exam 2>/dev/null || echo "no"')
if [ "$AUTH_CHECK" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: RBAC permissions for deploy-bot verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: deploy-bot cannot get pods in w8d4-exam.${NC}"
fi

# Task 2: Multi-container pod
C_READY=$(ssh controlplane 'kubectl get pod app-logger -n w8d4-exam -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$C_READY" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 2: Multi-container pod app-logger has 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-logger containers ready: '$C_READY' (expected 'true true').${NC}"
fi

# Task 3: db-client env from secret
DBC_USER=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_USER=dbadmin || true')
DBC_PASS=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_PASS=SuperSecret101 || true')
if [ -n "$DBC_USER" ] && [ -n "$DBC_PASS" ]; then
  echo -e "${GREEN}[PASS] Task 3: db-client environment variables verified from secret.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: db-client environment variables missing or mismatch.${NC}"
fi

# Task 4: DaemonSet node-sentinel
DS_READY=$(ssh controlplane 'kubectl get ds node-sentinel -n w8d4-exam -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DS_READY" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 4: DaemonSet node-sentinel active on $DS_READY nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: DaemonSet node-sentinel ready pods: $DS_READY (expected >= 2).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d4-cka${NC}"
  exit 1
fi
