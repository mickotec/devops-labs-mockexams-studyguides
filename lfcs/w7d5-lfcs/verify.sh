#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d5-lfcs: SSH Hardening, Key Auth & Time Sync...${NC}"
SCORE=0; TOTAL=3
# Task 1: Key exists, 4096 bit, authorized_keys has 0600
KEY_BITS=$(ssh-keygen -l -f /home/student/.ssh/id_admin_rsa 2>/dev/null | awk '{print $1}')
AUTH_PERMS=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$KEY_BITS" == "4096" ] && [ "$AUTH_PERMS" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: 4096-bit SSH key generated and authorized_keys permissions verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Key bits=$KEY_BITS (exp 4096), authorized_keys perms=$AUTH_PERMS (exp 600).${NC}"
fi

# Task 2: sshd hardening drop-in and test
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -q "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf && grep -q "MaxAuthTries 3" /etc/ssh/sshd_config.d/99-hardening.conf && sudo sshd -t; then
  echo -e "${GREEN}[PASS] Task 2: /etc/ssh/sshd_config.d/99-hardening.conf verified and sshd -t passed.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: sshd hardening configuration missing or syntax test failed.${NC}"
fi

# Task 3: NTP active
NTP_STATUS=$(timedatectl show -p NTP --value 2>/dev/null || echo "no")
if [ "$NTP_STATUS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 3: System NTP synchronization is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NTP synchronization is $NTP_STATUS (expected yes).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d5-lfcs${NC}"
  exit 1
fi
