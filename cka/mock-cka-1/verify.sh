#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-cka-1: CKA Full-Scale Timed Mock Exam 1...${NC}"
# Linux Foundation CKA Domain Tracking
SCORE_STOR=0; TOTAL_STOR=2       # 10%
SCORE_TROUBLE=0; TOTAL_TROUBLE=5   # 30%
SCORE_WORKLOAD=0; TOTAL_WORKLOAD=3 # 15%
SCORE_CLUSTER=0; TOTAL_CLUSTER=4   # 25%
SCORE_SVC=0; TOTAL_SVC=3           # 20%
TOTAL_PASSED=0; TOTAL_QUESTIONS=17
SCORE=0; TOTAL=17

echo -e "${BOLD}Evaluating CKA Mock Exam 1 against Linux Foundation Domain Weights...${NC}"

# Q1: ETCD Snapshot (Cluster Architecture - 25%)
if ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-backup.db --write-out=table 2>/dev/null | grep -qiE "REVISION|TOTAL KEYS"'; then
  echo -e "${GREEN}[PASS] Q1: ETCD snapshot verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: /opt/backup/etcd-backup.db missing or invalid.${NC}"
fi

# Q2: RBAC Role & Binding (Cluster Architecture - 25%)
if ssh controlplane 'kubectl get rolebinding read-pods -n mock-cka-1-q2 -o jsonpath="{.roleRef.name}" 2>/dev/null | grep -qw "pod-reader"'; then
  echo -e "${GREEN}[PASS] Q2: RBAC pod-reader Role and read-pods RoleBinding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: RoleBinding read-pods or Role pod-reader missing.${NC}"
fi

# Q3: ClusterRole & Binding (Cluster Architecture - 25%)
if ssh controlplane 'kubectl get clusterrolebinding node-watchers-binding -o jsonpath="{.roleRef.name}" 2>/dev/null | grep -qw "node-watcher"'; then
  echo -e "${GREEN}[PASS] Q3: ClusterRole node-watcher and Binding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: ClusterRoleBinding node-watchers-binding missing.${NC}"
fi

# Q4: Kubeconfig (Cluster Architecture - 25%)
if ssh controlplane 'test -f /opt/k8s/custom-kubeconfig' && ssh controlplane 'grep -q "dev-context" /opt/k8s/custom-kubeconfig'; then
  echo -e "${GREEN}[PASS] Q4: /opt/k8s/custom-kubeconfig verified with dev-context.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: custom-kubeconfig missing or invalid.${NC}"
fi

