#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d2-lfcs: Network Bonding & Bridging...${NC}"
SCORE=0; TOTAL=3
# Task 1: Bridge br0 has IP 192.168.100.1/24 and is up
if ip addr show dev br0 2>/dev/null | grep -q "192.168.100.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br0 exists with IP 192.168.100.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br0 missing or IP 192.168.100.1/24 not assigned.${NC}"
fi

# Task 2: veth pair exists
if ip link show dev veth-guest >/dev/null 2>&1 && ip link show dev veth-host >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Virtual ethernet pair veth-host and veth-guest created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth pair missing.${NC}"
fi

# Task 3: veth-host attached to br0 as master
MASTER=$(ip link show dev veth-host 2>/dev/null | grep -o "master br0" || true)
if [ "$MASTER" == "master br0" ]; then
  echo -e "${GREEN}[PASS] Task 3: veth-host attached to master bridge br0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: veth-host master is not br0.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d2-lfcs${NC}"
  exit 1
fi
