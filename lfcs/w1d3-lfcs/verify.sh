#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d3-lfcs: Standard Linux File Permissions...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Users & group devops_eng...${NC}"
if getent group devops_eng >/dev/null && id alice >/dev/null && id bob >/dev/null; then
  echo -e "${GREEN}[PASS] Users alice, bob and group devops_eng verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Group devops_eng or users alice/bob missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory permissions 775 / 664...${NC}"
PERM_DIR=$(stat -c '%a' /srv/data/engineering/src 2>/dev/null || echo "0")
PERM_FILE=$(stat -c '%a' /srv/data/engineering/README.md 2>/dev/null || echo "0")
GRP=$(stat -c '%G' /srv/data/engineering/README.md 2>/dev/null || echo "none")

if [ "$PERM_DIR" == "775" ] && [ "$PERM_FILE" == "664" ] && [ "$GRP" == "devops_eng" ]; then
  echo -e "${GREEN}[PASS] Recursive group devops_eng, dirs 775, files 664 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Permissions mismatch: dir=$PERM_DIR (expected 775), file=$PERM_FILE (expected 664), group=$GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /etc/profile.d/devops_umask.sh...${NC}"
if [ -f /etc/profile.d/devops_umask.sh ] && grep -q "002" /etc/profile.d/devops_umask.sh; then
  echo -e "${GREEN}[PASS] /etc/profile.d/devops_umask.sh configured with umask 002.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /etc/profile.d/devops_umask.sh missing or lacks umask 002.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d3-lfcs${NC}"
  exit 1
fi
