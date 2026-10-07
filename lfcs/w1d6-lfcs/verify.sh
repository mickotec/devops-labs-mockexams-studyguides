#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d6-lfcs: Week 1 Consolidation & Permission Security Triathlon...${NC}"
SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Secure vault directories...${NC}"
PERM_V=$(sudo stat -c '%a' /srv/secure_vault 2>/dev/null || echo "0")
PERM_I=$(sudo stat -c '%a' /srv/secure_vault/incoming 2>/dev/null || echo "0")
GRP_V=$(sudo stat -c '%G' /srv/secure_vault 2>/dev/null || echo "none")

if [ "$GRP_V" == "sysadmins" ] && [[ "$PERM_V" =~ ^2 ]] && [[ "$PERM_I" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /srv/secure_vault (SGID, sysadmins) and /incoming (Sticky) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Vault permissions incorrect: vault=$PERM_V, group=$GRP_V, incoming=$PERM_I.${NC}"
fi

echo -e "${BOLD}Checking Task 2: SUID audit...${NC}"
if [ -f /var/tmp/suid_audit.txt ] && grep -q "tool_suid" /var/tmp/suid_audit.txt && ! grep -q "tool_normal" /var/tmp/suid_audit.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/suid_audit.txt correctly identified SUID binary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/suid_audit.txt missing or incorrect.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Relative symlink...${NC}"
LINK=$(sudo readlink /srv/secure_vault/configs/current.conf 2>/dev/null || true)
if [ "$LINK" == "../storage/vault.conf" ]; then
  echo -e "${GREEN}[PASS] Relative symlink current.conf points to ../storage/vault.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Relative symlink missing or invalid: '$LINK'.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Tar backup...${NC}"
if [ -f /var/backups/vault_initial.tar.gz ] && tar -tzf /var/backups/vault_initial.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] /var/backups/vault_initial.tar.gz exists and is a valid tar.gz archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/vault_initial.tar.gz missing or invalid archive.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d6-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d6-lfcs${NC}"
  exit 1
fi
