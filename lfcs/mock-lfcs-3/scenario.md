# [LFCS MOCK-LFCS-3] LFCS Full-Scale Timed Mock Exam 3

**Date:** 2026-11-24  
**Time Limit:** 120m  
**Passing Score:** 67%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# LFCS Full-Scale Timed Mock Exam 3

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
   - Configure user resource limits and granular privilege escalation (sudoers)
   - Configure and manage ACLs and special permissions (SGID, sticky bit)

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** An Apache HTTP web server log file `/var/tmp/mock-lfcs-3/web_access.log` records client interactions.
  - Parse the log file to extract all unique client IP addresses (column 1) that received HTTP client/server error response status codes (`4xx` or `5xx` in column 9).
  - Sort the IP addresses numerically and save the unique list into `/var/tmp/mock-lfcs-3/error_ips.txt`.
- **Q2:** Generate an SSL Certificate Signing Request (CSR) and Private Key for an internal service:
  - Generate an RSA 2048-bit private key without passphrase at `/var/tmp/mock-lfcs-3/server.key`.
  - Create a Certificate Signing Request (CSR) at `/var/tmp/mock-lfcs-3/server.csr` with Common Name `lfcs.local` and Subject Alternative Names `DNS:lfcs.local,DNS:api.lfcs.local`.
- **Q3:** Create a multi-threaded compressed archive and verify its integrity:
  - Archive directory `/var/tmp/mock-lfcs-3/source_data` into `/var/tmp/mock-lfcs-3/backup.tar.xz` using `tar` with multithreaded `xz` compression (`-T0`).
  - Calculate the SHA256 checksum of `/var/tmp/mock-lfcs-3/backup.tar.xz` and save it to `/var/tmp/mock-lfcs-3/backup.tar.xz.sha256` in standard checksum format (`<sha256sum>  <filename>`).
- **Q4:** In Git repository `/var/tmp/mock-lfcs-3/git-app`:
  - Create an annotated release tag named `v1.2.0` on the current HEAD commit with annotation message `"Production Release 1.2.0"`.
  - Create and checkout a new branch named `release-1.2` starting from this tag.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Enforce cgroup resource control drop-in for systemd service `mock-worker.service`:
  - Create a systemd drop-in configuration directory at `/etc/systemd/system/mock-worker.service.d/` and drop-in file `limits.conf`.
  - Configure resource limits: `MemoryMax=64M` and `CPUQuota=40%`.
  - Reload systemd daemon configuration and restart `mock-worker.service`.
- **Q6:** Permanently blacklist legacy kernel module `cramfs`:
  - Create configuration file `/etc/modprobe.d/blacklist-cramfs.conf` containing `blacklist cramfs` and `install cramfs /bin/true`.
  - Ensure the module is unloaded from the running kernel.
- **Q7:** Query systemd journal logs to diagnose priority failures:
  - Use `journalctl` to extract all system log messages with priority level `err` or higher (`-p err..emerg`) generated since `2026-01-01`.
  - Save the extracted diagnostic log entries to `/var/tmp/mock-lfcs-3/system_errors.log`.
- **Q8:** Implement a graceful daemon reload script:
  - A running application PID is recorded in `/var/run/mock-app.pid`.
  - Create an executable bash script `/usr/local/bin/reload_mock_app.sh`.
  - When executed, the script must read `/var/run/mock-app.pid`, send signal `SIGHUP` (`kill -HUP $PID`) to trigger configuration reload without killing the daemon, and append `"RELOAD SIGNAL SENT"` with the timestamp to `/var/tmp/mock-lfcs-3/signal.log`.
- **Q9:** Container lifecycle and restart management with Podman:
  - Launch a detached Podman container named `mock-web-c3` from image `docker.io/library/nginx:alpine`.
  - Configure restart policy `--restart always` and map host port `8085` to container port `80` (`-p 8085:80`).
  - Verify the container status is running.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Configure Nginx as an HTTP Reverse Proxy Load Balancer:
  - Two backend applications are running on ports `8081` and `8082`.
  - Configure Nginx in `/etc/nginx/conf.d/proxy-balance.conf` with upstream `backend_nodes` distributing requests across `127.0.0.1:8081` and `127.0.0.1:8082` using round-robin.
  - Configure a server block listening on port `8080` that proxies all incoming requests (`location /`) to `http://backend_nodes`.
  - Test configuration syntax and reload or restart Nginx.
