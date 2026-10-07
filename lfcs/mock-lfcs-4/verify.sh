#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-lfcs-4: LFCS Full-Scale Timed Mock Exam 4 (Benchmark)...${NC}"
# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 4 against Linux Foundation Domain Weights...${NC}"

# Q1: Awk columnar calculation (Essential Commands - 20%)
TOTAL_CALC=$(cat /var/tmp/mock-lfcs-4/electronics_total.txt 2>/dev/null | tr -d '[:space:]' || echo "0")
if [ "$TOTAL_CALC" = "600" ]; then
  echo -e "${GREEN}[PASS] Q1: electronics_total.txt awk calculation (600) verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: electronics_total.txt value: '$TOTAL_CALC' (expected 600).${NC}"
fi

# Q2: Bulk file permission hardening (Essential Commands - 20%)
M1=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/old_backup.bak 2>/dev/null || echo "")
M2=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/legacy_data.old 2>/dev/null || echo "")
M3=$(stat -c %a /var/tmp/mock-lfcs-4/archive_vault/recent.bak 2>/dev/null || echo "")
if [ "$M1" = "600" ] && [ "$M2" = "600" ] && [ "$M3" = "644" ] && [ -s /var/tmp/mock-lfcs-4/vault_audit.txt ]; then
  echo -e "${GREEN}[PASS] Q2: Bulk find -exec chmod 600 and vault_audit.txt verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: Permissions not updated to 0600 on mtime +7 files or audit missing.${NC}"
fi

# Q3: SSL/TLS certificate inspection (Essential Commands - 20%)
if [ -s /var/tmp/mock-lfcs-4/cert-summary.txt ] && grep -qiE "notAfter|notAfter=" /var/tmp/mock-lfcs-4/cert-summary.txt && grep -qi "issuer" /var/tmp/mock-lfcs-4/cert-summary.txt && grep -qi "SHA256 Fingerprint" /var/tmp/mock-lfcs-4/cert-summary.txt; then
  echo -e "${GREEN}[PASS] Q3: cert-summary.txt openssl x509 details verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: cert-summary.txt missing or lacks required certificate fields.${NC}"
fi

# Q4: Git cherry-picking (Essential Commands - 20%)
if git -C /var/tmp/mock-lfcs-4/code-repo log --oneline 2>/dev/null | grep -q "HOTFIX: fix buffer overflow" && [ "$(git -C /var/tmp/mock-lfcs-4/code-repo branch --show-current 2>/dev/null)" = "main" ]; then
  echo -e "${GREEN}[PASS] Q4: Git cherry-pick on branch main verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: Branch main does not contain cherry-picked hotfix commit.${NC}"
fi

# Q5: Custom systemd slice (Operations Deployment - 25%)
SLICE_VAL=$(systemctl show batch-worker.service -p Slice --value 2>/dev/null || echo "")
MEM_VAL=$(systemctl show batch.slice -p MemoryMax --value 2>/dev/null || echo "")
CPU_VAL=$(systemctl show batch.slice -p CPUWeight --value 2>/dev/null || echo "")
if [ "$SLICE_VAL" = "batch.slice" ] && [ "$MEM_VAL" = "134217728" ] && [ "$CPU_VAL" = "150" ]; then
  echo -e "${GREEN}[PASS] Q5: batch.slice resource configuration (128M, CPUWeight 150) verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: batch.slice mismatch (Slice: $SLICE_VAL, Mem: $MEM_VAL, CPUWeight: $CPU_VAL).${NC}"
fi

# Q6: Kernel security sysctl parameters (Operations Deployment - 25%)
V_SRC=$(sysctl -n net.ipv4.conf.all.accept_source_route 2>/dev/null || echo "1")
V_ICMP=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")
V_SYN=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
if [ -f /etc/sysctl.d/99-security.conf ] && [ "$V_SRC" = "0" ] && [ "$V_ICMP" = "1" ] && [ "$V_SYN" = "1" ]; then
  echo -e "${GREEN}[PASS] Q6: Kernel security parameters in /etc/sysctl.d/99-security.conf verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: Kernel security sysctl parameters mismatch or not persistent.${NC}"
fi

# Q7: Automated backup script with rsync (Operations Deployment - 25%)
if [ -x /usr/local/bin/system_backup.sh ] && /usr/local/bin/system_backup.sh 2>/dev/null && [ -f /var/tmp/mock-lfcs-4/backup/file1.txt ] && [ -f /var/log/backup_sync.log ] && grep -q "SUCCESS" /var/log/backup_sync.log; then
  echo -e "${GREEN}[PASS] Q7: system_backup.sh rsync synchronization and logging verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: system_backup.sh execution failed or /var/log/backup_sync.log missing.${NC}"
fi

