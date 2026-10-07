#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d3-lfcs: Package Managers (APT, DNF/YUM & RPM)...${NC}"
SCORE=0; TOTAL=3
# Task 1: tar_package.txt
if [ -f /var/tmp/tar_package.txt ] && grep -qi "tar" /var/tmp/tar_package.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/tar_package.txt created with package ownership details.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/tar_package.txt missing or lacks tar info.${NC}"
fi

# Task 2: apt-mark showhold has tar
HOLD=$(apt-mark showhold 2>/dev/null || true)
if echo "$HOLD" | grep -q "tar"; then
  echo -e "${GREEN}[PASS] Task 2: Package 'tar' is pinned (hold) in apt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Package 'tar' is not held.${NC}"
fi

# Task 3: .deb file in /var/tmp/pkg_cache/
DEB_COUNT=$(ls /var/tmp/pkg_cache/*.deb 2>/dev/null | wc -l)
if [ "$DEB_COUNT" -ge 1 ]; then
  echo -e "${GREEN}[PASS] Task 3: Debian package downloaded to /var/tmp/pkg_cache/.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: No .deb package found in /var/tmp/pkg_cache/.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d3-lfcs completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d3-lfcs${NC}"
  exit 1
fi
