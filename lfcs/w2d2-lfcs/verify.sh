#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d2-lfcs: Text Processing: Grep & Regular Expressions...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/auth_ips.txt...${NC}"
if [ -f /var/tmp/auth_ips.txt ] && grep -q "192.168.1.50" /var/tmp/auth_ips.txt && grep -q "10.0.0.15" /var/tmp/auth_ips.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/auth_ips.txt contains extracted IP addresses.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/auth_ips.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/pam_rules.txt...${NC}"
if [ -f /var/tmp/pam_rules.txt ] && [ -s /var/tmp/pam_rules.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/pam_rules.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/pam_rules.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/error_count.txt...${NC}"
if [ -f /var/tmp/error_count.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/error_count.txt)" == "4" ]; then
  echo -e "${GREEN}[PASS] Error count matched expected count of 4.${NC}"
  SCORE=$((SCORE + 1))
else
  ACTUAL=$(cat /var/tmp/error_count.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Error count was '$ACTUAL' (expected 4).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d2-lfcs${NC}"
  exit 1
fi
