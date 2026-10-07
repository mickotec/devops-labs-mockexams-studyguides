#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d3-lfcs: Packet Filtering with Firewalld & Iptables...${NC}"
SCORE=0; TOTAL=3
# Task 1: DROP rule for port 8088
if sudo iptables -S INPUT | grep -q -- "-p tcp -m tcp --dport 8088 -j DROP\|-p tcp --dport 8088 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 1: Iptables rule dropping port 8088 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DROP rule for port 8088 not found in INPUT chain.${NC}"
fi

# Task 2: ACCEPT rule for ICMP from 192.168.0.0/16
if sudo iptables -S INPUT | grep -q -- "-p icmp -m icmp --icmp-type 8 -s 192.168.0.0/16 -j ACCEPT\|-s 192.168.0.0/16.*-p icmp.*-j ACCEPT"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables rule allowing ICMP from 192.168.0.0/16 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACCEPT rule for ICMP from 192.168.0.0/16 not found in INPUT chain.${NC}"
fi

# Task 3: Rules backup file exists
if [ -s /var/tmp/iptables_backup.rules ] && grep -q "8088" /var/tmp/iptables_backup.rules; then
  echo -e "${GREEN}[PASS] Task 3: Active iptables rules successfully backed up to /var/tmp/iptables_backup.rules.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/iptables_backup.rules missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d3-lfcs${NC}"
  exit 1
fi
