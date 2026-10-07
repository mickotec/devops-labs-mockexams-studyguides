#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d5-lfcs: Remote Filesystems: NFS & Storage Monitoring...${NC}"
SCORE=0; TOTAL=2
# Task 1: check-disk.sh exists and produces output
if [ -x /usr/local/bin/check-disk.sh ]; then
  sudo /usr/local/bin/check-disk.sh
  if [ -f /var/tmp/disk_audit.txt ] && [ -s /var/tmp/disk_audit.txt ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/check-disk.sh generated /var/tmp/disk_audit.txt.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/tmp/disk_audit.txt not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/check-disk.sh missing or not executable.${NC}"
fi

# Task 2: check headers
if [ -f /var/tmp/disk_audit.txt ] && grep -qiE "Filesystem|Use%" /var/tmp/disk_audit.txt; then
  echo -e "${GREEN}[PASS] Task 2: Disk audit report format verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Report format missing headers.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d5-lfcs${NC}"
  exit 1
fi
