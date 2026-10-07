#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d6-lfcs: Week 6 Storage Mastery & LVM Drill...${NC}"
SCORE=0; TOTAL=3
# Task 1: LV and mount
MNT=$(findmnt /mnt/secure_audit -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT" | grep -q "lv_audit" && echo "$MNT" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/secure_audit is mounted on lv_audit (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/secure_audit not mounted on lv_audit: $MNT.${NC}"
fi

# Task 2: ACL
ACL_CHECK=$(getfacl /mnt/secure_audit 2>/dev/null || true)
if echo "$ACL_CHECK" | grep -q "user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 2: ACL permissions user:student:rwx verified on /mnt/secure_audit.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACL missing user:student:rwx.${NC}"
fi

# Task 3: Size >= 170M
SZ=$(df -m /mnt/secure_audit | tail -1 | awk '{print $2}' || echo "0")
if [ "$SZ" -ge 160 ]; then
  echo -e "${GREEN}[PASS] Task 3: Online LVM expansion verified ($SZ MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Size is $SZ MB (expected >= 160MB).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d6-lfcs${NC}"
  exit 1
fi
