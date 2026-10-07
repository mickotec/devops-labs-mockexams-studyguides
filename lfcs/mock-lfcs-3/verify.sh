#!/usr/bin/env bash
set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Evaluating mock-lfcs-3: LFCS Full-Scale Timed Mock Exam 3...${NC}"
# Linux Foundation LFCS Domain Tracking
SCORE_OPS=0; TOTAL_OPS=5     # 25%
SCORE_NET=0; TOTAL_NET=5     # 25%
SCORE_STOR=0; TOTAL_STOR=4   # 20%
SCORE_CMD=0; TOTAL_CMD=4     # 20%
SCORE_USER=0; TOTAL_USER=2   # 10%
TOTAL_PASSED=0; TOTAL_QUESTIONS=20
SCORE=0; TOTAL=20

echo -e "${BOLD}Evaluating LFCS Mock Exam 3 against Linux Foundation Domain Weights...${NC}"

# Q1: Web Server Error Log Parsing (Essential Commands - 20%)
if [ -s /var/tmp/mock-lfcs-3/error_ips.txt ] && grep -q "192.168.1.50" /var/tmp/mock-lfcs-3/error_ips.txt && grep -q "10.0.0.12" /var/tmp/mock-lfcs-3/error_ips.txt && ! grep -q "192.168.1.10" /var/tmp/mock-lfcs-3/error_ips.txt; then
  echo -e "${GREEN}[PASS] Q1: error_ips.txt web log analysis verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: error_ips.txt missing or incorrect IP filtering.${NC}"
fi

# Q2: SSL CSR with SAN (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-3/server.key ] && [ -f /var/tmp/mock-lfcs-3/server.csr ] && openssl req -in /var/tmp/mock-lfcs-3/server.csr -text -noout 2>/dev/null | grep -qi "lfcs.local"; then
  echo -e "${GREEN}[PASS] Q2: SSL private key and CSR with SAN verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: server.key or server.csr missing or invalid CN/SAN.${NC}"
fi

# Q3: Multi-threaded archive and checksum (Essential Commands - 20%)
if [ -f /var/tmp/mock-lfcs-3/backup.tar.xz ] && tar -tf /var/tmp/mock-lfcs-3/backup.tar.xz &>/dev/null && [ -f /var/tmp/mock-lfcs-3/backup.tar.xz.sha256 ] && (cd /var/tmp/mock-lfcs-3 && sha256sum -c backup.tar.xz.sha256 &>/dev/null); then
  echo -e "${GREEN}[PASS] Q3: backup.tar.xz multi-threaded archive and sha256 verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: backup.tar.xz or sha256 verification failed.${NC}"
fi

