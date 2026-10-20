#!/usr/bin/env bash
set -uo pipefail
SCORE=0; TOTAL=16

echo "=========================================================================="
echo "          CKAD killer.sh Mock Exam 1 Scorecard & Evaluation               "
echo "=========================================================================="

# Q1: Secret Env (6.25%)
Q1=$(ssh controlplane 'kubectl get pod secret-pod -n mock-ckad-1-q1 -o jsonpath="{.spec.containers[0].env[0].valueFrom.secretKeyRef.name}" 2>/dev/null || echo ""')
[ "$Q1" == "db-secret" ] && { echo -e "[0;32m[PASS] Q1: secret-pod configured with db-secret.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q1: secretKeyRef mismatch.[0m"

# Q2: ConfigMap Volume (6.25%)
Q2=$(ssh controlplane 'kubectl get pod cfg-volume-pod -n mock-ckad-1-q2 -o jsonpath="{.spec.volumes[0].configMap.name}" 2>/dev/null || echo ""')
[ "$Q2" == "app-cfg" ] && { echo -e "[0;32m[PASS] Q2: ConfigMap volume app-cfg mounted.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q2: ConfigMap volume mismatch.[0m"

# Q3: SecurityContext (6.25%)
Q3=$(ssh controlplane 'kubectl get pod hardened-pod -n mock-ckad-1-q3 -o jsonpath="{.spec.containers[0].securityContext.runAsUser}" 2>/dev/null || echo 0')
[ "$Q3" == "10001" ] && { echo -e "[0;32m[PASS] Q3: hardened-pod runAsUser 10001 confirmed.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q3: SecurityContext runAsUser $Q3.[0m"

# Q4: ServiceAccount (6.25%)
Q4_SA=$(ssh controlplane 'kubectl get pod report-worker -n mock-ckad-1-q4 -o jsonpath="{.spec.serviceAccountName}" 2>/dev/null || echo ""')
Q4_AUTO=$(ssh controlplane 'kubectl get pod report-worker -n mock-ckad-1-q4 -o jsonpath="{.spec.automountServiceAccountToken}" 2>/dev/null || echo ""')
[ "$Q4_SA" == "report-runner" ] && [ "$Q4_AUTO" == "false" ] && { echo -e "[0;32m[PASS] Q4: report-worker SA & automount=false verified.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q4: SA or automount incorrect.[0m"

# Q5: Multi-Container Sidecar (6.67%)
Q5=$(ssh controlplane 'kubectl get pod app-with-sidecar -n mock-ckad-1-q5 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
[ "$Q5" -eq 2 ] && { echo -e "[0;32m[PASS] Q5: app-with-sidecar has 2/2 ready containers.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q5: Ready containers: $Q5 (expected 2).[0m"

# Q6: Init Container (6.67%)
Q6=$(ssh controlplane 'kubectl get pod web-init-pod -n mock-ckad-1-q6 -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')
[ "$Q6" == "Running" ] && { echo -e "[0;32m[PASS] Q6: web-init-pod is in Running state.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q6: web-init-pod status: '$Q6'.[0m"

# Q7: PV & PVC (6.67%)
Q7=$(ssh controlplane 'kubectl get pod pvc-pod -n mock-ckad-1-q7 -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')
[ "$Q7" == "Running" ] && { echo -e "[0;32m[PASS] Q7: pvc-pod running with bound volume.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q7: pvc-pod status: '$Q7'.[0m"

# Q8: Rolling Update (6.67%)
Q8_IMG=$(ssh controlplane 'kubectl get deployment store-api -n mock-ckad-1-q8 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
[ "$Q8_IMG" == "nginx:1.25.4-alpine" ] && { echo -e "[0;32m[PASS] Q8: store-api upgraded to nginx:1.25.4-alpine.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q8: store-api image '$Q8_IMG'.[0m"

# Q9: Blue/Green (6.67%)
Q9=$(ssh controlplane 'kubectl get svc payments-svc -n mock-ckad-1-q9 -o jsonpath="{.spec.selector.version}" 2>/dev/null || echo ""')
[ "$Q9" == "v2" ] && { echo -e "[0;32m[PASS] Q9: payments-svc cutover to version v2.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q9: Service selector: '$Q9'.[0m"

# Q10: Canary (6.67%)
Q10=$(ssh controlplane 'kubectl get deployment frontend-canary -n mock-ckad-1-q10 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q10" -ge 2 ] && { echo -e "[0;32m[PASS] Q10: frontend-canary has 2 ready replicas.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q10: Canary ready: $Q10.[0m"

# Q11: NetworkPolicy (6.67%)
Q11=$(ssh controlplane 'kubectl get networkpolicy db-access-policy -n mock-ckad-1-q11 -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo 0')
[ "$Q11" == "5432" ] && { echo -e "[0;32m[PASS] Q11: db-access-policy enforces port 5432.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q11: Policy port mismatch: $Q11.[0m"

# Q12: Ingress (6.67%)
Q12=$(ssh controlplane 'kubectl get ingress api-ingress -n mock-ckad-1-q12 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
[ "$Q12" == "store.example.com" ] && { echo -e "[0;32m[PASS] Q12: api-ingress host store.example.com configured.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q12: Ingress host '$Q12'.[0m"

# Q13: NodePort Svc (6.67%)
Q13=$(ssh controlplane 'kubectl get svc inventory-np -n mock-ckad-1-q13 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo 0')
[ "$Q13" -eq 30088 ] && { echo -e "[0;32m[PASS] Q13: inventory-np nodePort 30088 verified.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q13: nodePort $Q13 (expected 30088).[0m"

# Q14: Probes (5.0%)
Q14=$(ssh controlplane 'kubectl get pod probed-web -n mock-ckad-1-q14 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
[ "$Q14" == "true" ] && { echo -e "[0;32m[PASS] Q14: probed-web passing health checks (Ready).[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q14: Pod ready: '$Q14'.[0m"

# Q15: Pod Debugging (5.0%)
Q15_READY=$(ssh controlplane 'kubectl get pod order-worker -n mock-ckad-1-q15 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
Q15_ENV=$(ssh controlplane 'kubectl get pod order-worker -n mock-ckad-1-q15 -o jsonpath="{.spec.containers[0].env[?(@.name=="DB_HOST")].value}" 2>/dev/null || echo ""')
[ "$Q15_READY" == "true" ] && [ "$Q15_ENV" == "postgres" ] && { echo -e "[0;32m[PASS] Q15: order-worker debugged (Ready & DB_HOST=postgres).[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q15: order-worker ready='$Q15_READY', DB_HOST='$Q15_ENV'.[0m"

# Q16: Log Extraction (5.0%)
Q16=$(ssh controlplane 'grep -c "FATAL" /tmp/fatal-errors.txt 2>/dev/null || echo 0')
[ "$Q16" -ge 1 ] && { echo -e "[0;32m[PASS] Q16: /tmp/fatal-errors.txt contains $Q16 FATAL log lines.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q16: Log file missing or empty.[0m"

PCT=$(( SCORE * 100 / TOTAL ))
echo "=========================================================================="
echo "Final Score: $SCORE / $TOTAL ($PCT%)"
[ $PCT -ge 66 ] && { echo -e "[0;32mPASSED! Congratulations on clearing CKAD Mock Exam 1! (Threshold: 66%)[0m"; exit 0; } || { echo -e "[0;31mFAILED ($PCT% < 66%)[0m"; exit 1; }