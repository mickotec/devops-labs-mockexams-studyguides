#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d5-lfcs: System Integrity, Resource Monitoring & Top...${NC}"
SCORE=0; TOTAL=2
# Task 1: system_specs.txt
if [ -f /var/tmp/system_specs.txt ] && grep -qiE "RAM|Memory" /var/tmp/system_specs.txt && grep -qiE "CPU|Cores" /var/tmp/system_specs.txt && grep -qiE "Load" /var/tmp/system_specs.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_specs.txt contains RAM, CPU, and Load metrics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_specs.txt missing or incomplete metrics.${NC}"
fi

# Task 2: swappiness runtime and persistent
CURR_SWAP=$(sysctl -n vm.swappiness)
CONF_SWAP=$(grep -oE "vm.swappiness\s*=\s*15" /etc/sysctl.d/99-swappiness.conf 2>/dev/null || true)
if [ "$CURR_SWAP" == "15" ] && [ -n "$CONF_SWAP" ]; then
  echo -e "${GREEN}[PASS] Task 2: vm.swappiness=15 active and configured persistently in sysctl.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Runtime swappiness is $CURR_SWAP (expected 15) or config file missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d5-lfcs${NC}"
  exit 1
fi
