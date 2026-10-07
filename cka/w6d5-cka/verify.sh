#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d5-cka: Helm & Kustomize (2025 Updates)...${NC}"
SCORE=0; TOTAL=2
# Task 1: kustomization.yaml exists
KUST=$(ssh controlplane 'test -f /opt/k8s/kustomize/base/kustomization.yaml && echo "yes" || echo "no"')
if [ "$KUST" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/kustomize/base/kustomization.yaml created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: kustomization.yaml missing.${NC}"
fi

# Task 2: prod-web-server deployment in w6d5-kustomize
DEP=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
LBL=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.metadata.labels.env}" 2>/dev/null || echo "None"')

if [ "$DEP" -ge 2 ] && [ "$LBL" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 2: prod-web-server applied with prefix and env=production label.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment prod-web-server not running ($DEP/2) or label=$LBL.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d5-cka${NC}"
  exit 1
fi
