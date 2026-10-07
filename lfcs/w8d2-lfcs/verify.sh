#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d2-lfcs: Timed Mock Exam 1 (Strict Exam Conditions)...${NC}"
SCORE=0; TOTAL=4
# Task 1: auditor user and finance group
U_GID=$(id -u auditor 2>/dev/null || echo "0")
G_MEM=$(id -nG auditor 2>/dev/null || echo "")
if [ "$U_GID" == "2500" ] && echo "$G_MEM" | grep -q "finance"; then
  echo -e "${GREEN}[PASS] Task 1: User auditor (UID 2500) and group finance verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: auditor user or finance group mismatch (UID=$U_GID, groups=$G_MEM).${NC}"
fi

# Task 2: /srv/finance permissions 2770 and group finance
DIR_PERM=$(stat -c "%a" /srv/finance 2>/dev/null || echo "000")
DIR_GRP=$(stat -c "%G" /srv/finance 2>/dev/null || echo "")
if [ "$DIR_PERM" == "2770" ] && [ "$DIR_GRP" == "finance" ]; then
  echo -e "${GREEN}[PASS] Task 2: Directory /srv/finance has permissions 2770 and group finance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /srv/finance perms=$DIR_PERM (exp 2770), group=$DIR_GRP (exp finance).${NC}"
fi

# Task 3: Cron job /etc/cron.d/audit_sync
if [ -f /etc/cron.d/audit_sync ] && grep -q "30 3 \* \* \* root /bin/sync" /etc/cron.d/audit_sync; then
  echo -e "${GREEN}[PASS] Task 3: Scheduled cron job /etc/cron.d/audit_sync verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Cron job syntax or file missing in /etc/cron.d/audit_sync.${NC}"
fi

# Task 4: heartbeat.service and log
if [ -f /etc/systemd/system/heartbeat.service ] && [ -s /var/log/heartbeat.log ] && grep -q "heartbeat" /var/log/heartbeat.log; then
  echo -e "${GREEN}[PASS] Task 4: heartbeat.service verified and log generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: heartbeat.service or /var/log/heartbeat.log invalid.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d2-lfcs${NC}"
  exit 1
fi
