#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d6-cka: Week 4 App Lifecycle & Secret Security Drill...${NC}"
SCORE=0; TOTAL=3
# Task 1: secure-frontend deployment env vars
POD_NAME=$(ssh controlplane 'kubectl get pods -n w4-milestone -l app=secure-frontend -o jsonpath="{.items[0].metadata.name}" 2>/dev/null || echo "None"')
APP_MODE=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv APP_MODE 2>/dev/null || echo 'None'")
API_KEY=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv API_KEY 2>/dev/null || echo 'None'")
if [ "$APP_MODE" == "production" ] && [ "$API_KEY" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 1: Environment variables APP_MODE and API_KEY injected into workload.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Environment variables missing (APP_MODE=$APP_MODE, API_KEY=$API_KEY).${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa secure-frontend-hpa -n w4-milestone -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
if [ "$HPA_MAX" == "5" ]; then
  echo -e "${GREEN}[PASS] Task 2: secure-frontend-hpa configured with max 5 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: secure-frontend-hpa max replicas is $HPA_MAX (expected 5).${NC}"
fi

# Task 3: Volume mounted secret at /etc/auth/token
SECRET_CONTENT=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- cat /etc/auth/token/API_KEY 2>/dev/null || true")
if [ "$SECRET_CONTENT" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 3: Secret mounted successfully at /etc/auth/token.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Secret file missing at /etc/auth/token.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d6-cka${NC}"
  exit 1
fi