- **Q11:** Linux Network Bridge Configuration:
  - Create a network bridge interface named `br0` (`ip link add br0 type bridge`).
  - Attach interface `veth-br1` as a slave port to `br0` (`ip link set veth-br1 master br0`).
  - Assign IP address `192.168.50.1/24` to `br0` and bring both `br0` and `veth-br1` up.
- **Q12:** Port Redirection with Iptables NAT:
  - In `iptables` NAT table, append a PREROUTING rule to redirect incoming TCP traffic destined for port `8443` to local port `443` (`-p tcp --dport 8443 -j REDIRECT --to-ports 443`).
  - Save the active NAT table rules to `/var/tmp/mock-lfcs-3/nat-rules.txt`.
- **Q13:** Network Packet Capture with `tcpdump`:
  - Run `tcpdump` to capture exactly 5 TCP packets arriving on loopback interface `lo` for destination port `9999`.
  - Save the captured raw packets to `/var/tmp/mock-lfcs-3/traffic.pcap`.
- **Q14:** Static Network Route with Metric:
  - Add a static network route for destination network `10.150.0.0/16` via gateway `10.99.99.1` on device `dummy0` with a specific route metric of `150`.
  - Ensure the route appears in the active kernel routing table.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Storage Performance and I/O Activity Monitoring:
  - Use `iostat -x -d 1 3` to collect extended disk utilization statistics and write the output to `/var/tmp/mock-lfcs-3/io-report.txt`.
  - Use `sar -d 1 3` to record real-time block I/O activity and save the report to `/var/tmp/mock-lfcs-3/sar-disk.txt`.
  - Both reports must include device metrics (`%util` or `await`).
- **Q16:** Filesystem Automounter (`autofs`) Direct Map:
  - Configure `autofs` direct automount:
    - Create direct master map configuration `/etc/auto.master.d/direct.autofs` containing `/- /etc/auto.direct --timeout=60`.
    - In `/etc/auto.direct`, configure direct mountpoint `/mnt/auto-data` pointing to ext4 disk `/var/tmp/mock-lfcs-3/auto.img` with options `-fstype=ext4,loop,rw`.
    - Restart `autofs` (`systemctl restart autofs`) and verify accessing `/mnt/auto-data` automatically mounts the volume.
- **Q17:** LVM Thin Provisioning:
  - Inside Volume Group `mock-vg3`, create an LVM thin pool named `mock-pool` with data size `50MB` (`lvcreate -L 50M -T mock-vg3/mock-pool`).
  - Create a thin provisioned volume named `mock-thin` with virtual size `150MB` from `mock-pool` (`lvcreate -V 150M -T mock-vg3/mock-pool -n mock-thin`).
  - Format `/dev/mock-vg3/mock-thin` with filesystem `ext4`.
- **Q18:** Persistent Mount by UUID with Security Mount Options:
  - Obtain the filesystem UUID of `/var/tmp/mock-lfcs-3/secure_store.img` using `blkid`.
  - Create mount directory `/mnt/secure-data`.
  - Configure `/etc/fstab` to persistently mount the filesystem by its UUID (`UUID=<uuid>`) to `/mnt/secure-data` with options `noexec,nosuid,nodev`.
  - Mount the filesystem using `mount -a`.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Granular Sudoers Delegation (`/etc/sudoers.d/`):
  - User `developer` requires administrative privileges restricted strictly to commands `/usr/bin/systemctl restart nginx` and `/usr/bin/journalctl`.
  - Create a sudoers drop-in file at `/etc/sudoers.d/90-developer` with file mode `0440`.
  - Grant user `developer` execution privileges for those two commands without requiring a password prompt (`NOPASSWD:`).
- **Q20:** SGID and Sticky Bit Collaborative Workspace:
  - Create a team directory at `/var/tmp/mock-lfcs-3/team_collab` owned by user `student` and group `devteam`.
  - Set permissions to `2775` (rwxrwsr-x with SGID set).
  - Create subdirectory `/var/tmp/mock-lfcs-3/team_collab/dropzone` with permissions `1777` (rwxrwxrwt with sticky bit set) so users cannot remove files owned by others.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-lfcs-3
```
