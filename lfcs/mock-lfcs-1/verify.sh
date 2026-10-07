#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-lfcs-1: LFCS Full-Scale Timed Mock Exam 1...${NC}"
# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 1 against Linux Foundation Domain Weights...${NC}"

# Q1: Git repo (Essential Commands - 20%)
if [ -d /var/tmp/mock-lfcs-1/git-repo/.git ] && git -C /var/tmp/mock-lfcs-1/git-repo log --oneline 2>/dev/null | grep -q "feature"; then
  echo -e "${GREEN}[PASS] Q1: Git repository and feature branch merge verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: Git repo or feature commit missing.${NC}"
fi

# Q2: Systemd service (Essential Commands - 20%)
if systemctl is-active mock-monitor.service &>/dev/null; then
  echo -e "${GREEN}[PASS] Q2: mock-monitor.service is active.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: mock-monitor.service not active.${NC}"
fi

# Q3: Large files find (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-1/large-files.txt ] && grep -q "sample_large.bin" /var/tmp/mock-lfcs-1/large-files.txt; then
  echo -e "${GREEN}[PASS] Q3: Large files report verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: large-files.txt missing or lacks entries.${NC}"
fi

# Q4: SSL Cert Info (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-1/cert-info.txt ] && grep -qi "exam.local" /var/tmp/mock-lfcs-1/cert-info.txt; then
  echo -e "${GREEN}[PASS] Q4: cert-info.txt verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: cert-info.txt missing or lacks subject info.${NC}"
fi

# Q5: Swappiness (Operations Deployment - 25%)
if [ -f /etc/sysctl.d/99-swappiness.conf ] && [ "$(sysctl -n vm.swappiness)" == "10" ]; then
  echo -e "${GREEN}[PASS] Q5: vm.swappiness=10 persistently configured.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: vm.swappiness is $(sysctl -n vm.swappiness) (expected 10).${NC}"
fi

# Q6: Crontab student (Operations Deployment - 25%)
if crontab -u student -l 2>/dev/null | grep -q "30 2 \* \* 1-5"; then
  echo -e "${GREEN}[PASS] Q6: Crontab schedule verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: Crontab entry for student missing.${NC}"
fi

# Q7: Package file count (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-1/pkg-files.txt ] && [ -s /var/tmp/mock-lfcs-1/pkg-files.txt ]; then
  echo -e "${GREEN}[PASS] Q7: Package files query recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: pkg-files.txt missing or empty.${NC}"
fi

# Q8: Sleep PID (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-1/sleep.pid ] && pgrep -F /var/tmp/mock-lfcs-1/sleep.pid &>/dev/null; then
  echo -e "${GREEN}[PASS] Q8: Process PID recorded and running.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: Process PID missing or not running.${NC}"
fi

# Q9: Container mock-web (Operations Deployment - 25%)
if (docker ps 2>/dev/null || podman ps 2>/dev/null) | grep -q "mock-web"; then
  echo -e "${GREEN}[PASS] Q9: Container mock-web is running.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-web not running.${NC}"
fi

# Q10: /etc/hosts entry (Networking - 25%)
if grep -q "exam.local" /etc/hosts; then
  echo -e "${GREEN}[PASS] Q10: /etc/hosts contains exam.local.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: /etc/hosts lacks exam.local.${NC}"
fi

# Q11: Timedatectl (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/time-status.txt ] && grep -qi "Time zone" /var/tmp/mock-lfcs-1/time-status.txt; then
  echo -e "${GREEN}[PASS] Q11: time-status.txt verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: time-status.txt missing.${NC}"
fi

# Q12: Listening ports (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/listening-ports.txt ] && grep -qi "LISTEN" /var/tmp/mock-lfcs-1/listening-ports.txt; then
  echo -e "${GREEN}[PASS] Q12: listening-ports.txt verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: listening-ports.txt missing or empty.${NC}"
fi

# Q13: SSH drop-in config (Networking - 25%)
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -qi "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf; then
  echo -e "${GREEN}[PASS] Q13: SSH hardening drop-in verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: 99-hardening.conf missing or incomplete.${NC}"
fi

# Q14: Firewall status (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-1/firewall-rules.txt ] && [ -s /var/tmp/mock-lfcs-1/firewall-rules.txt ]; then
  echo -e "${GREEN}[PASS] Q14: Firewall rules report verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: firewall-rules.txt missing.${NC}"
fi

# Q15: Ext4 Disk Image (Storage - 20%)
if [ -f /var/tmp/mock-lfcs-1/disk1.img ] && file /var/tmp/mock-lfcs-1/disk1.img | grep -qi "ext4"; then
  echo -e "${GREEN}[PASS] Q15: disk1.img created and formatted as ext4.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: disk1.img missing or not ext4.${NC}"
fi

# Q16: LVM volume mount (Storage - 20%)
if mountpoint -q /var/tmp/mock-lfcs-1/lvm-mount 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q16: LVM logical volume mounted at lvm-mount.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: lvm-mount is not mounted.${NC}"
fi

# Q17: LVM extend size (Storage - 20%)
LV_SIZE=$(lvs --noheadings -o lv_size mock-vg/mock-lv 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SIZE" | grep -q "80"; then
  echo -e "${GREEN}[PASS] Q17: Logical volume extended to 80M.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: LV size is '$LV_SIZE' (expected 80M).${NC}"
fi

# Q18: Swapfile (Storage - 20%)
if swapon --show | grep -q "mock-lfcs-1/swapfile"; then
  echo -e "${GREEN}[PASS] Q18: Swapfile active.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: swapfile is not active.${NC}"
fi

# Q19: Users, Group & ACL (Users and Groups - 10%)
ACL_CHECK=$(getfacl /var/tmp/mock-lfcs-1/shared 2>/dev/null || true)
if id devops &>/dev/null && id tester &>/dev/null && echo "$ACL_CHECK" | grep -q "group:infrateam:rwx"; then
  echo -e "${GREEN}[PASS] Q19: Users devops, tester and ACL on shared directory verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: Users or ACL missing on /var/tmp/mock-lfcs-1/shared.${NC}"
fi

# Q20: Limits & Password aging (Users and Groups - 10%)
CHAGE_VAL=$(chage -l student 2>/dev/null | grep -i "Maximum" | awk -F: '{print $2}' | tr -d ' ' || echo "0")
if [ "$CHAGE_VAL" == "90" ] && grep -q "student.*nofile.*4096" /etc/security/limits.conf; then
  echo -e "${GREEN}[PASS] Q20: Password max age (90 days) and nofile limits verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: chage max age is '$CHAGE_VAL' (expected 90) or limits.conf missing.${NC}"
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
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-lfcs-1 completed successfully! (${TOTAL_PCT}% >= 67.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (67.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-lfcs-1${NC}"
  exit 1
fi
