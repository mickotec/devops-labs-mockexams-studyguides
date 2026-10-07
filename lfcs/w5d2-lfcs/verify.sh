#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d2-lfcs: Groups, Sudo Privileges & Visudo...${NC}"
SCORE=0; TOTAL=2
# Task 1: sysaudit group and student member
GRP_GID=$(getent group sysaudit | cut -d: -f3 || echo "0")
if [ "$GRP_GID" == "2800" ] && id -Gn student | grep -q "sysaudit"; then
  echo -e "${GREEN}[PASS] Task 1: Group sysaudit (GID 2800) created and student is member.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Group sysaudit missing or student not member.${NC}"
fi

# Task 2: sudoers drop-in validation
if [ -f /etc/sudoers.d/90-sysaudit ] && sudo visudo -cf /etc/sudoers.d/90-sysaudit >/dev/null 2>&1; then
  if grep -q "%sysaudit.*NOPASSWD.*journalctl" /etc/sudoers.d/90-sysaudit; then
    echo -e "${GREEN}[PASS] Task 2: Sudoers rule validated for %sysaudit with NOPASSWD for journalctl.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 2: Rule content does not grant NOPASSWD for journalctl to %sysaudit.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 2: /etc/sudoers.d/90-sysaudit missing or syntax error.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d2-lfcs${NC}"
  exit 1
fi
