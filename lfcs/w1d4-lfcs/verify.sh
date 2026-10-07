#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d4-lfcs: Special Permissions: SUID, SGID & Sticky Bit...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: SGID directory /opt/campaigns...${NC}"
PERM_C=$(sudo stat -c '%a' /opt/campaigns 2>/dev/null || echo "0")
GRP_C=$(sudo stat -c '%G' /opt/campaigns 2>/dev/null || echo "none")

# Check if group inheritance works
sudo -u root touch /opt/campaigns/test_file 2>/dev/null || true
TEST_GRP=$(sudo stat -c '%G' /opt/campaigns/test_file 2>/dev/null || echo "none")
sudo rm -f /opt/campaigns/test_file

if [ "$GRP_C" == "marketing" ] && [ "$TEST_GRP" == "marketing" ] && [[ "$PERM_C" =~ ^2 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns has SGID bit (perm $PERM_C) and group marketing.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns perm=$PERM_C, group=$GRP_C, test_grp=$TEST_GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sticky bit directory /opt/campaigns/incoming...${NC}"
PERM_INC=$(sudo stat -c '%a' /opt/campaigns/incoming 2>/dev/null || echo "0")
if [[ "$PERM_INC" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns/incoming has Sticky bit set (perm $PERM_INC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns/incoming lacks Sticky bit (perm $PERM_INC).${NC}"
fi

echo -e "${BOLD}Checking Task 3: World writable audit...${NC}"
if [ -f /var/tmp/world_writable_audit.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/world_writable_audit.txt created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/world_writable_audit.txt missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d4-lfcs${NC}"
  exit 1
fi
