#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d6-lfcs: Week 2 Speed Drills & Git Version Control...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Git repository initialized...${NC}"
if [ -d /srv/repo/.git ]; then
  echo -e "${GREEN}[PASS] Git repo initialized in /srv/repo.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /srv/repo/.git directory not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2 & 3: Branch merge & system.conf...${NC}"
sudo git config --system --add safe.directory /srv/repo 2>/dev/null || true
CONF=$(cat /srv/repo/system.conf 2>/dev/null || echo "None")
COMMITS=$(git -C /srv/repo rev-list --count HEAD 2>/dev/null || sudo git -C /srv/repo rev-list --count HEAD 2>/dev/null || echo "0")
if [ "$CONF" == "config=v2" ] && [ "$COMMITS" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Branch merged with config=v2 and commit history.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] system.conf: $CONF, commits: $COMMITS.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Backup archive...${NC}"
if [ -f /var/backups/repo.tar.gz ] && tar -tzf /var/backups/repo.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Repository backup archive verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/repo.tar.gz missing or invalid.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d6-lfcs${NC}"
  exit 1
fi
