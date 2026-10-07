# [LFCS MOCK-LFCS-4] LFCS Full-Scale Timed Mock Exam 4 (Benchmark)

**Date:** 2026-11-26  
**Time Limit:** 120m  
**Passing Score:** 67%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# LFCS Full-Scale Timed Mock Exam 4 (Benchmark)

**Passing Score:** 67% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Environment:** VirtualBox Ubuntu LFCS VM (`student@172.16.16.16`)

---

### Linux Foundation Official Domain Weights:
1. **Operations Deployment (25%)**
   - Configure kernel parameters, persistent and non-persistent
   - Diagnose, identify, manage, and troubleshoot processes and services
   - Manage or schedule jobs for executing commands
   - Search for, install, validate, and maintain software packages or repositories
   - Manage Virtual Machines and containers
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Monitor and troubleshoot networking
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Text manipulation and log analysis
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Archive and compress files
   - Work with SSL certificates and Git
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits and granular privilege escalation
   - Configure and manage ACLs and user aging policies

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** Advanced text analysis and columnar calculation with `awk`:
  - A CSV sales report is located at `/var/tmp/mock-lfcs-4/sales.csv` with fields `ID,Product,Department,Price,Quantity`.
  - Calculate the total sales revenue (`Price * Quantity`) for all items in the `Electronics` department.
  - Write the single calculated numerical sum into `/var/tmp/mock-lfcs-4/electronics_total.txt`.
- **Q2:** Bulk file permission hardening with `find -exec`:
  - In directory tree `/var/tmp/mock-lfcs-4/archive_vault`, find all regular files ending in `.bak` or `.old` that have modification time older than 7 days (`-mtime +7`).
  - Change their file permissions to `0600` (`chmod 600`) using `find ... -exec chmod 600 {} +`.
  - Save the sorted list of matched file paths into `/var/tmp/mock-lfcs-4/vault_audit.txt`.
- **Q3:** SSL/TLS Certificate Expiration & Fingerprint Inspection:
  - A TLS certificate is located at `/var/tmp/mock-lfcs-4/production.crt`.
  - Use `openssl x509` to extract its expiration date (`-enddate`), issuer organization (`-issuer`), and SHA256 fingerprint (`-fingerprint -sha256`) without opening an editor.
  - Write the extracted details to `/var/tmp/mock-lfcs-4/cert-summary.txt`.
- **Q4:** Git Commit Cherry-picking:
  - In repository `/var/tmp/mock-lfcs-4/code-repo`, branch `hotfix` contains a critical patch with commit message `"HOTFIX: fix buffer overflow"`.
  - On branch `main`, cherry-pick this commit to integrate it into `main`.
  - Ensure the commit is recorded in `main` history.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Custom Systemd Slice Resource Management:
  - Create a custom systemd slice unit file at `/etc/systemd/system/batch.slice` with `MemoryMax=128M` and `CPUWeight=150`.
  - Configure the existing service `/etc/systemd/system/batch-worker.service` to run inside `batch.slice` (`Slice=batch.slice`).
  - Reload systemd daemon configuration and restart `batch-worker.service`.
- **Q6:** Kernel Parameter Hardening via `/etc/sysctl.d/`:
  - Configure persistent network security parameters in `/etc/sysctl.d/99-security.conf`:
    - `net.ipv4.conf.all.accept_source_route = 0`
    - `net.ipv4.icmp_echo_ignore_broadcasts = 1`
    - `net.ipv4.tcp_syncookies = 1`
  - Apply the configuration immediately using `sysctl --system`.
- **Q7:** Automated Scheduled Backup Script with Rsync:
  - Create an automated backup script at `/usr/local/bin/system_backup.sh` (executable).
  - The script must synchronize directory `/var/tmp/mock-lfcs-4/data/` to `/var/tmp/mock-lfcs-4/backup/` using `rsync -a --delete`.
  - If the rsync succeeds, append `"SUCCESS: $(date)"` to `/var/log/backup_sync.log`. If it fails, append `"FAILED: $(date)"` to `/var/log/backup_sync.log`.
- **Q8:** Dynamic Linker Shared Library Configuration:
  - A custom shared library `libcustom.so` is located in directory `/opt/customlib`.
  - Configure the dynamic linker to include `/opt/customlib` by creating configuration file `/etc/ld.so.conf.d/customlib.conf`.
  - Update the dynamic linker runtime cache with `ldconfig` and verify `/opt/customlib` is indexed in `ldconfig -p`.
