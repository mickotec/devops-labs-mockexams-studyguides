#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d1-cka: Kubernetes Architecture & Container Runtimes...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: kube-scheduler health & scheduled pod...${NC}"
SCHED_STATUS=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Unknown"')
TEST_POD_STATUS=$(ssh controlplane 'kubectl get pod w1d1-pending-test -o jsonpath="{.status.phase}" 2>/dev/null || echo "Unknown"')

if [ "$SCHED_STATUS" == "Running" ] && [ "$TEST_POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] kube-scheduler is Running and w1d1-pending-test scheduled successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-scheduler is '$SCHED_STATUS' (expected Running) or w1d1-pending-test is '$TEST_POD_STATUS'.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Rogue container on node01...${NC}"
ROGUE_CHECK=$(ssh -o BatchMode=yes -o ConnectTimeout=5 node01 'sudo crictl ps -a 2>/dev/null | grep rogue-crypto-miner || true' 2>/dev/null || true)
if [ -z "$ROGUE_CHECK" ]; then
  echo -e "${GREEN}[PASS] Rogue container 'rogue-crypto-miner' has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Rogue container 'rogue-crypto-miner' is still running on node01.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Static Pod 'node01-monitor' on node01...${NC}"
STATIC_POD=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node01-monitor-node01" || true')
if [ -n "$STATIC_POD" ] && echo "$STATIC_POD" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod 'node01-monitor-node01' is running and registered with API server.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod 'node01-monitor-node01' not found or not in Running state.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d1-cka${NC}"
  exit 1
fi
