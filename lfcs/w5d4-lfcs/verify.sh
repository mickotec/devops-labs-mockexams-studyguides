#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d4-lfcs: Kernel Runtime Tuning with Sysctl...${NC}"
SCORE=0; TOTAL=2
# Task 1 & 2: sysctl settings active
IP_FWD=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
ICMP_IGN=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")

if [ "$IP_FWD" == "1" ] && [ "$ICMP_IGN" == "1" ] && [ -f /etc/sysctl.d/60-hardening.conf ]; then
  echo -e "${GREEN}[PASS] Task 1: Kernel parameters active and configured in /etc/sysctl.d/60-hardening.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Parameters not active (ip_forward=$IP_FWD, icmp_ignore=$ICMP_IGN).${NC}"
fi

if [ -f /var/tmp/kernel_params.txt ] && grep -q "net.ipv4.ip_forward = 1" /var/tmp/kernel_params.txt; then
  echo -e "${GREEN}[PASS] Task 2: Active parameters recorded in /var/tmp/kernel_params.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/kernel_params.txt missing or incomplete.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d4-lfcs${NC}"
  exit 1
fi
