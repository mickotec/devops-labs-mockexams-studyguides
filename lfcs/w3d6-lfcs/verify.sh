#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d6-lfcs: Week 3 Systemd & Process Orchestration...${NC}"
SCORE=0; TOTAL=3
# Task 1: Timer active
TIMER_ACTIVE=$(systemctl is-active cache-cleaner.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: cache-cleaner.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: cache-cleaner.timer is $TIMER_ACTIVE.${NC}"
fi

# Task 2: payment-bridge service fixed and running
SVC_ACTIVE=$(systemctl is-active payment-bridge.service 2>/dev/null || echo "inactive")
if [ "$SVC_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 2: payment-bridge.service is active (running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: payment-bridge.service is $SVC_ACTIVE.${NC}"
fi

# Task 3: limits file
if [ -f /etc/security/limits.d/50-worker.conf ] && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/50-worker.conf && grep -q "student.*hard.*nproc.*2048" /etc/security/limits.d/50-worker.conf; then
  echo -e "${GREEN}[PASS] Task 3: Security limits for student configured correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/50-worker.conf missing or values incorrect.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d6-lfcs${NC}"
  exit 1
fi
