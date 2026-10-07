#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d2-lfcs: Files, Directories, Hard & Soft Links...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Relative symbolic link...${NC}"
LINK_TARGET=$(readlink /opt/link-lab/configs/active.conf 2>/dev/null || true)
if [ -L /opt/link-lab/configs/active.conf ] && [ "$LINK_TARGET" == "../storage/v2/app-v2.conf" ] && [ -f /opt/link-lab/configs/active.conf ]; then
  echo -e "${GREEN}[PASS] Relative symlink active.conf points correctly to ../storage/v2/app-v2.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] active.conf target is '$LINK_TARGET' (expected relative path '../storage/v2/app-v2.conf').${NC}"
fi

echo -e "${BOLD}Checking Task 2: Hard link and inode synchronization...${NC}"
if [ -f /opt/link-lab/backup/app-v2.conf.hl ] && [ -f /opt/link-lab/storage/v2/app-v2.conf ]; then
  INODE1=$(stat -c '%i' /opt/link-lab/storage/v2/app-v2.conf 2>/dev/null || echo "1")
  INODE2=$(stat -c '%i' /opt/link-lab/backup/app-v2.conf.hl 2>/dev/null || echo "2")
  if [ "$INODE1" == "$INODE2" ] && grep -q "BACKUP_ENABLED=true" /opt/link-lab/storage/v2/app-v2.conf; then
    echo -e "${GREEN}[PASS] Hard link shares identical inode ($INODE1) and content updated.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Inodes differ ($INODE1 vs $INODE2) or BACKUP_ENABLED missing.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Hard link /opt/link-lab/backup/app-v2.conf.hl not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Dangling links removed...${NC}"
if [ -f /var/tmp/removed_links.txt ] && ! [ -L /opt/link-lab/orphan_links/broken1.link ] && [ -L /opt/link-lab/orphan_links/valid.link ]; then
  echo -e "${GREEN}[PASS] Dangling symlinks removed and recorded in /var/tmp/removed_links.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Broken links still present or /var/tmp/removed_links.txt missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d2-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d2-lfcs${NC}"
  exit 1
fi
