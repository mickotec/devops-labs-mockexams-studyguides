#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d3-cka: Secrets Management & Encryption at Rest...${NC}"
SCORE=0; TOTAL=2
# Task 1: Secret db-credentials
SEC_PASS=$(ssh controlplane 'kubectl get secret db-credentials -n w4d3-secrets -o jsonpath="{.data.password}" 2>/dev/null | base64 -d || echo "None"')
if [ "$SEC_PASS" == "S3cur3P@ssw0rd!" ]; then
  echo -e "${GREEN}[PASS] Task 1: Secret db-credentials verified with expected password.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Secret missing or password mismatch: $SEC_PASS.${NC}"
fi

# Task 2: vault-agent pod and mounted volume
PASS_FILE=$(ssh controlplane 'kubectl exec vault-agent -n w4d3-secrets -- cat /etc/vault/secrets/password 2>/dev/null || true')
PERM_MODE=$(ssh controlplane 'kubectl get pod vault-agent -n w4d3-secrets -o jsonpath="{.spec.volumes[0].secret.defaultMode}" 2>/dev/null || echo "0"')
if [ "$PASS_FILE" == "S3cur3P@ssw0rd!" ] && [ "$PERM_MODE" == "256" ]; then
  echo -e "${GREEN}[PASS] Task 2: Secret mounted at /etc/vault/secrets with defaultMode 256 (0400).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Mounted pass='$PASS_FILE' or defaultMode=$PERM_MODE (expected 256).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d3-cka${NC}"
  exit 1
fi