# Q4: Git annotated release tag and branch (Essential Commands - 20%)
if git -C /var/tmp/mock-lfcs-3/git-app tag -n 2>/dev/null | grep -q "v1.2.0.*Production Release 1.2.0" && git -C /var/tmp/mock-lfcs-3/git-app branch 2>/dev/null | grep -q "release-1.2"; then
  echo -e "${GREEN}[PASS] Q4: Git release tag v1.2.0 and release-1.2 branch verified.${NC}"; SCORE_CMD=$((SCORE_CMD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: Git tag v1.2.0 or release-1.2 branch missing.${NC}"
fi

# Q5: Systemd cgroups drop-in limits (Operations Deployment - 25%)
MEM_MAX=$(systemctl show mock-worker.service -p MemoryMax --value 2>/dev/null || echo "0")
CPU_QUOTA=$(systemctl show mock-worker.service -p CPUQuotaPerSecUSec --value 2>/dev/null || echo "0")
if [ "$MEM_MAX" = "67108864" ] && [ "$CPU_QUOTA" = "400ms" ]; then
  echo -e "${GREEN}[PASS] Q5: systemd cgroups drop-in limits (64M, 40%) verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: mock-worker.service cgroup limits mismatch (Mem: $MEM_MAX, CPU: $CPU_QUOTA).${NC}"
fi

# Q6: Kernel module blacklisting (Operations Deployment - 25%)
if [ -f /etc/modprobe.d/blacklist-cramfs.conf ] && grep -q "blacklist cramfs" /etc/modprobe.d/blacklist-cramfs.conf && grep -q "install cramfs /bin/true" /etc/modprobe.d/blacklist-cramfs.conf && ! lsmod | grep -q "^cramfs "; then
  echo -e "${GREEN}[PASS] Q6: cramfs kernel module blacklisting verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: blacklist-cramfs.conf missing or cramfs still loaded.${NC}"
fi

# Q7: Journalctl priority failure log extraction (Operations Deployment - 25%)
if [ -s /var/tmp/mock-lfcs-3/system_errors.log ] && grep -q "LFCS_MOCK3_CRITICAL_ERR" /var/tmp/mock-lfcs-3/system_errors.log; then
  echo -e "${GREEN}[PASS] Q7: system_errors.log journalctl error extraction verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: system_errors.log missing or did not capture priority err logs.${NC}"
fi

# Q8: Graceful process reload script (Operations Deployment - 25%)
if [ -x /usr/local/bin/reload_mock_app.sh ] && /usr/local/bin/reload_mock_app.sh 2>/dev/null && sleep 1 && [ -f /var/tmp/mock-lfcs-3/signal.log ] && grep -q "RELOAD SIGNAL SENT" /var/tmp/mock-lfcs-3/signal.log && [ -f /var/tmp/mock-lfcs-3/app_ack.log ]; then
  echo -e "${GREEN}[PASS] Q8: reload_mock_app.sh signal delivery and logging verified.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: reload_mock_app.sh failed or did not deliver SIGHUP.${NC}"
fi

# Q9: Podman container mock-web-c3 (Operations Deployment - 25%)
if podman ps --format "{{.Names}} {{.Ports}}" 2>/dev/null | grep -q "mock-web-c3" && podman inspect mock-web-c3 --format '{{.HostConfig.RestartPolicy.Name}}' 2>/dev/null | grep -qi "always"; then
  echo -e "${GREEN}[PASS] Q9: Podman container mock-web-c3 running with restart always.${NC}"; SCORE_OPS=$((SCORE_OPS + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: Container mock-web-c3 missing or restart policy not always.${NC}"
fi

# Q10: Nginx reverse proxy load balancer (Networking - 25%)
if systemctl is-active nginx &>/dev/null && [ -f /etc/nginx/conf.d/proxy-balance.conf ] && curl -s -m 2 http://127.0.0.1:8080 2>/dev/null | grep -qi "Backend"; then
  echo -e "${GREEN}[PASS] Q10: Nginx reverse proxy load balancer on port 8080 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: Nginx proxy-balance not responding on 8080 or backends unreachable.${NC}"
fi

# Q11: Network bridge br0 (Networking - 25%)
if ip link show br0 type bridge &>/dev/null && ip link show veth-br1 2>/dev/null | grep -q "master br0" && ip addr show br0 2>/dev/null | grep -q "192.168.50.1/24"; then
  echo -e "${GREEN}[PASS] Q11: Network bridge br0 with veth-br1 and 192.168.50.1/24 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: Bridge br0 missing or veth-br1 not enslaved.${NC}"
fi

# Q12: Iptables NAT port redirection (Networking - 25%)
if sudo iptables -t nat -L PREROUTING -n 2>/dev/null | grep -E "REDIRECT.*tcp.*dpt:8443.*redir ports 443" && [ -s /var/tmp/mock-lfcs-3/nat-rules.txt ]; then
  echo -e "${GREEN}[PASS] Q12: Iptables PREROUTING port 8443->443 redirection verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: Iptables NAT redirection rule missing or nat-rules.txt empty.${NC}"
fi

# Q13: Network packet capture with tcpdump (Networking - 25%)
# Send 5 test packets if not already sent
(for i in {1..5}; do nc -z -w 1 127.0.0.1 9999 2>/dev/null || true; done) &
if [ -s /var/tmp/mock-lfcs-3/traffic.pcap ] && [ "$(tcpdump -r /var/tmp/mock-lfcs-3/traffic.pcap 2>/dev/null | wc -l)" -ge 3 ]; then
  echo -e "${GREEN}[PASS] Q13: tcpdump traffic.pcap packet capture verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: traffic.pcap missing or does not contain captured TCP packets.${NC}"
fi

# Q14: Static route with metric (Networking - 25%)
if ip route show 10.150.0.0/16 2>/dev/null | grep -q "10.99.99.1.*metric 150"; then
  echo -e "${GREEN}[PASS] Q14: Static route 10.150.0.0/16 via 10.99.99.1 metric 150 verified.${NC}"; SCORE_NET=$((SCORE_NET + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: Static route 10.150.0.0/16 missing or metric mismatch.${NC}"
fi

# Q15: Storage Performance Monitoring (Storage - 20%)
if [ -s /var/tmp/mock-lfcs-3/io-report.txt ] && grep -qiE "Device|%util|await" /var/tmp/mock-lfcs-3/io-report.txt && [ -s /var/tmp/mock-lfcs-3/sar-disk.txt ] && grep -qiE "DEV|%util|tps" /var/tmp/mock-lfcs-3/sar-disk.txt; then
  echo -e "${GREEN}[PASS] Q15: Storage I/O monitoring reports (iostat & sar) verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: io-report.txt or sar-disk.txt missing or incomplete.${NC}"
fi

# Q16: Filesystem Automounter autofs direct map (Storage - 20%)
if systemctl is-active autofs &>/dev/null && [ -f /etc/auto.master.d/direct.autofs ] && [ -f /mnt/auto-data/auto_test.txt ]; then
  echo -e "${GREEN}[PASS] Q16: autofs direct automount /mnt/auto-data verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: autofs direct map failed to mount /mnt/auto-data.${NC}"
fi

# Q17: LVM Thin Provisioning (Storage - 20%)
if sudo lvs mock-vg3/mock-pool --noheadings -o lv_attr 2>/dev/null | grep -q "t" && sudo lvs mock-vg3/mock-thin --noheadings -o lv_attr 2>/dev/null | grep -q "V" && sudo blkid /dev/mock-vg3/mock-thin 2>/dev/null | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Q17: LVM thin pool and 150M thin volume verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: mock-pool or mock-thin missing or not formatted as ext4.${NC}"
fi

# Q18: Persistent mount by UUID with security options (Storage - 20%)
if mountpoint -q /mnt/secure-data 2>/dev/null && grep -q "UUID=" /etc/fstab && grep -q "/mnt/secure-data" /etc/fstab && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "noexec" && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "nosuid" && findmnt -n -o OPTIONS /mnt/secure-data 2>/dev/null | grep -q "nodev"; then
  echo -e "${GREEN}[PASS] Q18: Persistent UUID mount with noexec,nosuid,nodev verified.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q18: /mnt/secure-data not mounted or options/fstab incorrect.${NC}"
fi

# Q19: Granular Sudoers Delegation (Users and Groups - 10%)
SUDO_DEV=$(sudo -l -U developer 2>/dev/null || true)
if [ -f /etc/sudoers.d/90-developer ] && [ "$(stat -c %a /etc/sudoers.d/90-developer)" = "440" ] && echo "$SUDO_DEV" | grep -q "NOPASSWD: /usr/bin/systemctl restart nginx, /usr/bin/journalctl"; then
  echo -e "${GREEN}[PASS] Q19: Granular sudoers permissions for developer verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q19: 90-developer sudoers entry missing or permissions incorrect.${NC}"
fi

# Q20: SGID and Sticky Bit Collaborative Workspace (Users and Groups - 10%)
if [ -d /var/tmp/mock-lfcs-3/team_collab ] && [ "$(stat -c %a /var/tmp/mock-lfcs-3/team_collab)" = "2775" ] && [ "$(stat -c %G /var/tmp/mock-lfcs-3/team_collab)" = "devteam" ] && [ -d /var/tmp/mock-lfcs-3/team_collab/dropzone ] && [ "$(stat -c %a /var/tmp/mock-lfcs-3/team_collab/dropzone)" = "1777" ]; then
  echo -e "${GREEN}[PASS] Q20: SGID (2775) and sticky bit (1777) team directory verified.${NC}"; SCORE_USER=$((SCORE_USER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q20: team_collab or dropzone permissions/group mismatch.${NC}"
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
  echo -e "${GREEN}${BOLD}CONGRATULATIONS! Mock Exam mock-lfcs-3 completed successfully! (${TOTAL_PCT}% >= 67.0%)${NC}"
  exit 0
else
  echo -e "${RED}Score below passing threshold (67.0%). Current: ${TOTAL_PCT}%. Review domain competencies or run: ./lab solve mock-lfcs-3${NC}"
  exit 1
fi
