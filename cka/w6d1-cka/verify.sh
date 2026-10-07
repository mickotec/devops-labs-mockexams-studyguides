#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w6d1-cka: Certificates API & KubeConfig Management...${NC}"
SCORE=0; TOTAL=3
# Task 1 & 2: CSR approved and certificate extracted
CSR_STAT=$(ssh controlplane 'kubectl get csr developer-bob-csr -o jsonpath="{.status.conditions[0].type}" 2>/dev/null || echo "None"')
CRT_EXISTS=$(ssh controlplane 'test -s /opt/k8s/developer-bob.crt && echo "yes" || echo "no"')

if [ "$CSR_STAT" == "Approved" ]; then
  echo -e "${GREEN}[PASS] Task 1: CertificateSigningRequest developer-bob-csr approved.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: developer-bob-csr status is $CSR_STAT (expected Approved).${NC}"
fi

if [ "$CRT_EXISTS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: Certificate exported to /opt/k8s/developer-bob.crt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/developer-bob.crt missing or empty.${NC}"
fi

# Task 3: bob.kubeconfig has developer-bob user
if ssh controlplane 'test -f /opt/k8s/bob.kubeconfig && grep -q "developer-bob" /opt/k8s/bob.kubeconfig'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/bob.kubeconfig configured with developer-bob.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/bob.kubeconfig missing or does not reference developer-bob.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w6d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w6d1-cka${NC}"
  exit 1
fi