- **Q9:** Container Deployment with Volume Mount and Environment Variable (Podman):
  - Run a detached Podman container named `mock-backup-job` using image `docker.io/library/alpine`.
  - Set environment variable `BACKUP_INTERVAL=3600` (`-e BACKUP_INTERVAL=3600`).
  - Mount host directory `/var/tmp/mock-lfcs-4/cdata` to `/data:Z` in the container (`-v /var/tmp/mock-lfcs-4/cdata:/data:Z`).
  - Execute command `sh -c "echo active > /data/status.txt && sleep 3600"` in detached mode.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** HAProxy Layer 7 HTTP Load Balancer Configuration:
  - Configure HAProxy (`/etc/haproxy/haproxy.cfg`) with a frontend `mock_front` binding to `*:8088` and default backend `mock_back`.
  - In `mock_back`, configure roundrobin load balancing between `127.0.0.1:9001` and `127.0.0.1:9002` with health checks (`check`).
  - Ensure HAProxy service is enabled, started, and listening on port `8088`.
- **Q11:** Network Bonding Configuration (`bond0`):
  - Create a network bonding interface named `bond0` with `mode active-backup` and `miimon 100` (`ip link add bond0 type bond mode active-backup miimon 100`).
  - Attach slave dummy interfaces `veth-bond1` and `veth-bond2` to `bond0` (`ip link set veth-bond1 master bond0`, etc.).
  - Assign IP `192.168.99.10/24` to `bond0` and bring `bond0`, `veth-bond1`, and `veth-bond2` up.
- **Q12:** Iptables Stateful Packet Filtering & Rate Limiting:
  - In `iptables` INPUT chain:
    - Append a stateful rule allowing established and related connections: `-m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`.
    - Append a rule limiting incoming ICMP echo requests to 2 per second: `-p icmp --icmp-type echo-request -m limit --limit 2/second -j ACCEPT`.
  - Save the INPUT chain rules to `/var/tmp/mock-lfcs-4/iptables-input.txt`.
- **Q13:** Network Socket States Audit with `ss`:
  - Use `ss` socket statistics utility:
    - Extract all established TCP sockets with process details (`ss -t -a state established -p`) and save to `/var/tmp/mock-lfcs-4/tcp-established.txt`.
    - Extract all listening UDP sockets (`ss -u -l -n`) and save to `/var/tmp/mock-lfcs-4/udp-listening.txt`.
- **Q14:** 802.1Q VLAN Tagging Interface:
  - Create an 802.1Q tagged VLAN interface named `dummy0.50` on top of base interface `dummy0` with VLAN ID `50` (`ip link add link dummy0 name dummy0.50 type vlan id 50`).
  - Assign IP address `10.50.50.1/24` to `dummy0.50` and bring the interface up.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Storage Performance Monitoring with `iotop` & Active Process Tracking:
  - Run `iotop -b -n 3 -d 1 -o` in batch mode to capture processes actively performing disk I/O and save the output to `/var/tmp/mock-lfcs-4/iotop-report.txt`.
  - A background generator script is performing high disk write activity. Parse the process command name doing the high disk write into `/var/tmp/mock-lfcs-4/high-io-proc.txt`.
- **Q16:** Automounter Indirect Map (`autofs`):
  - Configure `autofs` indirect automounting under root mount `/shares`:
    - In `/etc/auto.master.d/shares.autofs`, configure `/shares /etc/auto.shares --timeout=60`.
    - In `/etc/auto.shares`, define map entry `docs` to mount `/var/tmp/mock-lfcs-4/storage_export` with options `-fstype=bind,rw`.
    - Restart `autofs` (`systemctl restart autofs`) and verify accessing `/shares/docs` automatically mounts the export.
- **Q17:** LVM Striped Logical Volume Creation:
  - In Volume Group `mock-vg4` (composed of two physical loop volumes), create a 2-stripe Logical Volume named `mock-striped` of size `50M` with stripe size `64k` (`lvcreate -i 2 -I 64k -L 50M -n mock-striped mock-vg4`).
  - Format `/dev/mock-vg4/mock-striped` with `ext4`.
- **Q18:** Filesystem Disk Quotas:
  - A filesystem is mounted at `/var/tmp/mock-lfcs-4/quota_mount` with user quota support enabled (`usrquota`).
  - Assign user `tester-quota` a block soft limit of `40MB` (40960 KB) and hard limit of `60MB` (61440 KB) using `setquota -u tester-quota 40960 61440 0 0 /var/tmp/mock-lfcs-4/quota_mount`.
  - Confirm the quota configuration with `quota -v -u tester-quota`.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Centralized Identity Lookup Configuration (SSSD / NSS):
  - In `/etc/nsswitch.conf`, ensure `passwd:` and `group:` queries include `sss` (e.g., `passwd: files systemd sss` and `group: files systemd sss`).
  - In `/etc/sssd/sssd.conf`, ensure file permissions are `0600` owned by `root:root`.
  - Configure a basic local domain in `/etc/sssd/sssd.conf` with `domains = local`, `[domain/local]`, and `id_provider = local`.
- **Q20:** User Account Expiration & Initial Login Password Change:
  - Create a temporary auditor account named `temp-auditor` with account expiration date set to `2026-12-31` (`useradd -e 2026-12-31 temp-auditor`).
  - Force the user to change their password on their very first login (`chage -d 0 temp-auditor`).
  - Verify configuration with `chage -l temp-auditor`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-lfcs-4
```
