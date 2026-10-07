#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d1-lfcs: Consoles, Navigation & System Documentation...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Documentation extraction files...${NC}"
if [ -f /var/tmp/lfcs-doc-search.txt ] && grep -qiE "fdisk|parted|gdisk" /var/tmp/lfcs-doc-search.txt && grep -qiE "passwd|shadow" /var/tmp/lfcs-doc-search.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/lfcs-doc-search.txt exists and contains expected search matches.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs-doc-search.txt missing or lacks search results.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory navigation tree & evidence...${NC}"
if [ -f /var/tmp/lfcs/a/b/c/d/e/evidence.txt ]; then
  echo -e "${GREEN}[PASS] Nested navigation structure and evidence file verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs/a/b/c/d/e/evidence.txt not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /usr/local/bin/quickman script functionality...${NC}"
if [ -x /usr/local/bin/quickman ]; then
  OUTPUT=$(/usr/local/bin/quickman useradd 2>&1 || true)
  if echo "$OUTPUT" | grep -qi "SYNOPSIS" && echo "$OUTPUT" | grep -qi "NAME"; then
    echo -e "${GREEN}[PASS] /usr/local/bin/quickman successfully extracts NAME and SYNOPSIS non-interactively.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] quickman did not output expected NAME and SYNOPSIS headers.${NC}"
  fi
else
  echo -e "${RED}[FAIL] /usr/local/bin/quickman does not exist or is not executable.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d1-lfcs${NC}"
  exit 1
fi
