#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w3d1-lfcs: Linux Boot Architecture & GRUB2...${NC}"
SCORE=0; TOTAL=2
# Check Task 1: GRUB configuration and generated grub.cfg
GRUB_PARAM=$(grep 'consoleblank=600' /etc/default/grub 2>/dev/null || true)
GRUB_TIME=$(grep 'GRUB_TIMEOUT=8' /etc/default/grub 2>/dev/null || true)
GRUB_CFG=$(sudo grep 'consoleblank=600' /boot/grub/grub.cfg 2>/dev/null || true)

if [ -n "$GRUB_PARAM" ] && [ -n "$GRUB_TIME" ] && [ -n "$GRUB_CFG" ]; then
  echo -e "${GREEN}[PASS] Task 1: GRUB default params and regenerated grub.cfg verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GRUB config missing consoleblank=600, TIMEOUT=8, or update-grub not executed.${NC}"
fi

# Check Task 2: boot diagnostic report
if [ -f /var/tmp/boot_diagnostic.txt ] && grep -qiE "BOOT_IMAGE|vmlinuz|Command line" /var/tmp/boot_diagnostic.txt && grep -qiE "UUID=" /var/tmp/boot_diagnostic.txt; then
  echo -e "${GREEN}[PASS] Task 2: Boot diagnostic report verified with kernel cmdline and root UUID.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/boot_diagnostic.txt missing or incomplete.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w3d1-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w3d1-lfcs${NC}"
  exit 1
fi
