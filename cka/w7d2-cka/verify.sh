#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d2-cka: Service Networking & CoreDNS Deep Dive...${NC}"
SCORE=0; TOTAL=3
# Task 1: backend-svc ClusterIP
SVC_PORT=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
SVC_TARGET=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.ports[0].targetPort}" 2>/dev/null || echo "0"')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints backend-svc -n w7d2-dns -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
if [ "$SVC_PORT" == "8080" ] && [ "$SVC_TARGET" == "80" ] && [ "$EP_COUNT" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: backend-svc ClusterIP verified with 2 ready endpoints.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: backend-svc port=$SVC_PORT (exp 8080), target=$SVC_TARGET (exp 80), endpoints=$EP_COUNT (exp >=2).${NC}"
fi

# Task 2: frontend-nodeport NodePort 30080
NP_TYPE=$(ssh controlplane 'kubectl get svc frontend-nodeport -n w7d2-dns -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
NODE_PORT=$(ssh controlplane 'kubectl get svc frontend-nodeport -n w7d2-dns -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$NP_TYPE" == "NodePort" ] && [ "$NODE_PORT" == "30080" ]; then
  echo -e "${GREEN}[PASS] Task 2: frontend-nodeport verified on NodePort 30080.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: frontend-nodeport type=$NP_TYPE (exp NodePort), nodePort=$NODE_PORT (exp 30080).${NC}"
fi

# Task 3: DNS resolution file exists and contains resolved IP
BACKEND_IP=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "MISSING"')
if ssh controlplane "test -s /opt/k8s/dns_resolution.txt && grep -q '$BACKEND_IP' /opt/k8s/dns_resolution.txt"; then
  echo -e "${GREEN}[PASS] Task 3: CoreDNS resolution verified for backend-svc ($BACKEND_IP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/dns_resolution.txt missing or does not contain clusterIP $BACKEND_IP.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d2-cka${NC}"
  exit 1
fi
