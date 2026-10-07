#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d1-lfcs: Containers & Virtual Machines on Linux...${NC}"
SCORE=0; TOTAL=3
# Task 1: web-container running and port mapped
if podman ps --format "{{.Names}}" 2>/dev/null | grep -q "web-container"; then
  echo -e "${GREEN}[PASS] Task 1: Container web-container is running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Container web-container is not running.${NC}"
fi

# Task 2: data-worker running and timestamps written
if [ -s /var/data/worker/timestamp.log ]; then
  echo -e "${GREEN}[PASS] Task 2: Container data-worker volume mount verified (/var/data/worker/timestamp.log).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/data/worker/timestamp.log missing or empty.${NC}"
fi

# Task 3: container IP extracted
if [ -s /var/tmp/container_ip.txt ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/container_ip.txt contains container IP details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/container_ip.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d1-lfcs${NC}"
  exit 1
fi
