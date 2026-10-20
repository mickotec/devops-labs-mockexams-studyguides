#!/usr/bin/env bash
set -uo pipefail
SCORE=0; TOTAL=16

echo "=========================================================================="
echo "          CKAD killer.sh Mock Exam 2 Scorecard & Evaluation               "
echo "=========================================================================="

# Q1: Secret envFrom (6.25%)
Q1=$(ssh controlplane 'kubectl get pod token-consumer -n mock-ckad-2-q1 -o jsonpath="{.spec.containers[0].envFrom[0].secretRef.name}" 2>/dev/null || echo ""')
[ "$Q1" == "api-tokens" ] && { echo -e "[0;32m[PASS] Q1: token-consumer envFrom api-tokens.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q1: secretRef mismatch.[0m"

# Q2: Quota (6.25%)
Q2=$(ssh controlplane 'kubectl get pods -n mock-ckad-2-q2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo ""')
[ "$Q2" == "Running" ] && { echo -e "[0;32m[PASS] Q2: Quota pod Running.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q2: Pod status: '$Q2'.[0m"

# Q3: SecurityContext (6.25%)
Q3=$(ssh controlplane 'kubectl get pod isolated-app -n mock-ckad-2-q3 -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo ""')
[ "$Q3" == "true" ] && { echo -e "[0;32m[PASS] Q3: isolated-app readOnlyRootFilesystem=true.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q3: SecurityContext mismatch.[0m"

# Q4: RBAC (6.25%)
Q4=$(ssh controlplane 'kubectl get rolebinding bind-secret-viewer -n mock-ckad-2-q4 -o jsonpath="{.roleRef.name}" 2>/dev/null || echo ""')
[ "$Q4" == "secret-viewer" ] && { echo -e "[0;32m[PASS] Q4: bind-secret-viewer references secret-viewer.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q4: RoleBinding mismatch.[0m"

# Q5: CronJob (6.67%)
Q5=$(ssh controlplane 'kubectl get cronjob db-backup-cron -n mock-ckad-2-q5 -o jsonpath="{.spec.concurrencyPolicy}" 2>/dev/null || echo ""')
[ "$Q5" == "Forbid" ] && { echo -e "[0;32m[PASS] Q5: db-backup-cron concurrencyPolicy=Forbid.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q5: CronJob mismatch.[0m"

# Q6: Adapter (6.67%)
Q6=$(ssh controlplane 'kubectl get pod metric-adapter -n mock-ckad-2-q6 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
[ "$Q6" -eq 2 ] && { echo -e "[0;32m[PASS] Q6: metric-adapter has 2 ready containers.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q6: Ready count: $Q6.[0m"

# Q7: StatefulSet (6.67%)
Q7=$(ssh controlplane 'kubectl get statefulset db-cluster -n mock-ckad-2-q7 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q7" -ge 2 ] && { echo -e "[0;32m[PASS] Q7: db-cluster statefulset ready.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q7: StatefulSet ready: $Q7.[0m"

# Q8: Kustomize (6.67%)
Q8=$(ssh controlplane 'test -d /tmp/kustomize-store/overlays/prod && echo "OK" || echo ""')
[ "$Q8" == "OK" ] && { echo -e "[0;32m[PASS] Q8: Kustomize store structure exists.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q8: /tmp/kustomize-store missing.[0m"

# Q9: Rollback (6.67%)
Q9=$(ssh controlplane 'kubectl get deployment checkout -n mock-ckad-2-q9 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
[ "$Q9" == "nginx:1.24-alpine" ] && { echo -e "[0;32m[PASS] Q9: checkout rolled back to nginx:1.24-alpine.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q9: Image '$Q9'.[0m"

# Q10: Canary (6.67%)
Q10=$(ssh controlplane 'kubectl get deployment web-v2 -n mock-ckad-2-q10 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q10" -ge 1 ] && { echo -e "[0;32m[PASS] Q10: web-v2 canary running.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q10: web-v2 ready: $Q10.[0m"

# Q11: NetworkPolicy Deny (6.67%)
Q11=$(ssh controlplane 'kubectl get networkpolicy deny-all-ingress -n mock-ckad-2-q11 -o jsonpath="{.spec.policyTypes[0]}" 2>/dev/null || echo ""')
[ "$Q11" == "Ingress" ] && { echo -e "[0;32m[PASS] Q11: deny-all-ingress configured.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q11: Policy missing.[0m"

# Q12: Ingress (6.67%)
Q12=$(ssh controlplane 'kubectl get ingress customer-ingress -n mock-ckad-2-q12 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
[ "$Q12" == "portal.internal" ] && { echo -e "[0;32m[PASS] Q12: customer-ingress configured for portal.internal.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q12: Ingress host '$Q12'.[0m"

# Q13: Service (6.67%)
Q13=$(ssh controlplane 'kubectl get svc redis-service -n mock-ckad-2-q13 -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo 0')
[ "$Q13" -eq 6379 ] && { echo -e "[0;32m[PASS] Q13: redis-service port 6379 verified.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q13: Service port $Q13.[0m"

# Q14: Startup Probe (5.0%)
Q14=$(ssh controlplane 'kubectl get pod slow-starter -n mock-ckad-2-q14 -o jsonpath="{.spec.containers[0].startupProbe.failureThreshold}" 2>/dev/null || echo 0')
[ "$Q14" -eq 30 ] && { echo -e "[0;32m[PASS] Q14: slow-starter startup probe failureThreshold=30.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q14: Startup probe threshold $Q14.[0m"

# Q15: Deprecated API (5.0%)
Q15=$(ssh controlplane 'grep -qi "autoscaling/v2" /tmp/hpa-version.txt 2>/dev/null && echo "OK" || echo ""')
[ "$Q15" == "OK" ] && { echo -e "[0;32m[PASS] Q15: /tmp/hpa-version.txt contains autoscaling/v2.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q15: File missing or invalid.[0m"

# Q16: Top Pod (5.0%)
Q16=$(ssh controlplane 'test -s /tmp/top-pod.txt && echo "OK" || echo ""')
[ "$Q16" == "OK" ] && { echo -e "[0;32m[PASS] Q16: /tmp/top-pod.txt populated.[0m"; SCORE=$((SCORE + 1)); } || echo -e "[0;31m[FAIL] Q16: File missing.[0m"

PCT=$(( SCORE * 100 / TOTAL ))
echo "=========================================================================="
echo "Final Score: $SCORE / $TOTAL ($PCT%)"
[ $PCT -ge 66 ] && { echo -e "[0;32mPASSED! Passed CKAD Mock Exam 2![0m"; exit 0; } || { echo -e "[0;31mFAILED ($PCT% < 66%)[0m"; exit 1; }