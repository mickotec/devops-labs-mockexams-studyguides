#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w5d2-cka: Cluster Upgrade: Kubeadm Control Plane...${NC}"
SCORE=0; TOTAL=2
# Task 1: upgrade_plan.txt
PLAN=$(ssh controlplane 'cat /opt/k8s/upgrade_plan.txt 2>/dev/null || true')
if echo "$PLAN" | grep -qiE "Components that can be upgraded|kubeadm|CURRENT"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/upgrade_plan.txt contains kubeadm upgrade plan.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/upgrade_plan.txt missing or empty.${NC}"
fi

# Task 2: Manifests exist
ALL_M=$(ssh controlplane 'ls /etc/kubernetes/manifests/{kube-apiserver.yaml,kube-controller-manager.yaml,kube-scheduler.yaml,etcd.yaml} 2>/dev/null | wc -l')
if [ "$ALL_M" -eq 4 ]; then
  echo -e "${GREEN}[PASS] Task 2: All 4 core control-plane static pod manifests verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: One or more static pod manifests missing in /etc/kubernetes/manifests.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w5d2-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w5d2-cka${NC}"
  exit 1
fi
