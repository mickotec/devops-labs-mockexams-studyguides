#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d5-cka: Fast Imperative CLI Mastery with Kubectl...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Shell environment & vimrc...${NC}"
BASH_CHECK=$(ssh controlplane 'grep -E "alias k=kubectl" ~/.bashrc 2>/dev/null || true')
VIM_CHECK=$(ssh controlplane 'grep -E "tabstop=2" ~/.vimrc 2>/dev/null || true')
if [ -n "$BASH_CHECK" ] && [ -n "$VIM_CHECK" ]; then
  echo -e "${GREEN}[PASS] Shell alias and ~/.vimrc configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.bashrc or ~/.vimrc missing required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Imperative deployment, service, secret...${NC}"
DEPLOY=$(ssh controlplane 'kubectl get deploy cache-redis -n speed-drill -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc cache-service -n speed-drill -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
SEC=$(ssh controlplane 'kubectl get secret redis-secret -n speed-drill -o jsonpath="{.data.auth}" 2>/dev/null || echo "none"')

if [ "$DEPLOY" == "3" ] && [ "$SVC" == "6379" ] && [ "$SEC" != "none" ]; then
  echo -e "${GREEN}[PASS] cache-redis (3 replicas), cache-service (6379), and redis-secret verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Resources incomplete: deploy replicas=$DEPLOY, svc port=$SVC, secret=$SEC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Clean YAML export...${NC}"
EXPORT_FILE=$(ssh controlplane 'cat /opt/k8s/clean-cache.yaml 2>/dev/null || true')
if [ -n "$EXPORT_FILE" ] && ! echo "$EXPORT_FILE" | grep -q "managedFields"; then
  echo -e "${GREEN}[PASS] /opt/k8s/clean-cache.yaml is clean of managedFields.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-cache.yaml missing or contains managedFields.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d5-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d5-cka${NC}"
  exit 1
fi