# Q5: Deployment rollback (Workloads & Scheduling - 15%)
IMG5=$(ssh controlplane 'kubectl get deploy nginx-deploy -n mock-cka-1-q5 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
if [ "$IMG5" == "nginx:1.24-alpine" ]; then
  echo -e "${GREEN}[PASS] Q5: nginx-deploy rolled back to nginx:1.24-alpine.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: nginx-deploy image is $IMG5 (expected nginx:1.24-alpine).${NC}"
fi

# Q6: Sidecar Pod (Workloads & Scheduling - 15%)
VOL6=$(ssh controlplane 'kubectl get pod multi-container-pod -n mock-cka-1-q6 -o jsonpath="{.spec.volumes[0].name}" 2>/dev/null || echo "None"')
C6=$(ssh controlplane 'kubectl get pod multi-container-pod -n mock-cka-1-q6 -o jsonpath="{.spec.containers[*].name}" 2>/dev/null || echo "None"')
if echo "$C6" | grep -qw "app" && echo "$C6" | grep -qw "sidecar" && [ "$VOL6" == "shared-data" ]; then
  echo -e "${GREEN}[PASS] Q6: Multi-container pod with shared volume verified.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: multi-container-pod containers: $C6, volume: $VOL6.${NC}"
fi

# Q7: ConfigMap and Secret env injection (Workloads & Scheduling - 15%)
ENV7=$(ssh controlplane 'kubectl get pod config-pod -n mock-cka-1-q7 -o jsonpath="{.spec.containers[0].env[*].name}" 2>/dev/null || echo "None"')
if echo "$ENV7" | grep -qw "CONFIG_VAL" && echo "$ENV7" | grep -qw "SECRET_VAL"; then
  echo -e "${GREEN}[PASS] Q7: Pod config-pod env injection verified.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: config-pod env vars: $ENV7.${NC}"
fi

# Q8: Services ClusterIP and NodePort (Services & Networking - 20%)
SVC8_C=$(ssh controlplane 'kubectl get svc web-svc -n mock-cka-1-q8 -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
SVC8_N=$(ssh controlplane 'kubectl get svc web-nodeport -n mock-cka-1-q8 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$SVC8_C" == "ClusterIP" ] && [ "$SVC8_N" == "31555" ]; then
  echo -e "${GREEN}[PASS] Q8: Services web-svc (ClusterIP) and web-nodeport (31555) verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: ClusterIP=$SVC8_C, NodePort=$SVC8_N.${NC}"
fi

# Q9: NetworkPolicy (Services & Networking - 20%)
NP9=$(ssh controlplane 'kubectl get netpol allow-client -n mock-cka-1-q9 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
if [ "$NP9" == "allow-client" ]; then
  echo -e "${GREEN}[PASS] Q9: NetworkPolicy allow-client verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: NetworkPolicy allow-client missing.${NC}"
fi

# Q10: CoreDNS query test (Services & Networking - 20%)
DNS10=$(ssh controlplane 'cat /opt/k8s/dns-test.txt 2>/dev/null || true')
if echo "$DNS10" | grep -qi "kubernetes.default"; then
  echo -e "${GREEN}[PASS] Q10: CoreDNS resolution verified in /opt/k8s/dns-test.txt.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: /opt/k8s/dns-test.txt missing or lacks resolution.${NC}"
fi

# Q11: PersistentVolume & PVC (Storage - 10%)
PV11=$(ssh controlplane 'kubectl get pv mock-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
PVC11=$(ssh controlplane 'kubectl get pvc mock-pvc -n mock-cka-1-q11 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV11" == "Bound" ] && [ "$PVC11" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Q11: PersistentVolume mock-pv and PVC mock-pvc Bound.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: PV=$PV11, PVC=$PVC11.${NC}"
fi

# Q12: Storage Pod mounting PVC (Storage - 10%)
POD12=$(ssh controlplane 'kubectl get pod storage-pod -n mock-cka-1-q12 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
FILE12=$(ssh controlplane 'cat /mnt/mock-data/status.txt 2>/dev/null || true')
if [ "$POD12" == "Running" ] && [ "$FILE12" == "storage-ok" ]; then
  echo -e "${GREEN}[PASS] Q12: Pod storage-pod Running and wrote storage-ok.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: storage-pod phase: $POD12, file content: '$FILE12'.${NC}"
fi

# Q13: Kube-scheduler troubleshooting (Troubleshooting - 30%)
SCHED13=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "None"')
SCHED13_CONF=$(ssh controlplane 'grep "--kubeconfig" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true')
if [ "$SCHED13" == "Running" ] && echo "$SCHED13_CONF" | grep -q "scheduler.conf" && ! echo "$SCHED13_CONF" | grep -q "broken"; then
  echo -e "${GREEN}[PASS] Q13: kube-scheduler repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: kube-scheduler status: $SCHED13, config: $SCHED13_CONF (expected scheduler.conf).${NC}"
fi

# Q14: CrashLoopBackOff fix (Troubleshooting - 30%)
POD14=$(ssh controlplane 'kubectl get pod broken-worker -n mock-cka-1-q14 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
CMD14=$(ssh controlplane 'kubectl get pod broken-worker -n mock-cka-1-q14 -o jsonpath="{.spec.containers[0].command}" 2>/dev/null || true')
if [ "$POD14" == "Running" ] && ! echo "$CMD14" | grep -q "invalid"; then
  echo -e "${GREEN}[PASS] Q14: broken-worker repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: broken-worker status: $POD14.${NC}"
fi

# Q15: Uncordon node01 (Troubleshooting - 30%)
SCHED15=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$SCHED15" != "true" ]; then
  echo -e "${GREEN}[PASS] Q15: node01 is uncordoned and schedulable.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: node01 is still cordoned.${NC}"
fi

# Q16: Broken service selector fix (Troubleshooting - 30%)
EP16=$(ssh controlplane 'kubectl get endpoints api-service -n mock-cka-1-q16 -o jsonpath="{.subsets[0].addresses[0].ip}" 2>/dev/null || echo "None"')
SEL16=$(ssh controlplane 'kubectl get svc api-service -n mock-cka-1-q16 -o jsonpath="{.spec.selector.app}" 2>/dev/null || echo "None"')
if [ "$EP16" != "None" ] && [ "$SEL16" == "api-v1" ]; then
  echo -e "${GREEN}[PASS] Q16: Service api-service selector repaired with active endpoints.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: api-service selector: $SEL16 (expected api-v1).${NC}"
fi

# Q17: Deployment missing env var fix (Troubleshooting - 30%)
READY17=$(ssh controlplane 'kubectl get deploy db-client -n mock-cka-1-q17 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$READY17" == "1" ]; then
  echo -e "${GREEN}[PASS] Q17: Deployment db-client healthy with 1/1 ready replicas.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: db-client ready replicas: $READY17.${NC}"
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
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-cka-1 completed successfully! (${TOTAL_PCT}% >= 66.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (66.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-cka-1${NC}"
  exit 1
fi
