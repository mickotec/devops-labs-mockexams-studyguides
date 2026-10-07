#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d1-lfcs: Linux Networking Configuration (IP & Routing)...${NC}"
SCORE=0; TOTAL=4
# Task 1: dummy0 interface exists and is up
if ip link show dummy0 2>/dev/null | grep -q "state UP\|UP"; then
  echo -e "${GREEN}[PASS] Task 1: Interface dummy0 is UP.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Interface dummy0 missing or not UP.${NC}"
fi

# Task 2: IP 10.10.20.50/24 assigned to dummy0
if ip addr show dev dummy0 2>/dev/null | grep -q "10.10.20.50/24"; then
  echo -e "${GREEN}[PASS] Task 2: IP 10.10.20.50/24 assigned to dummy0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: IP 10.10.20.50/24 not found on dummy0.${NC}"
fi

# Task 3: Route 10.200.0.0/16 exists
if ip route show 10.200.0.0/16 2>/dev/null | grep -q "dummy0"; then
  echo -e "${GREEN}[PASS] Task 3: Static route 10.200.0.0/16 via dummy0 exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Route 10.200.0.0/16 via dummy0 not found.${NC}"
fi

# Task 4: Audit script & log
if [ -x /usr/local/bin/network_audit.sh ] && [ -f /var/log/network_audit.log ] && grep -q "default" /var/log/network_audit.log && grep -q "nameserver" /var/log/network_audit.log; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_audit.sh and /var/log/network_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Audit script or log file invalid.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d1-lfcs${NC}"
  exit 1
fi
