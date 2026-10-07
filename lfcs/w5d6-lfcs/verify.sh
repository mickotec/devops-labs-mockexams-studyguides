#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d6-lfcs: Security Audit, User Quarantine & Recovery...${NC}"
SCORE=0; TOTAL=3
# Task 1: hacked_service quarantined
SHELL_HS=$(getent passwd hacked_service | cut -d: -f7 || echo "")
CHAGE_EXP=$(chage -l hacked_service | grep "Account expires" | awk -F: '{print $2}' | tr -d ' ' || echo "")
if [[ "$SHELL_HS" =~ (nologin|false) ]] && [ "$CHAGE_EXP" != "never" ]; then
  echo -e "${GREEN}[PASS] Task 1: hacked_service account is quarantined (shell=$SHELL_HS, expired).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: hacked_service still has shell $SHELL_HS or not expired ($CHAGE_EXP).${NC}"
fi

# Task 2: sudoers valid
if sudo visudo -c >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Sudoers configuration syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Sudoers configuration syntax error.${NC}"
fi

# Task 3: sysctl
SYNC=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
RPF=$(sysctl -n net.ipv4.conf.all.rp_filter 2>/dev/null || echo "0")
if [ "$SYNC" == "1" ] && [ "$RPF" == "1" ]; then
  echo -e "${GREEN}[PASS] Task 3: Kernel security parameters active (syncookies=1, rp_filter=1).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Parameters not set (syncookies=$SYNC, rp_filter=$RPF).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d6-lfcs${NC}"
  exit 1
fi
