#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d1-cka: ReplicaSets & Self-Healing Controllers...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ReplicaSet web-replicas in namespace core...${NC}"
RS_COUNT=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$RS_COUNT" == "4" ] || [ "$RS_COUNT" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet web-replicas has $RS_COUNT ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet has $RS_COUNT ready replicas (expected at least 4).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod labels and controller management...${NC}"
POD_COUNT=$(ssh controlplane 'kubectl get pods -n core -l app=web-app --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')
if [ -n "$POD_COUNT" ] && [ "$POD_COUNT" -ge 4 ]; then
  echo -e "${GREEN}[PASS] Pods matching selector app=web-app verified ($POD_COUNT running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod selector verification failed (found $POD_COUNT pods).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Scaled replicas (target: 6)...${NC}"
DESIRED=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
if [ "$DESIRED" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet scaled to 6 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet desired replicas is $DESIRED (expected 6).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d1-cka${NC}"
  exit 1
fi
