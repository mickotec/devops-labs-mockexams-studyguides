#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-cka-2: CKA Full-Scale Timed Mock Exam 2...${NC}"
# Linux Foundation CKA Domain Tracking
SCORE_STOR=0; TOTAL_STOR=2       # 10%
SCORE_TROUBLE=0; TOTAL_TROUBLE=5   # 30%
SCORE_WORKLOAD=0; TOTAL_WORKLOAD=3 # 15%
SCORE_CLUSTER=0; TOTAL_CLUSTER=4   # 25%
SCORE_SVC=0; TOTAL_SVC=3           # 20%
TOTAL_PASSED=0; TOTAL_QUESTIONS=17
SCORE=0; TOTAL=17

echo -e "${BOLD}Evaluating CKA Mock Exam 2 against Linux Foundation Domain Weights...${NC}"

# Q1: SA & ClusterRole (Cluster Architecture - 25%)
SA1=$(ssh controlplane 'kubectl get sa monitoring-sa -n mock-cka-2-q1 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
CRB1=$(ssh controlplane 'kubectl get clusterrolebinding monitoring-binding -o jsonpath="{.roleRef.name}" 2>/dev/null || echo "None"')
if [ "$SA1" == "monitoring-sa" ] && [ "$CRB1" == "monitoring-role" ]; then
  echo -e "${GREEN}[PASS] Q1: monitoring-sa and ClusterRoleBinding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: SA=$SA1, CRB=$CRB1.${NC}"
fi

# Q2: Cert Expiry (Cluster Architecture - 25%)
if ssh controlplane 'test -f /opt/k8s/apiserver-expiry.txt' && ssh controlplane 'grep -qi "CERTIFICATE" /opt/k8s/apiserver-expiry.txt'; then
  echo -e "${GREEN}[PASS] Q2: apiserver-expiry.txt verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: apiserver-expiry.txt missing or lacks cert table.${NC}"
fi

# Q3: Worker static pod on node01 (Cluster Architecture - 25%)
POD3=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "static-web-node01" || true')
if [ -n "$POD3" ] && echo "$POD3" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Q3: Static pod static-web-node01 Running.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: static-web-node01 not running.${NC}"
fi

# Q4: Node02 maintenance / Ready (Cluster Architecture - 25%)
READY4=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
SCHED4=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$READY4" == "True" ] && [ "$SCHED4" != "true" ]; then
  echo -e "${GREEN}[PASS] Q4: node02 is Ready and schedulable.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: node02 Ready=$READY4, unschedulable=$SCHED4.${NC}"
fi

# Q5: Init container emptyDir pod (Workloads & Scheduling - 15%)
POD5=$(ssh controlplane 'kubectl get pod init-volume-pod -n mock-cka-2-q5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
INIT5=$(ssh controlplane 'kubectl get pod init-volume-pod -n mock-cka-2-q5 -o jsonpath="{.spec.initContainers[0].name}" 2>/dev/null || echo "None"')
if [ "$POD5" == "Running" ] && [ "$INIT5" != "None" ]; then
  echo -e "${GREEN}[PASS] Q5: init-volume-pod running with initContainer.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: init-volume-pod phase: $POD5, initContainer: $INIT5.${NC}"
fi

# Q6: HPA (Workloads & Scheduling - 15%)
HPA6=$(ssh controlplane 'kubectl get hpa hpa-deployment -n mock-cka-2-q6 -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
if [ "$HPA6" == "8" ]; then
  echo -e "${GREEN}[PASS] Q6: HPA hpa-deployment verified (maxReplicas=8).${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: HPA maxReplicas: $HPA6 (expected 8).${NC}"
fi

# Q7: CronJob (Workloads & Scheduling - 15%)
CJ7=$(ssh controlplane 'kubectl get cronjob periodic-task -n mock-cka-2-q7 -o jsonpath="{.spec.schedule}" 2>/dev/null || echo "None"')
if [ "$CJ7" == "*/5 * * * *" ]; then
  echo -e "${GREEN}[PASS] Q7: CronJob periodic-task verified with schedule */5 * * * *.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: CronJob schedule: $CJ7.${NC}"
fi

# Q8: Headless service & deployment (Services & Networking - 20%)
SVC8=$(ssh controlplane 'kubectl get svc db-headless -n mock-cka-2-q8 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
DEP8=$(ssh controlplane 'kubectl get deploy db-deployment -n mock-cka-2-q8 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$SVC8" == "None" ] && [ "$DEP8" == "3" ]; then
  echo -e "${GREEN}[PASS] Q8: Headless service (clusterIP: None) and deployment verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: clusterIP=$SVC8, replicas=$DEP8.${NC}"
fi

# Q9: NetworkPolicy allow-frontend (Services & Networking - 20%)
NP9=$(ssh controlplane 'kubectl get netpol allow-frontend -n mock-cka-2-q9 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
if [ "$NP9" == "allow-frontend" ]; then
  echo -e "${GREEN}[PASS] Q9: NetworkPolicy allow-frontend verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: allow-frontend NetworkPolicy missing.${NC}"
fi

# Q10: ExternalName service (Services & Networking - 20%)
SVC10=$(ssh controlplane 'kubectl get svc db-external -n mock-cka-2-q10 -o jsonpath="{.spec.externalName}" 2>/dev/null || echo "None"')
if [ "$SVC10" == "database.example.com" ]; then
  echo -e "${GREEN}[PASS] Q10: ExternalName service verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: externalName is '$SVC10'.${NC}"
fi

# Q11: PV & PVC manual-pv (Storage - 10%)
PV11=$(ssh controlplane 'kubectl get pv manual-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
POD11=$(ssh controlplane 'kubectl get pod pv-pod -n mock-cka-2-q11 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV11" == "Bound" ] && [ "$POD11" == "Running" ]; then
  echo -e "${GREEN}[PASS] Q11: PV manual-pv Bound and pv-pod Running.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: PV phase: $PV11, Pod phase: $POD11.${NC}"
fi

# Q12: Projected volume pod (Storage - 10%)
POD12=$(ssh controlplane 'kubectl get pod projected-volume-pod -n mock-cka-2-q12 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
PROJ12=$(ssh controlplane 'kubectl get pod projected-volume-pod -n mock-cka-2-q12 -o jsonpath="{.spec.volumes[0].projected.sources}" 2>/dev/null || echo "None"')
if [ "$POD12" == "Running" ] && [ "$PROJ12" != "None" ]; then
  echo -e "${GREEN}[PASS] Q12: projected-volume-pod Running with projected sources.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: projected-volume-pod status: $POD12.${NC}"
fi

# Q13: Kubelet on node02 (Troubleshooting - 30%)
KUB13=$(ssh node02 'systemctl is-active kubelet 2>/dev/null || echo "inactive"')
if [ "$KUB13" == "active" ]; then
  echo -e "${GREEN}[PASS] Q13: Kubelet on node02 is active.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: Kubelet on node02 is $KUB13.${NC}"
fi

# Q14: Pending pod scheduled (Troubleshooting - 30%)
POD14=$(ssh controlplane 'kubectl get pod pending-pod -n mock-cka-2-q14 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD14" == "Running" ]; then
  echo -e "${GREEN}[PASS] Q14: pending-pod is now Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: pending-pod is $POD14.${NC}"
fi

# Q15: Broken logger troubleshooting (Troubleshooting - 30%)
POD15=$(ssh controlplane 'kubectl get pod broken-logger -n mock-cka-2-q15 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
CMD15=$(ssh controlplane 'kubectl get pod broken-logger -n mock-cka-2-q15 -o jsonpath="{.spec.containers[0].command}" 2>/dev/null || true')
if [ "$POD15" == "Running" ] && ! echo "$CMD15" | grep -q "invalid"; then
  echo -e "${GREEN}[PASS] Q15: broken-logger repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: broken-logger status: $POD15.${NC}"
fi

# Q16: Ingress app-ingress (Troubleshooting - 30%)
ING16=$(ssh controlplane 'kubectl get ingress app-ingress -n mock-cka-2-q16 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$ING16" == "app.example.com" ]; then
  echo -e "${GREEN}[PASS] Q16: Ingress app-ingress verified for app.example.com.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: Ingress host: $ING16.${NC}"
fi

# Q17: Broken deployment image fix (Troubleshooting - 30%)
READY17=$(ssh controlplane 'kubectl get deploy broken-deployment -n mock-cka-2-q17 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$READY17" == "1" ]; then
  echo -e "${GREEN}[PASS] Q17: broken-deployment image fixed and ready.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: ready replicas: $READY17.${NC}"
fi


PCT_STOR=$(awk "BEGIN {printf \"%.1f\", $SCORE_STOR * 10.0 / $TOTAL_STOR}")
PCT_TROUBLE=$(awk "BEGIN {printf \"%.1f\", $SCORE_TROUBLE * 30.0 / $TOTAL_TROUBLE}")
PCT_WORKLOAD=$(awk "BEGIN {printf \"%.1f\", $SCORE_WORKLOAD * 15.0 / $TOTAL_WORKLOAD}")
PCT_CLUSTER=$(awk "BEGIN {printf \"%.1f\", $SCORE_CLUSTER * 25.0 / $TOTAL_CLUSTER}")
PCT_SVC=$(awk "BEGIN {printf \"%.1f\", $SCORE_SVC * 20.0 / $TOTAL_SVC}")

TOTAL_PCT=$(awk "BEGIN {printf \"%.1f\", ($SCORE_STOR * 10.0 / $TOTAL_STOR) + ($SCORE_TROUBLE * 30.0 / $TOTAL_TROUBLE) + ($SCORE_WORKLOAD * 15.0 / $TOTAL_WORKLOAD) + ($SCORE_CLUSTER * 25.0 / $TOTAL_CLUSTER) + ($SCORE_SVC * 20.0 / $TOTAL_SVC)}")

echo ""
echo "────────────────────────────────────────────────────────────"
echo -e "${BOLD}Linux Foundation Domain Weight Breakdown (CKA):${NC}"
echo -e "  • Storage (10%):                                     ${SCORE_STOR}/${TOTAL_STOR} passed   (${PCT_STOR}% / 10.0%)"
echo -e "  • Troubleshooting (30%):                             ${SCORE_TROUBLE}/${TOTAL_TROUBLE} passed   (${PCT_TROUBLE}% / 30.0%)"
echo -e "  • Workloads & Scheduling (15%):                      ${SCORE_WORKLOAD}/${TOTAL_WORKLOAD} passed   (${PCT_WORKLOAD}% / 15.0%)"
echo -e "  • Cluster Architecture, Install & Config (25%):      ${SCORE_CLUSTER}/${TOTAL_CLUSTER} passed   (${PCT_CLUSTER}% / 25.0%)"
echo -e "  • Services & Networking (20%):                       ${SCORE_SVC}/${TOTAL_SVC} passed   (${PCT_SVC}% / 20.0%)"
echo "────────────────────────────────────────────────────────────"
echo -e "Questions Passed:     ${BOLD}${TOTAL_PASSED} / ${TOTAL_QUESTIONS}${NC}"
echo -e "Final Weighted Score: ${BOLD}${TOTAL_PCT}%${NC}"
echo -e "Passing Threshold:    66.0%"
echo "────────────────────────────────────────────────────────────"

IS_PASS=$(awk "BEGIN {if ($TOTAL_PCT >= 66.0) print 1; else print 0}")
if [ "$IS_PASS" -eq 1 ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-cka-2 completed successfully! (${TOTAL_PCT}% >= 66.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (66.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-cka-2${NC}"
  exit 1
fi
