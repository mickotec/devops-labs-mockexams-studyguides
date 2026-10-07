#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d3-cka: ServiceAccounts & SecurityContexts...${NC}"
SCORE=0; TOTAL=2
# Task 1: ServiceAccount
AUTO_MNT=$(ssh controlplane 'kubectl get sa restricted-sa -n w6d3-sec -o jsonpath="{.automountServiceAccountToken}" 2>/dev/null || echo "true"')
if [ "$AUTO_MNT" == "false" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount restricted-sa configured with automountServiceAccountToken=false.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ServiceAccount automountServiceAccountToken is $AUTO_MNT.${NC}"
fi

# Task 2: hardened-app securityContext
SEC_UID=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.securityContext.runAsUser}" 2>/dev/null || echo "0"')
RO_FS=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_UID" == "10001" ] && [ "$RO_FS" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: hardened-app running with runAsUser=10001 and readOnlyRootFilesystem=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Pod not running or securityContext mismatch (uid=$SEC_UID, ro_fs=$RO_FS, phase=$PHASE).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d3-cka${NC}"
  exit 1
fi