# Q8: Dynamic linker library path (Operations Deployment - 25%)
if [ -f /etc/ld.so.conf.d/customlib.conf ] && grep -q "/opt/customlib" /etc/ld.so.conf.d/customlib.conf && ldconfig -p 2>/dev/null | grep -q "/opt/customlib"; then
  echo -e "${GREEN}[PASS] Q8: Dynamic linker library cache /opt/customlib verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: ld.so.conf.d/customlib.conf missing or /opt/customlib not in ldconfig -p.${NC}"
fi

# Q9: Podman container with volume and env (Operations Deployment - 25%)
if podman ps --format "{{.Names}}" 2>/dev/null | grep -q "mock-backup-job" && podman inspect mock-backup-job --format '{{json .Config.Env}}' 2>/dev/null | grep -q "BACKUP_INTERVAL=3600" && [ -f /var/tmp/mock-lfcs-4/cdata/status.txt ] && grep -q "active" /var/tmp/mock-lfcs-4/cdata/status.txt; then
  echo -e "${GREEN}[PASS] Q9: Podman container mock-backup-job volume and env verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-backup-job missing or volume mount failed.${NC}"
fi

# Q10: HAProxy layer 7 load balancer (Networking - 25%)
if systemctl is-active haproxy &>/dev/null && ss -tlpn 2>/dev/null | grep -q ":8088 " && grep -q "balance roundrobin" /etc/haproxy/haproxy.cfg 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q10: HAProxy HTTP load balancer on port 8088 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: HAProxy not running on port 8088 or haproxy.cfg incorrect.${NC}"
fi

# Q11: Network bonding bond0 (Networking - 25%)
if ip link show bond0 &>/dev/null && grep -qi "active-backup" /proc/net/bonding/bond0 2>/dev/null && grep -qi "veth-bond1" /proc/net/bonding/bond0 2>/dev/null && ip addr show bond0 2>/dev/null | grep -q "192.168.99.10/24"; then
  echo -e "${GREEN}[PASS] Q11: Network bonding bond0 (active-backup, 192.168.99.10/24) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: bond0 interface missing or slaves not attached.${NC}"
fi

# Q12: Iptables stateful packet filtering & rate limiting (Networking - 25%)
if sudo iptables -L INPUT -n 2>/dev/null | grep -qiE "RELATED.*ESTABLISHED|ESTABLISHED.*RELATED" && sudo iptables -L INPUT -n 2>/dev/null | grep -qiE "limit: avg 2/sec|limit 2/sec" && [ -s /var/tmp/mock-lfcs-4/iptables-input.txt ]; then
  echo -e "${GREEN}[PASS] Q12: Iptables stateful filter and ICMP rate limit verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: Iptables INPUT rules missing or iptables-input.txt empty.${NC}"
fi

# Q13: Network socket states audit with ss (Networking - 25%)
if [ -s /var/tmp/mock-lfcs-4/tcp-established.txt ] && grep -qiE "ESTAB|State|Recv-Q" /var/tmp/mock-lfcs-4/tcp-established.txt && [ -f /var/tmp/mock-lfcs-4/udp-listening.txt ] && grep -qiE "UNCONN|State|Recv-Q" /var/tmp/mock-lfcs-4/udp-listening.txt; then
  echo -e "${GREEN}[PASS] Q13: Socket reports (tcp-established.txt & udp-listening.txt) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: tcp-established.txt or udp-listening.txt missing or empty.${NC}"
fi

# Q14: 802.1Q VLAN interface (Networking - 25%)
if ip -d link show dummy0.50 2>/dev/null | grep -q "id 50" && ip addr show dummy0.50 2>/dev/null | grep -q "10.50.50.1/24"; then
  echo -e "${GREEN}[PASS] Q14: 802.1Q VLAN dummy0.50 (ID 50, 10.50.50.1/24) verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: VLAN dummy0.50 missing or IP not assigned.${NC}"
fi

# Q15: Storage I/O monitoring with iotop (Storage - 20%)
if [ -s /var/tmp/mock-lfcs-4/iotop-report.txt ] && grep -qi "Total DISK" /var/tmp/mock-lfcs-4/iotop-report.txt && [ -s /var/tmp/mock-lfcs-4/high-io-proc.txt ] && grep -qiE "dd|io_burn|python" /var/tmp/mock-lfcs-4/high-io-proc.txt; then
  echo -e "${GREEN}[PASS] Q15: iotop-report.txt and high I/O process identification verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: iotop-report.txt or high-io-proc.txt missing or invalid.${NC}"
fi

# Q16: Automounter indirect map autofs (Storage - 20%)
if systemctl is-active autofs &>/dev/null && [ -f /etc/auto.master.d/shares.autofs ] && [ -f /shares/docs/policy.pdf ]; then
  echo -e "${GREEN}[PASS] Q16: autofs indirect automount /shares/docs verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: autofs indirect map failed to mount /shares/docs.${NC}"
fi

