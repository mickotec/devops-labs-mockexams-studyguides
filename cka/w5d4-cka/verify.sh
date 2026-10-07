#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d4-cka: ETCD Snapshot Backup & Disaster Recovery...${NC}"
SCORE=0; TOTAL=2
# Task 1 & 2: etcd snapshot exists and is valid
IS_VALID=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
STATUS_FILE=$(ssh controlplane 'cat /opt/backup/etcd_snapshot_status.txt 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')

if [ -n "$IS_VALID" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/etcd-snapshot-w5.db is a valid etcd snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Snapshot file missing or invalid.${NC}"
fi

if [ -n "$STATUS_FILE" ]; then
  echo -e "${GREEN}[PASS] Task 2: Snapshot status table saved to /opt/backup/etcd_snapshot_status.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/backup/etcd_snapshot_status.txt missing or empty.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d4-cka${NC}"
  exit 1
fi
