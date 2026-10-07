# [LFCS MOCK-LFCS-1] LFCS Full-Scale Timed Mock Exam 1

**Date:** 2026-11-17  
**Time Limit:** 120m  
**Passing Score:** 67%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# LFCS Full-Scale Timed Mock Exam 1

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
   - Recover from hardware, operating system, or filesystem failures
   - Manage Virtual Machines (libvirt)
   - Configure container engines, create and manage containers
   - Create and enforce MAC using SELinux
2. **Networking (25%)**
   - Configure IPv4 and IPv6 networking and hostname resolution
   - Set and synchronize system time using time servers
   - Monitor and troubleshoot networking
   - Configure the OpenSSH server and client
   - Configure packet filtering, port redirection, and NAT
   - Configure static routing
   - Configure bridge and bonding devices
   - Implement reverse proxies and load balancers
3. **Storage (20%)**
   - Configure and manage LVM storage
   - Manage and configure the virtual file system
   - Create, manage, and troubleshoot filesystems
   - Use remote filesystems and network block devices
   - Configure and manage swap space
   - Configure filesystem automounters
   - Monitor storage performance
4. **Essential Commands (20%)**
   - Basic Git Operations
   - Create, configure, and troubleshoot services
   - Monitor and troubleshoot system performance and services
   - Determine application and service specific constraints
   - Troubleshoot diskspace issues
   - Work with SSL certificates
5. **Users and Groups (10%)**
   - Create and manage local user and group accounts
   - Manage personal and system-wide environment profiles
   - Configure user resource limits
   - Configure and manage ACLs
   - Configure the system to use LDAP user and group accounts

---

### Questions Overview:

#### Domain: Essential Commands (20% Weight - 4 Questions, 5.0% each)
- **Q1:** Initialize a standard Git source code management workflow for a project in `/var/tmp/mock-lfcs-1/git-repo`:
  - Create a new Git repository in `/var/tmp/mock-lfcs-1/git-repo`.
  - Add a file named `README.md` with the content `# Master Repo` and commit it to branch `main`.
  - Create and switch to a new branch named `feature`.
  - In branch `feature`, add a file named `feature.txt` with content `new feature` and commit the file.
  - Return to branch `main` and merge branch `feature` into `main` so the commit history records the integration.
- **Q2:** A custom monitoring script `/usr/local/bin/mock_monitor.sh` needs to be managed as a continuous background daemon:
  - Create a custom systemd service unit file at `/etc/systemd/system/mock-monitor.service`.
  - Configure the unit to run `/usr/local/bin/mock_monitor.sh` (which logs timestamps to `/var/tmp/mock-lfcs-1/monitor.log`).
  - Reload systemd daemon configuration, enable the service to start at boot, and start it immediately.
  - Verify that the service status is active and running.
- **Q3:** Perform a disk space audit to identify recently modified large files in `/var/tmp/mock-lfcs-1`:
  - Locate all regular files within `/var/tmp/mock-lfcs-1` that were modified within the past 7 days and exceed 100 Kilobytes in size.
  - Save the list of matched file paths into `/var/tmp/mock-lfcs-1/large-files.txt`.
- **Q4:** Extract metadata from an X.509 certificate for a security compliance audit:
  - Inspect the SSL/TLS certificate located at `/var/tmp/mock-lfcs-1/exam.crt`.
  - Extract the certificate's subject, issuer, and expiration date.
  - Save the extracted certificate details into `/var/tmp/mock-lfcs-1/cert-info.txt`.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Optimize memory management by tuning the kernel swappiness parameter:
  - Set the kernel parameter `vm.swappiness` to value `10`.
  - Ensure the setting persists across system reboots by placing a sysctl configuration file at `/etc/sysctl.d/99-swappiness.conf`.
  - Apply the change immediately to the active kernel without rebooting the system.
- **Q6:** Establish an automated cron job for administrative logging under user `student`:
  - Configure a user crontab for user `student`.
  - Schedule command `/bin/echo 'Cron job executed'` to run at 02:30 AM every weekday (Monday through Friday).
  - Confirm the schedule is installed and visible in `student`'s crontab listing.
