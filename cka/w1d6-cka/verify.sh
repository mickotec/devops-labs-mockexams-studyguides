#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w1d6-cka: Week 1 Integration & Milestone Triathlon...${NC}"
SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Control plane static pods...${NC}"
API_POD=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$API_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Control-plane kube-apiserver is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-apiserver status: $API_POD (manifests may still be misplaced).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Workload in triathlon-w1...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy web-ui -n triathlon-w1 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc web-ui-svc -n triathlon-w1 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$REPLICAS" == "2" ] && [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Deployment web-ui (2/2 ready) and service web-ui-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Workload incomplete: replicas=$REPLICAS, svc=$SVC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: ETCD snapshot...${NC}"
SNAP=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/triathlon-etcd.db --write-out=table 2>/dev/null || true')
if echo "$SNAP" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] /opt/backup/triathlon-etcd.db is a valid snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Worker static pod on node01...${NC}"
AGENT=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "w1-worker-agent-node01" || true')
if [ -n "$AGENT" ] && echo "$AGENT" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod w1-worker-agent-node01 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod w1-worker-agent-node01 not running.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w1d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w1d6-cka${NC}"
  exit 1
fi
