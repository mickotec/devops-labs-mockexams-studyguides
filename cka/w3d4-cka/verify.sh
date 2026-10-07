#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d4-cka: DaemonSets & Static Pods Architecture...${NC}"
SCORE=0; TOTAL=2
# Task 1: DaemonSet
DESIRED=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.desiredNumberScheduled}" 2>/dev/null || echo "0"')
READY=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DESIRED" -ge 2 ] && [ "$DESIRED" == "$READY" ]; then
  echo -e "${GREEN}[PASS] Task 1: DaemonSet log-collector is fully scheduled ($READY/$DESIRED ready).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DaemonSet log-collector desired=$DESIRED, ready=$READY.${NC}"
fi

# Task 2: Static pod on node02
STATIC=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node02-telemetry-node02" || true')
if [ -n "$STATIC" ] && echo "$STATIC" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Task 2: Static pod node02-telemetry-node02 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Static pod node02-telemetry-node02 not found or not Running: $STATIC.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d4-cka${NC}"
  exit 1
fi
