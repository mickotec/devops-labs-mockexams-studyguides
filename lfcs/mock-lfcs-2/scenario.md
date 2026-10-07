# [LFCS MOCK-LFCS-2] LFCS Full-Scale Timed Mock Exam 2

**Date:** 2026-11-18  
**Time Limit:** 120m  
**Passing Score:** 67%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# LFCS Full-Scale Timed Mock Exam 2

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
- **Q1:** An automated deployment pipeline requires applying text modifications to an application configuration file:
  - In `/var/tmp/mock-lfcs-2/app.conf`, change the listener port by updating line `PORT = 8080` to `PORT = 9000`.
  - Remove all lines containing the string `DEBUG`.
  - Insert a new configuration line `ENV = production` immediately following the section header `[app]`.
  - Save the changes directly to `/var/tmp/mock-lfcs-2/app.conf`.
- **Q2:** Analyze system log files to identify active services generating excessive log volume:
  - Process the log entries in `/var/tmp/mock-lfcs-2/sample_syslog`.
  - Calculate message frequencies by process name and determine the top 3 processes generating the most log messages.
  - Save the top process ranking into `/var/tmp/mock-lfcs-2/top_loggers.txt`.
- **Q3:** Generate and apply a unified diff patch between software source revisions:
  - Compare `/var/tmp/mock-lfcs-2/fileA` and `/var/tmp/mock-lfcs-2/fileB` and create a unified diff patch file saved to `/var/tmp/mock-lfcs-2/patch.diff`.
  - Apply the generated patch to target file `/var/tmp/mock-lfcs-2/fileTarget` so its contents are updated to match `fileB`.
- **Q4:** Conduct a storage utilization audit under the system log directory:
  - Inspect directory `/var/log` to find the 3 largest regular files.
  - Record their full file paths and sizes into `/var/tmp/mock-lfcs-2/largest_files.txt`.

#### Domain: Operations Deployment (25% Weight - 5 Questions, 5.0% each)
- **Q5:** Schedule a periodic maintenance task using native systemd timer units:
  - Create a systemd service unit `/etc/systemd/system/mock-cleanup.service` executing `/bin/echo 'Cleaning temporary cache'`.
  - Create a companion timer unit `/etc/systemd/system/mock-cleanup.timer` scheduled to trigger every 15 minutes.
  - Reload systemd, enable the timer, and activate it so it is actively scheduled.
- **Q6:** Manage process scheduling priorities by launching and renicing a running process:
  - Start the command `sleep 600` with an initial scheduling nice value of `10`.
  - While running, dynamically adjust the process's nice priority to `15`.
  - Verify the modified scheduling priority and save the process PID and nice level to `/var/tmp/mock-lfcs-2/nice_proc.txt`.
- **Q7:** Route application facility log messages to a dedicated log destination:
  - In `/etc/rsyslog.d/`, create configuration file `40-custom.conf`.
  - Configure the logging daemon to route all messages from facility `local5.*` to file `/var/log/custom-app.log`.
  - Restart or reload the rsyslog daemon to apply the new logging rule.
- **Q8:** Document the operating system target configuration:
  - Query the system service manager to identify the current default systemd target.
  - Write the exact default target name into file `/var/tmp/mock-lfcs-2/boot-target.txt`.
- **Q9:** Prevent unexpected major software updates by configuring package pinning:
  - In directory `/etc/apt/preferences.d/`, create an APT preferences file named `pin-package`.
  - Configure package pinning for package `nginx` setting its package pin priority to `999`.

#### Domain: Networking (25% Weight - 5 Questions, 5.0% each)
- **Q10:** Create a virtual network interface for localized software testing:
  - Create a virtual dummy network interface named `dummy0`.
  - Assign the IPv4 address `10.99.99.1` with subnet mask `/24` to `dummy0`.
  - Bring the interface to an `UP` state and verify its address assignment.
- **Q11:** Open inbound network access for a web service through the firewall:
  - Add an iptables packet filtering rule to allow incoming TCP traffic on destination port `8080` in the `INPUT` chain.
  - Export the active `INPUT` chain rule set with numeric addresses and ports to `/var/tmp/mock-lfcs-2/iptables.txt`.
- **Q12:** Identify the daemon bound to the remote access port for a security audit:
  - Inspect the system socket table to determine which process is listening on TCP port 22.
  - Save the process name and process ID (PID) to `/var/tmp/mock-lfcs-2/ssh-proc.txt`.
- **Q13:** Verify DNS resolver configuration:
  - Query the local DNS stub resolver status.
  - Record the current active upstream DNS server IP address into `/var/tmp/mock-lfcs-2/dns-server.txt`.
- **Q14:** Configure static network routing for remote network communication:
  - Add a static route for destination network `192.168.100.0/24`.
  - Route traffic via next-hop gateway `10.99.99.254` reachable over interface `dummy0` (enable onlink if required).
  - Confirm the route is registered in the kernel routing table.

#### Domain: Storage (20% Weight - 4 Questions, 5.0% each)
- **Q15:** Create a point-in-time storage snapshot for backup verification:
  - In volume group `mock-vg2`, locate logical volume `data-lv`.
  - Create a 20 Megabyte snapshot named `data-snap` of the logical volume.
  - Confirm the snapshot is active in logical volume reporting tools.
- **Q16:** Optimize disk space availability on an ext4 filesystem:
  - Examine the ext4 filesystem image at `/var/tmp/mock-lfcs-2/tunable.img`.
  - Modify the reserved blocks percentage allocated to the super-user so that it is reduced to `1%`.
  - Verify the change in filesystem parameters.
- **Q17:** Configure persistent filesystem mounting with performance and security options:
  - Add an entry to `/etc/fstab` to persistently mount filesystem path `/var/tmp/mock-lfcs-2/mnt-point`.
  - Apply mount options `noatime` (suppress access time updates) and `nodev` (prevent device node interpretation).
- **Q18:** Create and activate a secure virtual memory swap file:
  - Create a 128 Megabyte swap file at `/var/tmp/mock-lfcs-2/swapfile2`.
  - Set file permissions so only root has read and write privileges (`600`).
  - Format the file for swap and activate it immediately.

#### Domain: Users and Groups (10% Weight - 2 Questions, 5.0% each)
- **Q19:** Implement strict password security policies for user accounts:
  - Configure password aging parameters for user `student`:
    - Maximum password lifetime: 60 days
    - Minimum days required between password changes: 7 days
    - Advance warning period prior to expiration: 14 days
  - Verify the password aging policy using account aging utilities.
- **Q20:** Establish default skeleton files for new user provisioning:
  - In the default user skeleton directory `/etc/skel`, add a file named `.custom_profile` (containing `# Custom User Profile`).
  - Create a new user account named `newhire` ensuring standard home directory initialization.
  - Confirm `/home/newhire/.custom_profile` was automatically provisioned upon account creation.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-lfcs-2
```
