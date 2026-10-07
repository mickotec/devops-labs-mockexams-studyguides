#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w2d6-cka: Week 2 Speed Drills & Controller Triathlon...${NC}"
SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Deployment replicas in triathlon-w2...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$REPLICAS" == "5" ]; then
  echo -e "${GREEN}[PASS] Deployment order-processor has 5 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Ready replicas: $REPLICAS (expected 5).${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service on 30500...${NC}"
PORT=$(ssh controlplane 'kubectl get svc order-service -n triathlon-w2 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$PORT" == "30500" ]; then
  echo -e "${GREEN}[PASS] NodePort service on 30500 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $PORT (expected 30500).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Image rolled back to 1.24-alpine...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
if [ "$IMAGE" == "nginx:1.24-alpine" ]; then
  echo -e "${GREEN}[PASS] Image is rolled back to nginx:1.24-alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is $IMAGE (expected nginx:1.24-alpine).${NC}"
fi

echo -e "${BOLD}Checking Task 4: Clean YAML export...${NC}"
EXPORT=$(ssh controlplane 'cat /opt/k8s/clean-export.yaml 2>/dev/null || true')
if [ -n "$EXPORT" ] && ! echo "$EXPORT" | grep -q "resourceVersion:"; then
  echo -e "${GREEN}[PASS] Clean YAML export verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-export.yaml missing or contains resourceVersion.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w2d6-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w2d6-cka${NC}"
  exit 1
fi
