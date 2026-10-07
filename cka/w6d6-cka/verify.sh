#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d6-cka: Security & Storage Lab Triathlon...${NC}"
SCORE=0; TOTAL=3
# Task 1: RBAC check
CAN_SEC=$(ssh controlplane 'kubectl auth can-i list secrets -n w6-milestone --as=system:serviceaccount:w6-milestone:vault-operator 2>/dev/null || echo "no"')
if [ "$CAN_SEC" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: vault-operator authorized to list secrets in w6-milestone.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: vault-operator cannot list secrets.${NC}"
fi

# Task 2: PVC bound
PVC_ST=$(ssh controlplane 'kubectl get pvc m6-pvc -n w6-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_ST" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim m6-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: m6-pvc status is $PVC_ST (expected Bound).${NC}"
fi

# Task 3: Pod flag.txt
FLAG=$(ssh controlplane 'kubectl exec vault-pod -n w6-milestone -- cat /data/flag.txt 2>/dev/null || true')
if [ "$FLAG" == "Milestone6Complete" ]; then
  echo -e "${GREEN}[PASS] Task 3: vault-pod running with volume mount and verified flag.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /data/flag.txt mismatch: '$FLAG'.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d6-cka${NC}"
  exit 1
fi
