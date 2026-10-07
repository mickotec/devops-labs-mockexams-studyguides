#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d3-lfcs: Logical Volume Management (LVM) Architecture...${NC}"
SCORE=0; TOTAL=2
# Task 1: LVM objects
LV_EXISTS=$(sudo lvs -o lv_name,vg_name --noheadings /dev/vg_database/lv_orders 2>/dev/null || echo "None")
if echo "$LV_EXISTS" | grep -q "lv_orders" && echo "$LV_EXISTS" | grep -q "vg_database"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_orders exists in vg_database.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Logical Volume /dev/vg_database/lv_orders not found.${NC}"
fi

# Task 2: Mounted
MNT_CHECK=$(findmnt /mnt/orders_data -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT_CHECK" | grep -q "lv_orders" && echo "$MNT_CHECK" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 2: /mnt/orders_data is mounted from lv_orders (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /mnt/orders_data not mounted from lv_orders: $MNT_CHECK.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d3-lfcs${NC}"
  exit 1
fi
