#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d4-cka: Storage: Volumes, PV, PVC & StorageClasses...${NC}"
SCORE=0; TOTAL=3
# Task 1: PV status
PV_STAT=$(ssh controlplane 'kubectl get pv app-data-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV_STAT" == "Bound" ] || [ "$PV_STAT" == "Available" ]; then
  echo -e "${GREEN}[PASS] Task 1: PersistentVolume app-data-pv exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: app-data-pv status is $PV_STAT.${NC}"
fi

# Task 2: PVC status
PVC_STAT=$(ssh controlplane 'kubectl get pvc app-data-pvc -n w6d4-storage -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim app-data-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-data-pvc is $PVC_STAT (expected Bound).${NC}"
fi

# Task 3: storage-writer Pod and content
CONTENT=$(ssh controlplane 'kubectl exec storage-writer -n w6d4-storage -- cat /mnt/data/success.txt 2>/dev/null || true')
if [ "$CONTENT" == "StorageVerified" ]; then
  echo -e "${GREEN}[PASS] Task 3: storage-writer wrote to PV and verified data persistence.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /mnt/data/success.txt content mismatch: '$CONTENT'.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d4-cka${NC}"
  exit 1
fi
