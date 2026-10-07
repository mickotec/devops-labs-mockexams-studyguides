#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d2-lfcs: Filesystems & Boot Mounting (/etc/fstab)...${NC}"
SCORE=0; TOTAL=2
# Task 1 & 2: Mounted filesystem
IS_MOUNTED=$(findmnt /mnt/data_store -o FSTYPE,OPTIONS -n 2>/dev/null || true)
if echo "$IS_MOUNTED" | grep -q "ext4" && echo "$IS_MOUNTED" | grep -q "noatime"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/data_store is mounted with ext4 and noatime.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/data_store not mounted or missing noatime option: $IS_MOUNTED.${NC}"
fi

# Task 2: /etc/fstab has UUID entry
if grep -qiE "UUID=.*\/mnt\/data_store.*ext4.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab configured with UUID and persistent options.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing proper UUID entry for /mnt/data_store.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d2-lfcs${NC}"
  exit 1
fi
