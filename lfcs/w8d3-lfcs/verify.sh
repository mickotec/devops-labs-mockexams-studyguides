#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d3-lfcs: Timed Mock Exam 2 (Strict Exam Conditions)...${NC}"
SCORE=0; TOTAL=4
# Task 1: tar archive exists and valid
if [ -s /var/tmp/etc_configs.tar.gz ] && tar -tzf /var/tmp/etc_configs.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/etc_configs.tar.gz is a valid gzip archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/etc_configs.tar.gz missing or invalid archive.${NC}"
fi

# Task 2: swap active
if swapon --show | grep -q "/swapfile_mock2"; then
  echo -e "${GREEN}[PASS] Task 2: Swap file /swapfile_mock2 active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /swapfile_mock2 not active in swapon.${NC}"
fi

# Task 3: nice +10 process
NICE_VAL=$(ps -eo nice,cmd | grep "sleep 7200" | grep -v grep | awk '{print $1}' | head -n 1 || echo "")
if [ "$NICE_VAL" == "10" ]; then
  echo -e "${GREEN}[PASS] Task 3: sleep 7200 running with nice priority +10.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: sleep 7200 nice value is '$NICE_VAL' (expected 10).${NC}"
fi

# Task 4: log count integer
if [ -s /var/tmp/auth_summary.txt ] && grep -E -q '^[0-9]+$' /var/tmp/auth_summary.txt; then
  echo -e "${GREEN}[PASS] Task 4: /var/tmp/auth_summary.txt contains valid count: $(cat /var/tmp/auth_summary.txt).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/tmp/auth_summary.txt missing or not an integer.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d3-lfcs${NC}"
  exit 1
fi
