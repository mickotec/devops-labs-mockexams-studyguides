#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w8d3-cka: JSONPath Queries & Lightning Labs 1 & 2...${NC}"
SCORE=0; TOTAL=4
# Task 1: node_names.txt contains nodes
if ssh controlplane 'test -s /opt/k8s/node_names.txt && grep -q controlplane /opt/k8s/node_names.txt && grep -q node01 /opt/k8s/node_names.txt'; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/node_names.txt contains cluster nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node_names.txt missing or incomplete.${NC}"
fi

# Task 2: kube_system_images.txt
if ssh controlplane 'test -s /opt/k8s/kube_system_images.txt && grep -q -E "(coredns|apiserver|etcd)" /opt/k8s/kube_system_images.txt'; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/kube_system_images.txt contains system container images.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/kube_system_images.txt missing or lacks system images.${NC}"
fi

# Task 3: pod_node_mapping.txt custom columns
if ssh controlplane 'test -s /opt/k8s/pod_node_mapping.txt && grep -q "NAME" /opt/k8s/pod_node_mapping.txt && grep -q "pod-alpha" /opt/k8s/pod_node_mapping.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/pod_node_mapping.txt custom columns verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/pod_node_mapping.txt missing or invalid format.${NC}"
fi

# Task 4: Lightning challenge pod & service
LIGHT_PHASE=$(ssh controlplane 'kubectl get pod fast-pod -n w8d3-lightning -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
LIGHT_SVC=$(ssh controlplane 'kubectl get svc fast-svc -n w8d3-lightning -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
if [ "$LIGHT_PHASE" == "Running" ] && [ "$LIGHT_SVC" == "6379" ]; then
  echo -e "${GREEN}[PASS] Task 4: Lightning Pod fast-pod and Service fast-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: fast-pod phase=$LIGHT_PHASE, fast-svc port=$LIGHT_SVC.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w8d3-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w8d3-cka${NC}"
  exit 1
fi
