#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d4-lfcs: I/O Redirection & Stream Multiplexing...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Separated standard streams...${NC}"
if [ -f /var/tmp/stdout.log ] && [ -f /var/tmp/stderr.log ]; then
  echo -e "${GREEN}[PASS] stdout.log and stderr.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Stream files missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Process dump and count...${NC}"
if [ -f /var/tmp/process_dump.txt ] && [ -f /var/tmp/process_count.txt ] && [ -s /var/tmp/process_count.txt ]; then
  echo -e "${GREEN}[PASS] Process dump and count verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Process dump files missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Health report via heredoc...${NC}"
if [ -f /var/tmp/health.report ] && grep -q "HOST:" /var/tmp/health.report && grep -q "KERNEL:" /var/tmp/health.report; then
  echo -e "${GREEN}[PASS] Health report generated with HOST and KERNEL.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/health.report missing or incomplete.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d4-lfcs${NC}"
  exit 1
fi
