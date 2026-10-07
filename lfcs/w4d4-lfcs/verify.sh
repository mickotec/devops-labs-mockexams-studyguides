#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d4-lfcs: Compiling Software from Source Code...${NC}"
SCORE=0; TOTAL=3
# Task 1: extracted source
if [ -f /var/tmp/src-build/hello.c ]; then
  echo -e "${GREEN}[PASS] Task 1: Source code extracted to /var/tmp/src-build/hello.c.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/src-build/hello.c not found.${NC}"
fi

# Task 2: compiled binary
if [ -x /usr/local/bin/hello-app ]; then
  echo -e "${GREEN}[PASS] Task 2: Compiled binary /usr/local/bin/hello-app exists and is executable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /usr/local/bin/hello-app missing or not executable.${NC}"
fi

# Task 3: execution output
if [ -f /var/tmp/hello_output.txt ] && grep -q "LFCS Source Compilation Successful" /var/tmp/hello_output.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/hello_output.txt verified with correct binary output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/hello_output.txt missing or output incorrect.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d4-lfcs${NC}"
  exit 1
fi
