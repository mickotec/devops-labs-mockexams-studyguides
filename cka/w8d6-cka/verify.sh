#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d6-cka: Killer.sh Simulator Marathon (Exam Benchmark)...${NC}"
SCORE=0; TOTAL=4
# Task 1: audit-counter sidecar pod
AC_STATUS=$(ssh controlplane 'kubectl get pod audit-counter -n w8d6-benchmark -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$AC_STATUS" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 1: Pod audit-counter running with 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: audit-counter status: '$AC_STATUS' (expected 'true true').${NC}"
fi

# Task 2: etcd snapshot backup
if ssh controlplane 'test -s /opt/k8s/etcd-backup.db && ETCDCTL_API=3 etcdctl snapshot status /opt/k8s/etcd-backup.db >/dev/null 2>&1'; then
  echo -e "${GREEN}[PASS] Task 2: Valid etcd snapshot verified at /opt/k8s/etcd-backup.db.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/etcd-backup.db missing or invalid etcd database.${NC}"
fi

# Task 3: Ingress with TLS
TLS_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.tls[0].secretName}" 2>/dev/null || echo "None"')
HOST_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$TLS_NAME" == "benchmark-tls" ] && [ "$HOST_NAME" == "benchmark.k8s.local" ]; then
  echo -e "${GREEN}[PASS] Task 3: Ingress benchmark-ingress with TLS verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Ingress TLS or host mismatch (tls=$TLS_NAME, host=$HOST_NAME).${NC}"
fi

# Task 4: NetworkPolicy strict-db-policy
NP_TARGET=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_ALLOW=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_PORT=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
if [ "$NP_TARGET" == "db" ] && [ "$NP_ALLOW" == "backend" ] && [ "$NP_PORT" == "5432" ]; then
  echo -e "${GREEN}[PASS] Task 4: NetworkPolicy strict-db-policy correctly isolates db on port 5432.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: NetworkPolicy rules mismatch (target=$NP_TARGET, allow=$NP_ALLOW, port=$NP_PORT).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d6-cka${NC}"
  exit 1
fi