- **Q7:** Query the package management database to audit installed package artifacts:
  - Query all installed files belonging to the package `tar`.
  - Write the complete file listing into `/var/tmp/mock-lfcs-1/pkg-files.txt`.
- **Q8:** Launch an asynchronous background process and record its process ID for operational tracking:
  - Launch the command `sleep 9999` in the background.
  - Determine the process ID (PID) of this active command.
  - Write only the numeric PID to file `/var/tmp/mock-lfcs-1/sleep.pid`.
- **Q9:** Provision a lightweight containerized web server to verify container runtime functionality:
  - Using the available container engine (Docker or Podman), run a detached container named `mock-web`.
  - Deploy using container image `nginx:alpine`.
  - Expose container port 80 by publishing it to host port `8088`.
  - Verify that `mock-web` is running.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Configure static host name resolution for local system services:
  - Edit the system's static host lookup table (`/etc/hosts`).
  - Map host name `exam.local` to the loopback IPv4 address `127.0.0.1`.
- **Q11:** Inspect and document the system's time synchronization and timezone configuration:
  - Query the status of system time, time zone, and network time synchronization.
  - Save the command output to file `/var/tmp/mock-lfcs-1/time-status.txt`.
- **Q12:** Conduct a network port audit to document all actively listening TCP sockets:
  - Query all listening TCP sockets along with associated process identifiers.
  - Write the socket table output into `/var/tmp/mock-lfcs-1/listening-ports.txt`.
- **Q13:** Implement SSH server hardening in accordance with corporate security standards:
  - Create a drop-in configuration file at `/etc/ssh/sshd_config.d/99-hardening.conf`.
  - Disable direct remote root login (`PermitRootLogin no`).
  - Restrict the maximum authentication attempts per connection to 3 (`MaxAuthTries 3`).
  - Validate the SSH configuration syntax to confirm no syntax errors exist.
- **Q14:** Document active firewall packet filtering rules for network security auditing:
  - Query the system's active packet filtering rules and chains.
  - Save the active firewall rules table to file `/var/tmp/mock-lfcs-1/firewall-rules.txt`.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Provision a raw block storage container file and create an ext4 filesystem:
  - Create a 100 Megabyte zero-filled image file at `/var/tmp/mock-lfcs-1/disk1.img`.
  - Format the image file with an `ext4` filesystem.
  - Confirm filesystem creation.
- **Q16:** Configure Logical Volume Management (LVM) storage components on loop storage:
  - Associate `/var/tmp/mock-lfcs-1/disk1.img` with a loop device and initialize it as an LVM Physical Volume.
  - Create a Volume Group named `mock-vg` using the physical volume.
  - Within `mock-vg`, create a Logical Volume named `mock-lv` with an initial size of `50MB`.
  - Format `mock-lv` as `ext4` and mount it at directory `/var/tmp/mock-lfcs-1/lvm-mount`.
- **Q17:** Dynamically expand logical volume storage to accommodate capacity growth:
  - Extend logical volume `mock-lv` in volume group `mock-vg` to a total size of `80MB`.
  - Resize the underlying `ext4` filesystem online so the additional storage is immediately available.
  - Verify that `lvs` and filesystem reports show the updated 80MB size.
- **Q18:** Allocate and activate additional virtual memory swap storage:
  - Create a 64 Megabyte swap file at `/var/tmp/mock-lfcs-1/swapfile`.
  - Secure the file permissions so that only the root user has read and write access.
  - Format the file as swap space and enable it immediately.
  - Verify that the swap file is active in system swap allocations.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Create project accounts and configure granular POSIX filesystem access controls:
  - Create user `devops` with specific UID `2001`.
  - Create user `tester` with specific UID `2002`.
  - Create group `infrateam` with specific GID `3001`.
  - Configure POSIX Access Control Lists (ACLs) on directory `/var/tmp/mock-lfcs-1/shared` granting group `infrateam` read, write, and execute (`rwx`) permissions.
- **Q20:** Configure process resource limits and user password aging policies:
  - In `/etc/security/limits.conf`, set both soft and hard open file limits (`nofile`) to `4096` for user `student`.
  - Configure password aging for user `student` such that passwords must be changed at least every 90 days.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-lfcs-1
```
