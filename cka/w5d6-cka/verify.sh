#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d6-cka: Full Disaster Recovery & Upgrade Drill...${NC}"
SCORE=0; TOTAL=3
# Task 1: etcd snapshot
SNAP_OK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/milestone5-etcd.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
if [ -n "$SNAP_OK" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/milestone5-etcd.db verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/backup/milestone5-etcd.db missing or invalid.${NC}"
fi

# Task 2: node02 drained
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Task 2: node02 is cordoned/drained for maintenance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: node02 is not cordoned (unschedulable=$UNSCHED).${NC}"
fi

# Task 3: certs audit
if ssh controlplane 'test -s /opt/k8s/m5_certs_audit.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/m5_certs_audit.txt generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/m5_certs_audit.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d6-cka${NC}"
  exit 1
fi
