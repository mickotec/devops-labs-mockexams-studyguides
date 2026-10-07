#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating w4d4-cka: Autoscaling: HPA, VPA & In-Place Pod Resize...${NC}"
SCORE=0; TOTAL=2
# Task 1: Deployment order-backend
DEP_REQS=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.spec.template.spec.containers[0].resources.requests.cpu}" 2>/dev/null || echo "None"')
DEP_REP=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$DEP_REQS" == "50m" ] && [ "$DEP_REP" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: Deployment order-backend running with 50m CPU requests.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: order-backend cpu requests=$DEP_REQS, readyReplicas=$DEP_REP.${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
HPA_MIN=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.minReplicas}" 2>/dev/null || echo "0"')
HPA_TARGET=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.scaleTargetRef.name}" 2>/dev/null || echo "None"')
if [ "$HPA_MAX" == "6" ] && [ "$HPA_MIN" == "2" ] && [ "$HPA_TARGET" == "order-backend" ]; then
  echo -e "${GREEN}[PASS] Task 2: order-backend-hpa configured with min=2, max=6 targeting order-backend.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: HPA target=$HPA_TARGET, min=$HPA_MIN, max=$HPA_MAX.${NC}"
fi

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${BOLD}${SCORE}/${TOTAL}${NC}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Lab w4d4-cka completed successfully!${NC}"
  exit 0
else
  echo -e "${RED}Checks incomplete. Review scenario tasks or run: ./lab solve w4d4-cka${NC}"
  exit 1
fi
