#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d1-cka: Manual Scheduling, Labels & Selectors...${NC}"
SCORE=0; TOTAL=3
# Check Task 1: labels
L1=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.metadata.labels.disktype}" 2>/dev/null || echo "None"')
L2=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.metadata.labels.environment}" 2>/dev/null || echo "None"')
if [ "$L1" == "ssd" ] && [ "$L2" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node labels verified on node01 and node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Labels missing or incorrect (node01=$L1, node02=$L2).${NC}"
fi

# Check Task 2: storage-worker on node01
NODE_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_SW" == "node01" ] && [ "$STATUS_SW" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: storage-worker scheduled to node01 via nodeSelector and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: storage-worker node=$NODE_SW, status=$STATUS_SW (expected node01, Running).${NC}"
fi

# Check Task 3: orphan-task on node02
NODE_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_OT" == "node02" ] && [ "$STATUS_OT" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: orphan-task scheduled to node02 via nodeName.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: orphan-task node=$NODE_OT, status=$STATUS_OT (expected node02, Running).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d1-cka${NC}"
  exit 1
fi
