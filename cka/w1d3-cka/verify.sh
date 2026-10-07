#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d3-cka: Pod Internals & YAML Architecture...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'fintech'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'fintech' is Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'fintech' not found or inactive.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Repaired Pod 'transaction-processor'...${NC}"
POD1=$(ssh controlplane 'kubectl get pod transaction-processor -n fintech -o jsonpath="{.status.phase}_{.spec.containers[0].resources.limits.memory}_{.spec.containers[0].env[0].name}" 2>/dev/null || echo "NotFound"')
if [[ "$POD1" == Running* ]] && echo "$POD1" | grep -q "128Mi"; then
  echo -e "${GREEN}[PASS] Pod 'transaction-processor' is Running with validated resources and env schema.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'transaction-processor' not running or specification invalid. Status: '$POD1'.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Streamer pod 'event-streamer'...${NC}"
POD2=$(ssh controlplane 'kubectl get pod event-streamer -n fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_CHECK=$(ssh controlplane 'kubectl exec -n fintech event-streamer -- cat /tmp/stream.log 2>/dev/null | grep STREAM || true')

if [ "$POD2" == "Running" ] && [ -n "$LOG_CHECK" ]; then
  echo -e "${GREEN}[PASS] Pod 'event-streamer' is Running and streaming logs successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'event-streamer' not running or /tmp/stream.log missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d3-cka${NC}"
  exit 1
fi
