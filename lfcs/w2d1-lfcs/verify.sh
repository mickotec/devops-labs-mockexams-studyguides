#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d1-lfcs: File Searching with Find and Locate...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/large_logs.txt...${NC}"
if [ -f /var/tmp/large_logs.txt ] && [ -s /var/tmp/large_logs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/large_logs.txt created with entries.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/large_logs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/recent_configs.txt...${NC}"
if [ -f /var/tmp/recent_configs.txt ] && [ -s /var/tmp/recent_configs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/recent_configs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/recent_configs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/systemd_confs.txt...${NC}"
if [ -f /var/tmp/systemd_confs.txt ] && grep -q "/etc/systemd" /var/tmp/systemd_confs.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/systemd_confs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_confs.txt missing or lacks systemd configs.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d1-lfcs${NC}"
  exit 1
fi
