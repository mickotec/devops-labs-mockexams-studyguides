#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d2-cka: ConfigMaps & Application Configuration...${NC}"
SCORE=0; TOTAL=2
# Task 1: ConfigMaps
CM1=$(ssh controlplane 'kubectl get cm backend-config -n w4d2-config -o jsonpath="{.data.DB_HOST}" 2>/dev/null || echo "None"')
CM2=$(ssh controlplane 'kubectl get cm ui-settings -n w4d2-config -o jsonpath="{.data.settings\.json}" 2>/dev/null || echo "None"')
if [ "$CM1" == "postgres.internal" ] && [ "$CM2" != "None" ]; then
  echo -e "${GREEN}[PASS] Task 1: ConfigMaps backend-config and ui-settings created accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ConfigMaps missing or invalid (DB_HOST=$CM1).${NC}"
fi

# Task 2: portal-app envFrom and Volume Mount
P_ENV=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- printenv DB_PORT 2>/dev/null || echo "None"')
P_FILE=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- cat /etc/portal/config/settings.json 2>/dev/null || true')
if [ "$P_ENV" == "5432" ] && echo "$P_FILE" | grep -q "dark"; then
  echo -e "${GREEN}[PASS] Task 2: portal-app has DB_PORT env var and /etc/portal/config/settings.json mounted.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env DB_PORT=$P_ENV or mounted file missing.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d2-cka${NC}"
  exit 1
fi
