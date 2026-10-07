#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d1-cka: Troubleshooting: Control Plane & Applications...${NC}"
SCORE=0; TOTAL=3
# Task 1: Static pod running
WATCHDOG_PHASE=$(ssh controlplane 'kubectl get pod -n default -l "" 2>/dev/null | grep broken-watchdog | awk '''{print $3}''' || echo "NotFound"')
if ssh controlplane 'kubectl get pods -A | grep broken-watchdog | grep -q Running'; then
  echo -e "${GREEN}[PASS] Task 1: Static pod broken-watchdog is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Static pod broken-watchdog not Running (status: $WATCHDOG_PHASE).${NC}"
fi

# Task 2: db-connector running with DB_HOST
DBC_PHASE=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
DBC_ENV=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.spec.containers[0].env[?(@.name=="DB_HOST")].value}" 2>/dev/null || echo "None"')
if [ "$DBC_PHASE" == "Running" ] && [ "$DBC_ENV" == "10.0.0.1" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod db-connector Running with DB_HOST=10.0.0.1.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: db-connector phase=$DBC_PHASE, DB_HOST=$DBC_ENV.${NC}"
fi

# Task 3: apiserver log export
if ssh controlplane 'test -s /opt/k8s/apiserver_log_sample.txt && [ $(wc -l < /opt/k8s/apiserver_log_sample.txt) -ge 10 ]'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/apiserver_log_sample.txt contains log diagnostics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/apiserver_log_sample.txt missing or has fewer than 10 lines.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d1-cka${NC}"
  exit 1
fi
