#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d5-lfcs: Archiving, Compression & Remote Backups...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/systemd_backup.tar.gz...${NC}"
if [ -f /var/tmp/systemd_backup.tar.gz ] && tar -tzf /var/tmp/systemd_backup.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Gzip tar archive created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_backup.tar.gz missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Extracted directory...${NC}"
if [ -d /var/tmp/extracted_systemd/etc/systemd ] || [ -d /var/tmp/extracted_systemd/systemd ]; then
  echo -e "${GREEN}[PASS] Archive extracted to target directory.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Extracted directory structure missing.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/archive_manifest.txt...${NC}"
if [ -f /var/tmp/archive_manifest.txt ] && grep -q "system.conf" /var/tmp/archive_manifest.txt; then
  echo -e "${GREEN}[PASS] Archive manifest verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/archive_manifest.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d5-lfcs${NC}"
  exit 1
fi
