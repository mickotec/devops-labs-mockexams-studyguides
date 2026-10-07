#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d5-lfcs: Timed Mock Exam 4 & Final Speed Marathon...${NC}"
SCORE=0; TOTAL=4
# Task 1: systemd timer active
TIMER_STATUS=$(systemctl is-active tmp_cleanup.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_STATUS" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: tmp_cleanup.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: tmp_cleanup.timer status is $TIMER_STATUS (expected active).${NC}"
fi

# Task 2: limits file
if [ -f /etc/security/limits.d/99-student-limits.conf ] && grep -q "student.*nofile.*65535" /etc/security/limits.d/99-student-limits.conf && grep -q "student.*nproc.*2048" /etc/security/limits.d/99-student-limits.conf; then
  echo -e "${GREEN}[PASS] Task 2: Process limits in /etc/security/limits.d/99-student-limits.conf verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Process limits missing or incorrect in 99-student-limits.conf.${NC}"
fi

# Task 3: net-speed0 MTU 1400, IP, UP
MTU_VAL=$(ip link show dev net-speed0 2>/dev/null | grep -o "mtu 1400" || echo "")
IP_VAL=$(ip addr show dev net-speed0 2>/dev/null | grep -o "10.99.1.1/24" || echo "")
if [ "$MTU_VAL" == "mtu 1400" ] && [ "$IP_VAL" == "10.99.1.1/24" ]; then
  echo -e "${GREEN}[PASS] Task 3: net-speed0 MTU 1400 and IP 10.99.1.1/24 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: net-speed0 MTU or IP incorrect (mtu=$MTU_VAL, ip=$IP_VAL).${NC}"
fi

# Task 4: logrotate config test
if [ -f /etc/logrotate.d/mock4_logs ] && sudo logrotate -d /etc/logrotate.d/mock4_logs >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 4: Logrotate configuration /etc/logrotate.d/mock4_logs syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /etc/logrotate.d/mock4_logs missing or syntax error.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d5-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d5-lfcs${NC}"
  exit 1
fi
