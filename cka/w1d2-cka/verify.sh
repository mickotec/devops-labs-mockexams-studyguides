#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d2-cka: ETCD Fundamentals & Cluster State Store...${NC}"
SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ETCD health export...${NC}"
HEALTH_CHECK=$(ssh controlplane 'sudo cat /opt/backup/etcd-health.txt 2>/dev/null || true')
if echo "$HEALTH_CHECK" | grep -qi "healthy"; then
  echo -e "${GREEN}[PASS] /opt/backup/etcd-health.txt contains verified health output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/backup/etcd-health.txt missing or does not indicate healthy status.${NC}"
fi

echo -e "${BOLD}Checking Task 2: ETCD snapshot file & status table...${NC}"
SNAP_CHECK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table 2>/dev/null || true')
if echo "$SNAP_CHECK" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] Snapshot /opt/backup/etcd-snapshot-w1d2.db is valid and readable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot invalid or status verification failed.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Namespace count file...${NC}"
COUNT=$(ssh controlplane 'sudo cat /opt/backup/namespace-count.txt 2>/dev/null | tr -d "[:space:]" || true')
ACTUAL_NS_COUNT=$(ssh controlplane 'kubectl get ns --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')

if [ -n "$COUNT" ] && [ "$COUNT" == "$ACTUAL_NS_COUNT" ]; then
  echo -e "${GREEN}[PASS] Namespace count matched ($COUNT namespaces).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace count was '$COUNT' (expected $ACTUAL_NS_COUNT).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d2-cka${NC}"
  exit 1
fi
