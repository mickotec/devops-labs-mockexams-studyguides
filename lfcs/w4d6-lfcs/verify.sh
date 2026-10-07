#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d6-lfcs: Week 4 System Automation & Maintenance Triathlon...${NC}"
SCORE=0; TOTAL=3
# Task 1: script exists and works
if [ -x /usr/local/bin/log-auditor.sh ]; then
  sudo /usr/local/bin/log-auditor.sh
  if [ -f /var/log/audit/summary.log ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/log-auditor.sh executed and generated summary.log.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/log/audit/summary.log not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/log-auditor.sh missing or not executable.${NC}"
fi

# Task 2: cron.d file
if [ -f /etc/cron.d/log-audit ] && grep -qiE "\*/30\s+\*\s+\*\s+\*\s+\*\s+root" /etc/cron.d/log-audit; then
  echo -e "${GREEN}[PASS] Task 2: /etc/cron.d/log-audit cron schedule verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/cron.d/log-audit missing or invalid schedule.${NC}"
fi

# Task 3: package hold
if apt-mark showhold | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 3: Package tar is held.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Package tar is not held.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d6-lfcs${NC}"
  exit 1
fi
