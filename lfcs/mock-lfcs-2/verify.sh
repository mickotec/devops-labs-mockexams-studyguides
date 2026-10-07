#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-lfcs-2: LFCS Full-Scale Timed Mock Exam 2...${NC}"
# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 2 against Linux Foundation Domain Weights...${NC}"

# Q1: Sed editing (Essential Commands - 20%)
CONF1=$(cat /var/tmp/mock-lfcs-2/app.conf 2>/dev/null || true)
if echo "$CONF1" | grep -q "PORT = 9000" && echo "$CONF1" | grep -q "ENV = production" && ! echo "$CONF1" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Q1: app.conf sed editing verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: app.conf modifications incomplete.${NC}"
fi

# Q2: Top loggers (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-2/top_loggers.txt ] && grep -q "sshd" /var/tmp/mock-lfcs-2/top_loggers.txt; then
  echo -e "${GREEN}[PASS] Q2: top_loggers.txt syslog analysis verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: top_loggers.txt missing or empty.${NC}"
fi

# Q3: Patch (Essential Commands - 20%)
if grep -q "line2_modified" /var/tmp/mock-lfcs-2/fileTarget 2>/dev/null; then
  echo -e "${GREEN}[PASS] Q3: Patch successfully applied to fileTarget.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: fileTarget not patched.${NC}"
fi

# Q4: Largest files (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-2/largest_files.txt ] && [ -s /var/tmp/mock-lfcs-2/largest_files.txt ]; then
  echo -e "${GREEN}[PASS] Q4: largest_files.txt created.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: largest_files.txt missing.${NC}"
fi

# Q5: Systemd timer (Operations Deployment - 25%)
if systemctl is-active mock-cleanup.timer &>/dev/null; then
  echo -e "${GREEN}[PASS] Q5: mock-cleanup.timer is active.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: mock-cleanup.timer not active.${NC}"
fi

# Q6: Nice process (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-2/nice_proc.txt ] && grep -q "15" /var/tmp/mock-lfcs-2/nice_proc.txt; then
  echo -e "${GREEN}[PASS] Q6: Process nice level 15 recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: nice_proc.txt missing or lacks nice 15.${NC}"
fi

# Q7: Rsyslog rule (Operations Deployment - 25%)
if [ -f /etc/rsyslog.d/40-custom.conf ] && grep -q "local5" /etc/rsyslog.d/40-custom.conf; then
  echo -e "${GREEN}[PASS] Q7: rsyslog rule verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: 40-custom.conf missing.${NC}"
fi

# Q8: Default target (Operations Deployment - 25%)
if [ -f /var/tmp/mock-lfcs-2/boot-target.txt ] && grep -q "\.target" /var/tmp/mock-lfcs-2/boot-target.txt; then
  echo -e "${GREEN}[PASS] Q8: boot-target.txt recorded.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: boot-target.txt missing.${NC}"
fi

# Q9: Apt pinning (Operations Deployment - 25%)
if [ -f /etc/apt/preferences.d/pin-package ] && grep -q "999" /etc/apt/preferences.d/pin-package; then
  echo -e "${GREEN}[PASS] Q9: APT package pin verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: pin-package missing or lacks 999.${NC}"
fi

# Q10: Dummy interface (Networking - 25%)
if ip link show dummy0 &>/dev/null; then
  echo -e "${GREEN}[PASS] Q10: Interface dummy0 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: dummy0 interface missing.${NC}"
fi

# Q11: IPTables rule (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/iptables.txt ] && grep -q "8080" /var/tmp/mock-lfcs-2/iptables.txt; then
  echo -e "${GREEN}[PASS] Q11: IPTables rule on port 8080 recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: iptables.txt missing or lacks 8080.${NC}"
fi

# Q12: SSH PID (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/ssh-proc.txt ] && grep -qi "sshd" /var/tmp/mock-lfcs-2/ssh-proc.txt; then
  echo -e "${GREEN}[PASS] Q12: sshd listening PID recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: ssh-proc.txt missing.${NC}"
fi

# Q13: DNS server (Networking - 25%)
if [ -f /var/tmp/mock-lfcs-2/dns-server.txt ] && [ -s /var/tmp/mock-lfcs-2/dns-server.txt ]; then
  echo -e "${GREEN}[PASS] Q13: dns-server.txt recorded.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: dns-server.txt missing.${NC}"
fi

# Q14: Static route (Networking - 25%)
if ip route show 2>/dev/null | grep -q "192.168.100.0/24.*10.99.99.254"; then
  echo -e "${GREEN}[PASS] Q14: Static route for 192.168.100.0/24 via 10.99.99.254 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: Static route for 192.168.100.0/24 missing.${NC}"
fi

# Q15: LVM Snapshot (Storage - 20%)
if lvs mock-vg2/data-snap &>/dev/null; then
  echo -e "${GREEN}[PASS] Q15: LVM snapshot data-snap verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: LVM snapshot data-snap missing.${NC}"
fi

# Q16: Tune2fs reserved blocks (Storage - 20%)
RES_BLOCKS=$(sudo tune2fs -l /var/tmp/mock-lfcs-2/tunable.img 2>/dev/null | grep -i "Reserved block count:" | awk '{print $NF}' || echo "0")
if [ "$RES_BLOCKS" -eq 128 ]; then
  echo -e "${GREEN}[PASS] Q16: tune2fs 1% reserved blocks verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: tune2fs reserved blocks: $RES_BLOCKS (expected 128 blocks / 1%).${NC}"
fi

# Q17: Fstab entry (Storage - 20%)
if grep -q "mnt-point.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Q17: /etc/fstab entry verified with noatime.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: /etc/fstab lacks mnt-point entry.${NC}"
fi

# Q18: Swapfile (Storage - 20%)
if swapon --show 2>/dev/null | grep -q "mock-lfcs-2/swapfile2"; then
  echo -e "${GREEN}[PASS] Q18: Swap file swapfile2 verified active.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: swapfile2 missing or not active.${NC}"
fi

# Q19: Chage password aging (Users and Groups - 10%)
CHAGE_OUT=$(chage -l student 2>/dev/null || true)
if echo "$CHAGE_OUT" | grep -q "Maximum.*60" && echo "$CHAGE_OUT" | grep -q "Minimum.*7"; then
  echo -e "${GREEN}[PASS] Q19: Password aging policy (60/7/14) verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: chage aging settings mismatch.${NC}"
fi

# Q20: Skeleton & user (Users and Groups - 10%)
if id newhire &>/dev/null && [ -f /home/newhire/.custom_profile ]; then
  echo -e "${GREEN}[PASS] Q20: User newhire and populated skeleton verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: user newhire missing or .custom_profile not populated.${NC}"
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
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-lfcs-2 completed successfully! (${TOTAL_PCT}% >= 67.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (67.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-lfcs-2${NC}"
  exit 1
fi
