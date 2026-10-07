#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d4-lfcs: Dynamic LVM Volume Expansion...${NC}"
SCORE=0; TOTAL=2
# Task 1: LV Size is 200MB
LV_SZ=$(sudo lvs -o lv_size --units m --noheadings /dev/vg_expand/lv_store 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SZ" | grep -q "200"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_store extended to 200MB.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: lv_store size is $LV_SZ (expected 200MB).${NC}"
fi

# Task 2: Filesystem reflects expanded size
FS_SIZE=$(df -m /mnt/expand_store | tail -1 | awk '{print $2}' || echo "0")
if [ "$FS_SIZE" -ge 180 ]; then
  echo -e "${GREEN}[PASS] Task 2: Filesystem resized online ($FS_SIZE MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Filesystem size is $FS_SIZE MB (expected >= 180MB).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d4-lfcs${NC}"
  exit 1
fi
