#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d1-lfcs: Journald & System Log File Analysis...${NC}"
SCORE=0; TOTAL=3
# Task 1: system_errors.log
if [ -f /var/tmp/system_errors.log ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_errors.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_errors.log missing.${NC}"
fi

# Task 2: ssh_service.log has entries
if [ -f /var/tmp/ssh_service.log ] && [ -s /var/tmp/ssh_service.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/ssh_service.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/ssh_service.log missing or empty.${NC}"
fi

# Task 3: journal_usage.txt
if [ -f /var/tmp/journal_usage.txt ] && grep -qiE "Archived|Active|take up" /var/tmp/journal_usage.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/journal_usage.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/journal_usage.txt missing or lacks usage metrics.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d1-lfcs${NC}"
  exit 1
fi
