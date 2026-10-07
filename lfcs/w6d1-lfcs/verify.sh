#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d1-lfcs: Storage Partitions (MBR vs GPT) & Swap...${NC}"
SCORE=0; TOTAL=2
# Task 1: Swap file permissions and active
SWAP_ACTIVE=$(swapon --show | grep "/var/tmp/swapfile_extra" || true)
PERM=$(stat -c "%a" /var/tmp/swapfile_extra 2>/dev/null || echo "0")

if [ -n "$SWAP_ACTIVE" ] && [ "$PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/swapfile_extra active as swap with permissions 600.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Swap file inactive or permissions=$PERM (expected 600).${NC}"
fi

# Task 2: /etc/fstab entry
if grep -q "/var/tmp/swapfile_extra.*swap" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab contains persistent swap entry.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing entry for /var/tmp/swapfile_extra.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d1-lfcs${NC}"
  exit 1
fi
