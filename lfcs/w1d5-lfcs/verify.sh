#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d5-lfcs: Pagers, Vim Mastery & Terminal Editing...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ~/.vimrc configuration...${NC}"
if [ -f ~/.vimrc ] && grep -q "tabstop=4" ~/.vimrc && grep -q "number" ~/.vimrc; then
  echo -e "${GREEN}[PASS] ~/.vimrc verified with tabstop=4 and line numbering.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.vimrc missing or lacks required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/app_legacy.conf refactoring...${NC}"
CONF=$(cat /var/tmp/app_legacy.conf 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 8443" && echo "$CONF" | grep -q "^SSL_ENABLED = true" && ! echo "$CONF" | grep -q "DEPRECATED"; then
  echo -e "${GREEN}[PASS] /var/tmp/app_legacy.conf refactored correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Configuration transformations incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/status_summary.txt...${NC}"
if [ -f /var/tmp/status_summary.txt ] && grep -q "200" /var/tmp/status_summary.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/status_summary.txt created with status counts.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/status_summary.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d5-lfcs${NC}"
  exit 1
fi
