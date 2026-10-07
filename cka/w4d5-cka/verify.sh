#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d5-cka: Admission Controllers & Validating Webhooks...${NC}"
SCORE=0; TOTAL=2
# Task 1: enabled_admission_plugins.txt
PLUGINS=$(ssh controlplane 'cat /opt/k8s/enabled_admission_plugins.txt 2>/dev/null || true')
if [ -n "$PLUGINS" ] && echo "$PLUGINS" | grep -qiE "NodeRestriction|NamespaceLifecycle|LimitRanger"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/enabled_admission_plugins.txt contains active admission plugins.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/enabled_admission_plugins.txt missing or lacks recognized plugins.${NC}"
fi

# Task 2: admission_rejection.log
REJECT=$(ssh controlplane 'cat /opt/k8s/admission_rejection.log 2>/dev/null || true')
if echo "$REJECT" | grep -qiE "NotFound|not found|namespaces.*void-ns"; then
  echo -e "${GREEN}[PASS] Task 2: NamespaceLifecycle admission rejection logged.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/admission_rejection.log missing or did not capture rejection.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d5-cka${NC}"
  exit 1
fi
