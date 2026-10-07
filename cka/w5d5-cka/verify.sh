#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d5-cka: TLS Basics & PKI in Kubernetes...${NC}"
SCORE=0; TOTAL=2
# Task 1: certs_expiration.txt
EXPIRE=$(ssh controlplane 'cat /opt/k8s/certs_expiration.txt 2>/dev/null || true')
if echo "$EXPIRE" | grep -qiE "CERTIFICATE|EXPIRES|RESIDUAL TIME"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/certs_expiration.txt contains certificate expiration report.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/certs_expiration.txt missing or empty.${NC}"
fi

# Task 2: apiserver_sans.txt
SANS=$(ssh controlplane 'cat /opt/k8s/apiserver_sans.txt 2>/dev/null || true')
if echo "$SANS" | grep -qi "kubernetes"; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/apiserver_sans.txt contains API Server SANs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/apiserver_sans.txt missing or lacks SANs.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d5-cka${NC}"
  exit 1
fi
