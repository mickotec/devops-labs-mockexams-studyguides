#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d4-cka: Multi-Container Pod Patterns & Init Containers...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'telemetry'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'telemetry' Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'telemetry' not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sidecar Pod 'order-service'...${NC}"
C_COUNT=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.spec.containers[*].name}" 2>/dev/null || true')
PHASE=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_TEST=$(ssh controlplane 'kubectl logs -n telemetry order-service -c logger --tail=5 2>/dev/null || true')

if [ "$PHASE" == "Running" ] && echo "$C_COUNT" | grep -qw "app" && echo "$C_COUNT" | grep -qw "logger" && echo "$LOG_TEST" | grep -q "ORDER"; then
  echo -e "${GREEN}[PASS] Multi-container pod 'order-service' running and logger streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] order-service invalid or logger output missing. Phase: $PHASE, Containers: $C_COUNT.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Init Container Pod 'web-portal'...${NC}"
INIT_NAME=$(ssh controlplane 'kubectl get pod web-portal -n telemetry -o jsonpath="{.spec.initContainers[0].name}" 2>/dev/null || true')
if [ -n "$INIT_NAME" ]; then
  echo -e "${GREEN}[PASS] Init container '$INIT_NAME' defined on web-portal.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod web-portal missing or lacks init container.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d4-cka${NC}"
  exit 1
fi
