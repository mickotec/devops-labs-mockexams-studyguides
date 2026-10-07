#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d5-lfcs: Bash Automation & Maintenance Scripting...${NC}"
SCORE=0; TOTAL=2
# Task 1: script executable and handles arguments
if [ -x /usr/local/bin/daily-maint.sh ]; then
  ERR_OUT=$(/usr/local/bin/daily-maint.sh 2>&1 || true)
  if echo "$ERR_OUT" | grep -qi "Usage:"; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/daily-maint.sh exists, executable, and validates arguments.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: Script did not exit with Usage message when no argument was passed.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/daily-maint.sh missing or not executable.${NC}"
fi

# Task 2: log file updated
if [ -f /var/log/daily-maint.log ] && grep -qi "Processed logs" /var/log/daily-maint.log; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/daily-maint.log verified with processed logs summary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/daily-maint.log missing or missing log entry.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d5-lfcs${NC}"
  exit 1
fi
