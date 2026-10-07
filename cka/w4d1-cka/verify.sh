#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d1-cka: Commands & Arguments (Docker vs Kubernetes)...${NC}"
SCORE=0; TOTAL=2
# Task 1: custom-streamer
LOGS_CS=$(ssh controlplane 'kubectl logs custom-streamer -n w4d1-cmd --tail=5 2>/dev/null || true')
PHASE_CS=$(ssh controlplane 'kubectl get pod custom-streamer -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_CS" == "Running" ] && echo "$LOGS_CS" | grep -q "STREAMING_EVENT"; then
  echo -e "${GREEN}[PASS] Task 1: custom-streamer is Running and streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: custom-streamer status=$PHASE_CS or logs empty.${NC}"
fi

# Task 2: env-interpolator
LOGS_EI=$(ssh controlplane 'kubectl logs env-interpolator -n w4d1-cmd 2>/dev/null || true')
PHASE_EI=$(ssh controlplane 'kubectl get pod env-interpolator -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_EI" == "Running" ] && echo "$LOGS_EI" | grep -q "Initialized as processor"; then
  echo -e "${GREEN}[PASS] Task 2: env-interpolator is Running with interpolated variable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env-interpolator status=$PHASE_EI or logs missing 'Initialized as processor'.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d1-cka${NC}"
  exit 1
fi
