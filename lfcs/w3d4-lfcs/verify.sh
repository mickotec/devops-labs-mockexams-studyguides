#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d4-lfcs: Process Diagnostics & Signal Management...${NC}"
SCORE=0; TOTAL=3
# Task 1: rogue-sim killed
if ! pgrep -f "rogue-sim" >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: Rogue process rogue-sim has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: rogue-sim process is still running.${NC}"
fi

# Task 2: batch-calc reniced to 12
NI=$(ps -eo ni,cmd | grep "batch-calc" | grep -v grep | awk '{print $1}' | head -1 || echo "0")
if [ "$NI" == "12" ]; then
  echo -e "${GREEN}[PASS] Task 2: batch-calc has nice priority 12.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: batch-calc nice value is '$NI' (expected 12).${NC}"
fi

# Task 3: process_report.txt exists with at least 5 entries
if [ -f /var/tmp/process_report.txt ] && [ $(wc -l < /var/tmp/process_report.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/process_report.txt created with memory stats.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/process_report.txt missing or has fewer than 5 lines.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d4-lfcs${NC}"
  exit 1
fi
