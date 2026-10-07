#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d3-cka: Cluster Upgrade: Worker Nodes...${NC}"
SCORE=0; TOTAL=2
# Task 1: Drain verification
DRAIN_LOG=$(ssh controlplane 'cat /opt/k8s/node01_drain.txt 2>/dev/null || true')
if echo "$DRAIN_LOG" | grep -qiE "node01 already cordoned|cordoned|evicting|drained"; then
  echo -e "${GREEN}[PASS] Task 1: Drain operation verified in /opt/k8s/node01_drain.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node01_drain.txt missing or did not contain drain output.${NC}"
fi

# Task 2 & 3: kubelet active and node01 uncordoned & Ready
KUBELET_STAT=$(ssh node01 'systemctl is-active kubelet 2>/dev/null || echo "inactive"')
N1_STATUS=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
UNSCHED=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')

if [ "$KUBELET_STAT" == "active" ] && [ "$N1_STATUS" == "True" ] && [ "$UNSCHED" != "true" ]; then
  echo -e "${GREEN}[PASS] Task 2 & 3: Worker node01 kubelet is active and node is Ready and schedulable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2 & 3: kubelet=$KUBELET_STAT, Ready=$N1_STATUS, unschedulable=$UNSCHED.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d3-cka${NC}"
  exit 1
fi
