#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d1-lfcs: Local User Management & /etc/passwd...${NC}"
SCORE=0; TOTAL=3
# Task 1: devops_user UID and shell
USER_INFO=$(getent passwd devops_user 2>/dev/null || true)
if echo "$USER_INFO" | grep -q ":1600:" && echo "$USER_INFO" | grep -q "/bin/bash"; then
  echo -e "${GREEN}[PASS] Task 1: devops_user created with UID 1600 and /bin/bash shell.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: devops_user missing or UID/shell incorrect: $USER_INFO.${NC}"
fi

# Task 2: chage settings
CHAGE_INFO=$(chage -l devops_user 2>/dev/null || true)
if echo "$CHAGE_INFO" | grep -qi "Dec 31, 2027" && echo "$CHAGE_INFO" | grep -q "90"; then
  echo -e "${GREEN}[PASS] Task 2: Password aging and expiry configured for devops_user.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: chage settings missing or incorrect.${NC}"
fi

# Task 3: test_lock_user locked
SHADOW_STAT=$(sudo passwd -S test_lock_user 2>/dev/null || true)
if echo "$SHADOW_STAT" | grep -qiE " L |locked"; then
  echo -e "${GREEN}[PASS] Task 3: test_lock_user account is locked.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: test_lock_user is not locked: $SHADOW_STAT.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d1-lfcs${NC}"
  exit 1
fi
