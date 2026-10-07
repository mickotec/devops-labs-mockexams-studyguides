#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d3-lfcs: Profiles, Template Environments & User Limits...${NC}"
SCORE=0; TOTAL=3
# Task 1: /etc/skel/WELCOME.txt
if [ -f /etc/skel/WELCOME.txt ] && grep -qi "All activity is monitored" /etc/skel/WELCOME.txt; then
  echo -e "${GREEN}[PASS] Task 1: /etc/skel/WELCOME.txt created and verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/skel/WELCOME.txt missing or text mismatch.${NC}"
fi

# Task 2: /etc/profile.d/corp_vars.sh
if [ -f /etc/profile.d/corp_vars.sh ] && grep -q 'CORPORATE_ENV="production"' /etc/profile.d/corp_vars.sh; then
  echo -e "${GREEN}[PASS] Task 2: /etc/profile.d/corp_vars.sh exports CORPORATE_ENV.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/profile.d/corp_vars.sh missing or variable missing.${NC}"
fi

# Task 3: limits.d
if [ -f /etc/security/limits.d/80-nofile.conf ] && grep -q "student.*soft.*nofile.*2048" /etc/security/limits.d/80-nofile.conf && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/80-nofile.conf; then
  echo -e "${GREEN}[PASS] Task 3: File limits for student configured in limits.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/80-nofile.conf missing or values incorrect.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d3-lfcs${NC}"
  exit 1
fi
