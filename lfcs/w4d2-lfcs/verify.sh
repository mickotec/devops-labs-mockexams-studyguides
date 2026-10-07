#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d2-lfcs: Task Scheduling with Cron and At...${NC}"
SCORE=0; TOTAL=3
# Task 1: /etc/cron.d/sync-audit
if [ -f /etc/cron.d/sync-audit ] && grep -qiE "\*/15\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/sync-audit; then
  echo -e "${GREEN}[PASS] Task 1: /etc/cron.d/sync-audit configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/cron.d/sync-audit missing or syntax incorrect.${NC}"
fi

# Task 2: student user crontab
STUDENT_CRON=$(crontab -u student -l 2>/dev/null || true)
if echo "$STUDENT_CRON" | grep -qiE "30\s+3\s+\*\s+\*\s+\*"; then
  echo -e "${GREEN}[PASS] Task 2: User student crontab configured for 03:30 AM.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: student crontab missing or schedule incorrect.${NC}"
fi

# Task 3: /etc/at.allow
if [ -f /etc/at.allow ] && grep -q "^student$" /etc/at.allow; then
  echo -e "${GREEN}[PASS] Task 3: /etc/at.allow restricts access to student.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/at.allow missing or does not specify student.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d2-lfcs${NC}"
  exit 1
fi