# Q17: LVM Striped Logical Volume (Storage - 20%)
STRIPES_NUM=$(sudo lvs mock-vg4/mock-striped --noheadings -o stripes 2>/dev/null | tr -d ' ' || echo "0")
if [ "$STRIPES_NUM" = "2" ] && sudo blkid /dev/mock-vg4/mock-striped 2>/dev/null | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Q17: LVM 2-stripe logical volume mock-striped verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: mock-striped volume missing or not 2-stripe ext4.${NC}"
fi

# Q18: Filesystem disk quotas (Storage - 20%)
QUOTA_OUT=$(sudo quota -v -u tester-quota 2>/dev/null || true)
if echo "$QUOTA_OUT" | grep -q "40960.*61440"; then
  echo -e "${GREEN}[PASS] Q18: Filesystem disk quota (soft 40M, hard 60M) verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: Quota for tester-quota not set to 40960/61440 limits.${NC}"
fi

# Q19: Centralized identity lookup SSSD / NSS (Users and Groups - 10%)
if grep -E "^passwd:.*sss" /etc/nsswitch.conf &>/dev/null && grep -E "^group:.*sss" /etc/nsswitch.conf &>/dev/null && [ -f /etc/sssd/sssd.conf ] && [ "$(stat -c %a /etc/sssd/sssd.conf)" = "600" ] && sudo grep -q "domain/local" /etc/sssd/sssd.conf; then
  echo -e "${GREEN}[PASS] Q19: SSSD and nsswitch.conf centralized identity config verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: nsswitch.conf lacks sss or /etc/sssd/sssd.conf incorrect.${NC}"
fi

# Q20: User account expiration and password reset (Users and Groups - 10%)
CHAGE_INFO=$(sudo chage -l temp-auditor 2>/dev/null || true)
if id temp-auditor &>/dev/null && echo "$CHAGE_INFO" | grep -qi "Account expires.*Dec 31, 2026" && echo "$CHAGE_INFO" | grep -qi "Password must be changed"; then
  echo -e "${GREEN}[PASS] Q20: User temp-auditor expiration and password reset verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: temp-auditor missing or expiration/password reset not configured.${NC}"
fi


PCT_OPS=$(awk "BEGIN {printf \"%.1f\", $SCORE_OPS * 25.0 / $TOTAL_OPS}")
PCT_NET=$(awk "BEGIN {printf \"%.1f\", $SCORE_NET * 25.0 / $TOTAL_NET}")
PCT_STOR=$(awk "BEGIN {printf \"%.1f\", $SCORE_STOR * 20.0 / $TOTAL_STOR}")
PCT_CMD=$(awk "BEGIN {printf \"%.1f\", $SCORE_CMD * 20.0 / $TOTAL_CMD}")
PCT_USER=$(awk "BEGIN {printf \"%.1f\", $SCORE_USER * 10.0 / $TOTAL_USER}")

TOTAL_PCT=$(awk "BEGIN {printf \"%.1f\", ($SCORE_OPS * 25.0 / $TOTAL_OPS) + ($SCORE_NET * 25.0 / $TOTAL_NET) + ($SCORE_STOR * 20.0 / $TOTAL_STOR) + ($SCORE_CMD * 20.0 / $TOTAL_CMD) + ($SCORE_USER * 10.0 / $TOTAL_USER)}")

echo ""
echo "────────────────────────────────────────────────────────────"
echo -e "${BOLD}Linux Foundation Domain Weight Breakdown (LFCS):${NC}"
echo -e "  • Operations Deployment (25%):                       ${SCORE_OPS}/${TOTAL_OPS} passed   (${PCT_OPS}% / 25.0%)"
echo -e "  • Networking (25%):                                  ${SCORE_NET}/${TOTAL_NET} passed   (${PCT_NET}% / 25.0%)"
echo -e "  • Storage (20%):                                     ${SCORE_STOR}/${TOTAL_STOR} passed   (${PCT_STOR}% / 20.0%)"
echo -e "  • Essential Commands (20%):                          ${SCORE_CMD}/${TOTAL_CMD} passed   (${PCT_CMD}% / 20.0%)"
echo -e "  • Users and Groups (10%):                            ${SCORE_USER}/${TOTAL_USER} passed   (${PCT_USER}% / 10.0%)"
echo "────────────────────────────────────────────────────────────"
echo -e "Questions Passed:     ${BOLD}${TOTAL_PASSED} / ${TOTAL_QUESTIONS}${NC}"
echo -e "Final Weighted Score: ${BOLD}${TOTAL_PCT}%${NC}"
echo -e "Passing Threshold:    67.0%"
echo "────────────────────────────────────────────────────────────"

IS_PASS=$(awk "BEGIN {if ($TOTAL_PCT >= 67.0) print 1; else print 0}")
if [ "$IS_PASS" -eq 1 ]; then
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-lfcs-4 completed successfully! (${TOTAL_PCT}% >= 67.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (67.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-lfcs-4${NC}"
  exit 1
fi
