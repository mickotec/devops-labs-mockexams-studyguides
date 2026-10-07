#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d5-lfcs: Mandatory Access Control: SELinux & AppArmor...${NC}"
SCORE=0; TOTAL=2
# Task 1: apparmor_summary.txt
if [ -f /var/tmp/apparmor_summary.txt ] && grep -qiE "profiles are in enforce mode|profiles are loaded" /var/tmp/apparmor_summary.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/apparmor_summary.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/apparmor_summary.txt missing or invalid.${NC}"
fi

# Task 2: apparmor_profiles.txt
if [ -f /var/tmp/apparmor_profiles.txt ] && [ $(wc -l < /var/tmp/apparmor_profiles.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/apparmor_profiles.txt contains profile listings.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/apparmor_profiles.txt missing or has fewer than 5 entries.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d5-lfcs${NC}"
  exit 1
fi
