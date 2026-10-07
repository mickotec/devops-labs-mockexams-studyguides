#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d4-lfcs: NAT, Port Redirection & Reverse Proxies...${NC}"
SCORE=0; TOTAL=3
# Task 1: IP forward enabled in sysctl and file
SYSCTL_VAL=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
if [ "$SYSCTL_VAL" == "1" ] && grep -q "net.ipv4.ip_forward.*=.*1" /etc/sysctl.d/99-ipforward.conf 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 1: IP packet forwarding enabled persistently.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: net.ipv4.ip_forward is $SYSCTL_VAL or /etc/sysctl.d/99-ipforward.conf missing.${NC}"
fi

# Task 2: iptables NAT redirection
if sudo iptables -t nat -S PREROUTING | grep -q -- "-p tcp -m tcp --dport 8080 -j REDIRECT --to-ports 80\|-p tcp --dport 8080 -j REDIRECT --to-ports 80"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables PREROUTING redirection 8080 -> 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: NAT PREROUTING redirection for port 8080 not found.${NC}"
fi

# Task 3: Reverse proxy configuration template
if [ -s /var/tmp/reverse_proxy.conf ] && grep -q "listen 8888" /var/tmp/reverse_proxy.conf && grep -q "proxy_pass http://127.0.0.1:80" /var/tmp/reverse_proxy.conf; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/reverse_proxy.conf reverse proxy configuration verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/reverse_proxy.conf missing or proxy settings incorrect.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d4-lfcs${NC}"
  exit 1
fi
