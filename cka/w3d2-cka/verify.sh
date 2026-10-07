#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d2-cka: Taints, Tolerations & Node Affinity...${NC}"
SCORE=0; TOTAL=3
# Task 1: Taint on node01
TAINT=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.taints[?(@.key=="workload")].value}" 2>/dev/null || echo "None"')
if [ "$TAINT" == "critical" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node node01 tainted with workload=critical:NoSchedule.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Taint not found on node01.${NC}"
fi

# Task 2: critical-processor on node01
NODE_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_CP" == "node01" ] && [ "$STATUS_CP" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: critical-processor running on tainted node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-processor status=$STATUS_CP on node=$NODE_CP (expected Running on node01).${NC}"
fi

# Task 3: data-collector node affinity to node02
NODE_DC=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
AFF_KEY=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key}" 2>/dev/null || echo "None"')
if [ "$NODE_DC" == "node02" ] && [ "$AFF_KEY" == "kubernetes.io/hostname" ]; then
  echo -e "${GREEN}[PASS] Task 3: data-collector configured with nodeAffinity running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: data-collector node=$NODE_DC or affinity key=$AFF_KEY incorrect.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d2-cka${NC}"
  exit 1
fi
