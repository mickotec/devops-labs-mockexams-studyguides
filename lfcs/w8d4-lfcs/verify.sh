#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d4-lfcs: Timed Mock Exam 3 (Strict Exam Conditions)...${NC}"
SCORE=0; TOTAL=4
# Task 1: ACL on /var/mock3_shared
ACL_CHK=$(getfacl /var/mock3_shared 2>/dev/null || true)
if echo "$ACL_CHK" | grep -q "user:student:rwx" && echo "$ACL_CHK" | grep -q "default:user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 1: ACL and default ACL for user student verified on /var/mock3_shared.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ACL missing on /var/mock3_shared.${NC}"
fi

# Task 2: SUID audit
if [ -s /var/tmp/suid_binaries.txt ] && grep -q "/usr/bin/" /var/tmp/suid_binaries.txt; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/suid_binaries.txt contains SUID executable paths.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/suid_binaries.txt missing or empty.${NC}"
fi

# Task 3: dummy kernel module loaded and persistent
MOD_LOADED=$(lsmod | grep -q "^dummy" && echo "yes" || echo "no")
MOD_CONF=$(grep -E "^dummy" /etc/modules-load.d/dummy.conf 2>/dev/null || true)
if [ "$MOD_LOADED" == "yes" ] && [ -n "$MOD_CONF" ]; then
  echo -e "${GREEN}[PASS] Task 3: dummy kernel module active and configured in /etc/modules-load.d/dummy.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: dummy module not loaded or persistent config missing.${NC}"
fi

# Task 4: OUTPUT drop rule
if sudo iptables -S OUTPUT | grep -q -- "-d 198.51.100.1/32 -p tcp -m tcp --dport 443 -j DROP\|-d 198.51.100.1 -p tcp --dport 443 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 4: Iptables OUTPUT drop rule for 198.51.100.1:443 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Iptables OUTPUT drop rule missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d4-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d4-lfcs${NC}"
  exit 1
fi
