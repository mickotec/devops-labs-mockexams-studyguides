#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d6-lfcs: Week 7 Linux Networking & Firewall Marathon...${NC}"
SCORE=0; TOTAL=4
# Task 1: br-marathon exists with 172.25.1.1/24
if ip addr show dev br-marathon 2>/dev/null | grep -q "172.25.1.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br-marathon verified with IP 172.25.1.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br-marathon missing or IP not set.${NC}"
fi

# Task 2: veth-m1 attached to br-marathon
if ip link show dev veth-m1 2>/dev/null | grep -q "master br-marathon"; then
  echo -e "${GREEN}[PASS] Task 2: veth-m1 attached to master br-marathon.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth-m1 master is not br-marathon.${NC}"
fi

# Task 3: iptables rules
NAT_OK=$(sudo iptables -t nat -S PREROUTING 2>/dev/null | grep -E -- "--dport 9090.*REDIRECT.*--to-ports 80" || true)
IN_OK=$(sudo iptables -S INPUT 2>/dev/null | grep -E -- "-p udp.*--dport 5353.*-j DROP" || true)
if [ -n "$NAT_OK" ] && [ -n "$IN_OK" ]; then
  echo -e "${GREEN}[PASS] Task 3: NAT port 9090 redirection and UDP 5353 drop rules verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Firewall rules missing (NAT=$NAT_OK, INPUT=$IN_OK).${NC}"
fi

# Task 4: Health script and status log
if [ -x /usr/local/bin/network_health.sh ] && grep -q "STATUS=HEALTHY" /var/log/net_marathon.status 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_health.sh and /var/log/net_marathon.status verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/log/net_marathon.status missing or status not HEALTHY.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d6-lfcs${NC}"
  exit 1
fi
