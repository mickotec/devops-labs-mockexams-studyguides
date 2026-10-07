#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d3-lfcs: Advanced Stream Analysis: Sed & Awk Fundamentals...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Awk regular users report...${NC}"
if [ -f /var/tmp/regular_users.txt ] && grep -q "UID:" /var/tmp/regular_users.txt; then
  echo -e "${GREEN}[PASS] Awk user report verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/regular_users.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sed transformations...${NC}"
CONF=$(cat /var/tmp/config_sample.ini 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 443" && echo "$CONF" | grep -q "ENVIRONMENT = Production" && ! echo "$CONF" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Sed transformations verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Transformations missing in /var/tmp/config_sample.ini.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Sales sum...${NC}"
if [ -f /var/tmp/sales_total.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/sales_total.txt)" == "90" ]; then
  echo -e "${GREEN}[PASS] Sales sum matched 90 (25 + 50 + 15).${NC}"
  SCORE=$((SCORE + 1))
else
  VAL=$(cat /var/tmp/sales_total.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Sales sum was '$VAL' (expected 90).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d3-lfcs${NC}"
  exit 1
fi
