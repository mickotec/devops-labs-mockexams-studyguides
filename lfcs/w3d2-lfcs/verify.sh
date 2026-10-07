#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d2-lfcs: Systemd Targets & Runlevel Management...${NC}"
SCORE=0; TOTAL=3
# Task 1: default target is multi-user.target
DEF_TARGET=$(systemctl get-default 2>/dev/null || true)
if [ "$DEF_TARGET" == "multi-user.target" ]; then
  echo -e "${GREEN}[PASS] Task 1: Default target is multi-user.target.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Default target is '$DEF_TARGET' (expected multi-user.target).${NC}"
fi

# Task 2: maintenance.target unit file
if [ -f /etc/systemd/system/maintenance.target ] && grep -qi "Maintenance Mode" /etc/systemd/system/maintenance.target; then
  echo -e "${GREEN}[PASS] Task 2: /etc/systemd/system/maintenance.target created and validated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: maintenance.target missing or invalid description.${NC}"
fi

# Task 3: /var/tmp/default_target.txt
if [ -f /var/tmp/default_target.txt ] && grep -q "multi-user.target" /var/tmp/default_target.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/default_target.txt recorded accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/default_target.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d2-lfcs${NC}"
  exit 1
fi
