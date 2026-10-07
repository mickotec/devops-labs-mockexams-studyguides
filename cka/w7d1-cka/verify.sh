#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w7d1-cka: Cluster & Pod Networking Prerequisites...${NC}"
SCORE=0; TOTAL=3
# Task 1: CNI plugin type file exists and has content
CNI_TYPE=$(ssh controlplane 'cat /opt/k8s/cni-plugin-type.txt 2>/dev/null | tr -d "[:space:]"')
if [ -n "$CNI_TYPE" ] && [[ "$CNI_TYPE" =~ (flannel|calico|bridge|weave|cilium|canal) ]]; then
  echo -e "${GREEN}[PASS] Task 1: Valid CNI plugin type recorded ($CNI_TYPE).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/cni-plugin-type.txt missing or invalid: $CNI_TYPE.${NC}"
fi

# Task 2: Node podCIDRs recorded
CIDR1=$(ssh controlplane 'grep -E "^node01=" /opt/k8s/node-podcidrs.txt 2>/dev/null || true')
CIDR2=$(ssh controlplane 'grep -E "^node02=" /opt/k8s/node-podcidrs.txt 2>/dev/null || true')
ACTUAL1=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.podCIDR}" 2>/dev/null || true')
ACTUAL2=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.podCIDR}" 2>/dev/null || true')

if [ "$CIDR1" == "node01=$ACTUAL1" ] && [ "$CIDR2" == "node02=$ACTUAL2" ]; then
  echo -e "${GREEN}[PASS] Task 2: Node podCIDRs correctly recorded ($ACTUAL1, $ACTUAL2).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Node podCIDRs mismatch. Expected node01=$ACTUAL1 and node02=$ACTUAL2.${NC}"
fi

# Task 3: DaemonSet net-mesh running on worker nodes
READY_DS=$(ssh controlplane 'kubectl get ds net-mesh -n w7d1-net -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
DESIRED_DS=$(ssh controlplane 'kubectl get ds net-mesh -n w7d1-net -o jsonpath="{.status.desiredNumberScheduled}" 2>/dev/null || echo "0"')
if [ "$READY_DS" -ge 2 ] && [ "$READY_DS" -eq "$DESIRED_DS" ]; then
  echo -e "${GREEN}[PASS] Task 3: DaemonSet net-mesh has $READY_DS/$DESIRED_DS ready pods.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: DaemonSet net-mesh ready pods: $READY_DS (expected >= 2).${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w7d1-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w7d1-cka${NC}"
  exit 1
fi
