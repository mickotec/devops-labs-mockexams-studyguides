#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d3-lfcs: Creating & Managing Systemd Services...${NC}"
SCORE=0; TOTAL=3
# Task 1: script exists and executable
if [ -x /usr/local/bin/worker-daemon.sh ]; then
  echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/worker-daemon.sh executable verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/worker-daemon.sh missing or not executable.${NC}"
fi

# Task 2: service file
if [ -f /etc/systemd/system/worker-daemon.service ] && grep -qi "Restart=always" /etc/systemd/system/worker-daemon.service; then
  echo -e "${GREEN}[PASS] Task 2: worker-daemon.service unit file configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Service unit file missing or Restart directive absent.${NC}"
fi

# Task 3: service is running and logging
IS_ACTIVE=$(systemctl is-active worker-daemon.service 2>/dev/null || echo "inactive")
if [ "$IS_ACTIVE" == "active" ] && [ -f /var/log/worker-daemon.log ] && [ -s /var/log/worker-daemon.log ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-daemon.service is active and writing to /var/log/worker-daemon.log.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Service is $IS_ACTIVE or /var/log/worker-daemon.log empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d3-lfcs${NC}"
  exit 1
fi
