#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d6-lfcs: Certification Gate Review & Readiness Audit...${NC}"
SCORE=0; TOTAL=4
# Task 1: Storage audit log exists
if [ -s /var/log/storage_audit.log ] && grep -q "/" /var/log/storage_audit.log; then
  echo -e "${GREEN}[PASS] Task 1: /var/log/storage_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/log/storage_audit.log missing or empty.${NC}"
fi

# Task 2: Security audit log exists
if [ -s /var/log/security_audit.log ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/log/security_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/log/security_audit.log missing or empty.${NC}"
fi

# Task 3: Backup script and archive
if [ -x /usr/local/bin/system_backup.sh ] && [ -s /var/backups/etc_backup_audit.tar.gz ] && tar -tzf /var/backups/etc_backup_audit.tar.gz >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 3: /usr/local/bin/system_backup.sh and /var/backups/etc_backup_audit.tar.gz verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Backup script or archive missing/corrupt.${NC}"
fi

# Task 4: Student ssh permissions
SSH_PERM=$(stat -c "%a" /home/student/.ssh 2>/dev/null || echo "000")
AUTH_PERM=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$SSH_PERM" == "700" ] && [ "$AUTH_PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 4: /home/student/.ssh permissions (700) and authorized_keys (600) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Permissions incorrect (.ssh=$SSH_PERM, authorized_keys=$AUTH_PERM).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d6-lfcs${NC}"
  exit 1
fi
