#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-lfcs-2 (LFCS Full-Scale Timed Mock Exam 2)..."
sudo rm -rf /var/tmp/mock-lfcs-2 /etc/rsyslog.d/40-custom.conf /etc/apt/preferences.d/pin-package /etc/skel/.custom_profile
sudo mkdir -p /var/tmp/mock-lfcs-2/mnt-point && sudo chown -R student:student /var/tmp/mock-lfcs-2 && sudo chmod -R 777 /var/tmp/mock-lfcs-2
# Q1 sample
cat << 'EOF' > /var/tmp/mock-lfcs-2/app.conf
[app]
HOST = 0.0.0.0
PORT = 8080
DEBUG = true
TIMEOUT = 30
EOF
# Q2 syslog sample
cat << 'EOF' > /var/tmp/mock-lfcs-2/sample_syslog
Sep 14 10:00:01 host sshd[100]: session opened
Sep 14 10:00:02 host kernel: [0.123] disk ok
Sep 14 10:00:03 host sshd[101]: session closed
Sep 14 10:00:04 host systemd[1]: started timer
Sep 14 10:00:05 host sshd[102]: login ok
EOF
# Q3 diff sample
echo -e "line1
line2" > /var/tmp/mock-lfcs-2/fileA
echo -e "line1
line2_modified
line3" > /var/tmp/mock-lfcs-2/fileB
cp /var/tmp/mock-lfcs-2/fileA /var/tmp/mock-lfcs-2/fileTarget
# Q15 LVM setup
dd if=/dev/zero of=/var/tmp/mock-lfcs-2/lvm2.img bs=1M count=100 2>/dev/null || true
LOOP=$(sudo losetup -f --show /var/tmp/mock-lfcs-2/lvm2.img 2>/dev/null || true)
if [ -n "$LOOP" ]; then
  sudo pvcreate "$LOOP" 2>/dev/null || true
  sudo vgcreate mock-vg2 "$LOOP" 2>/dev/null || true
  sudo lvcreate -L 40M -n data-lv mock-vg2 2>/dev/null || true
  sudo mkfs.ext4 /dev/mock-vg2/data-lv 2>/dev/null || true
fi
# Q16 tunable image
dd if=/dev/zero of=/var/tmp/mock-lfcs-2/tunable.img bs=1M count=50 2>/dev/null || true
mkfs.ext4 -F /var/tmp/mock-lfcs-2/tunable.img 2>/dev/null || true
sudo userdel -r newhire 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show mock-lfcs-2"
